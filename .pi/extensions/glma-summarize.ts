/**
 * Glma Summarize Extension for pi
 *
 * Provides /glma-summarize command and glma_summarize tool for AI-powered
 * code chunk summarization using pi's model registry.
 *
 * Installation: Place in .pi/extensions/ (project-local) or ~/.pi/agent/extensions/ (global)
 * Reload: /reload in pi to pick up changes
 *
 * Configuration (.glma.toml):
 *   [summarize]
 *   model_hint = "fast"       # "fast", "capable", exact model ID, or empty for active model
 */

import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { Type } from "@sinclair/typebox";
import { execSync } from "node:child_process";
import * as fs from "node:fs";
import * as path from "node:path";

// Model hint resolution constants
const FAST_FAMILIES = ["haiku", "flash", "mini", "nano", "turbo", "tiny", "small"];
const CAPABLE_FAMILIES = ["opus", "sonnet", "gpt-4", "gpt-5", "ultra", "pro", "max"];

interface ProviderPreset {
    baseUrl: string;
    model: string;
}

const GLMA_PRESETS: Record<string, ProviderPreset> = {
    local: { baseUrl: "http://localhost:1234/v1", model: "default" },
    ollama: { baseUrl: "http://localhost:11434/v1", model: "llama3" },
    lmstudio: { baseUrl: "http://localhost:1234/v1", model: "default" },
    llamacpp: { baseUrl: "http://localhost:8080/v1", model: "default" },
    vllm: { baseUrl: "http://localhost:8000/v1", model: "default" },
    aphrodite: { baseUrl: "http://localhost:7860/v1", model: "default" },
};

interface ModelInfo {
    id: string;
    provider: string;
    cost: { input: number; output: number };
    baseUrl?: string;
}

/**
 * Resolve a model_hint string to an actual model from pi's registry.
 *
 * - "fast" → cheapest/fastest known model family
 * - "capable" → strongest known model family
 * - exact model ID → direct lookup
 * - empty/undefined → pi's current active model
 */
function resolveModelHint(
    hint: string,
    availableModels: ModelInfo[],
    currentModel: any,
): any | null {
    if (!hint || hint.trim() === "") return currentModel;

    if (hint === "fast") {
        // Prefer known fast families, fall back to cheapest by cost
        const fast = availableModels.filter((m) =>
            FAST_FAMILIES.some((f) => m.id.toLowerCase().includes(f)),
        );
        if (fast.length > 0) {
            return fast.sort(
                (a, b) => a.cost.input + a.cost.output - (b.cost.input + b.cost.output),
            )[0];
        }
        return (
            availableModels.sort(
                (a, b) => a.cost.input + a.cost.output - (b.cost.input + b.cost.output),
            )[0] ?? null
        );
    }

    if (hint === "capable") {
        // Prefer known capable families, fall back to most expensive by cost
        const capable = availableModels.filter((m) =>
            CAPABLE_FAMILIES.some((f) => m.id.toLowerCase().includes(f)),
        );
        if (capable.length > 0) {
            return capable.sort(
                (a, b) => b.cost.input + b.cost.output - (a.cost.input + a.cost.output),
            )[0];
        }
        return (
            availableModels.sort(
                (a, b) => b.cost.input + b.cost.output - (a.cost.input + a.cost.output),
            )[0] ?? null
        );
    }

    // Exact model ID — search across all providers
    return availableModels.find((m) => m.id === hint) ?? null;
}

/**
 * Run glma summarization by shelling out to the CLI.
 *
 * For local models: uses provider presets for base URL detection.
 * For cloud models: passes API key as env var and uses the cloud provider's base URL.
 */
async function runGlmaSummarize(hint: string, ctx: any): Promise<string> {
    const cwd = ctx.cwd;
    const available = ctx.modelRegistry.getAvailable();
    const model = resolveModelHint(hint, available, ctx.model);

    if (!model) {
        return `Error: Could not resolve model hint "${hint}". Available models: ${available.map((m: any) => m.id).join(", ")}`;
    }

    // Get auth for the model
    const auth = await ctx.modelRegistry.getApiKeyAndHeaders(model);
    if (!auth?.ok || !auth?.apiKey) {
        return `Error: No API key available for model ${model.provider}/${model.id}. Configure via /login or settings.`;
    }

    // Check if this is a local model (localhost URL or known preset)
    const isLocal =
        (model.baseUrl && (model.baseUrl.includes("localhost") || model.baseUrl.includes("127.0.0.1"))) ?? false;

    const env = { ...process.env };
    let command: string;

    if (isLocal) {
        // Find matching preset for the base URL
        const preset = Object.entries(GLMA_PRESETS).find(
            ([_, v]) => v.baseUrl === model.baseUrl,
        );
        const providerFlag = preset
            ? `--summarize-provider ${preset[0]}`
            : `--summarize-provider local`;
        command = `glma index --summarize ${providerFlag} --summarize-model ${model.id}`;
    } else {
        // Cloud model — pass URL and API key via env
        env.OPENAI_API_KEY = auth.apiKey;
        if (auth.headers) {
            Object.assign(env, auth.headers);
        }
        command = `glma index --summarize --summarize-provider local --ai-url ${model.baseUrl} --summarize-model ${model.id}`;
    }

    try {
        const output = execSync(command, {
            cwd,
            env,
            timeout: 300000, // 5 min timeout for large repos
            encoding: "utf-8",
        });
        return output || "Summarization complete.";
    } catch (e: any) {
        return `Error during summarization: ${e.message}`;
    }
}

/**
 * Read model_hint from .glma.toml [summarize] section.
 */
function readModelHint(cwd: string): string {
    const configPath = path.join(cwd, ".glma.toml");
    if (!fs.existsSync(configPath)) return "";

    const content = fs.readFileSync(configPath, "utf-8");
    const match = content.match(/model_hint\s*=\s*["']([^"']+)["']/);
    return match ? match[1] : "";
}

export default function (pi: ExtensionAPI) {
    // Register /glma-summarize command
    pi.registerCommand("glma-summarize", {
        description: "Summarize codebase chunks using AI via pi's model registry",
        handler: async (_args, ctx) => {
            ctx.ui.notify("Starting glma summarization...", "info");

            const hint = readModelHint(ctx.cwd);
            const result = await runGlmaSummarize(hint, ctx);
            ctx.ui.notify(
                result,
                result.startsWith("Error") ? "error" : "success",
            );
        },
    });

    // Register glma_summarize tool (callable by LLM agents)
    pi.registerTool({
        name: "glma_summarize",
        label: "Glma Summarize",
        description:
            "Trigger codebase summarization using glma. Generates AI summaries for code chunks that don't have them yet. Runs /glma-summarize command in the background.",
        parameters: Type.Object({
            model_hint: Type.Optional(
                Type.String({
                    description:
                        "Model hint: 'fast' (cheapest), 'capable' (strongest), exact model ID, or empty for pi's current model",
                }),
            ),
        }),
        async execute(
            _toolCallId: string,
            params: { model_hint?: string },
            _signal: any,
            _onUpdate: any,
            ctx: any,
        ) {
            const hint = params.model_hint || "";
            const result = await runGlmaSummarize(hint, ctx);
            return {
                content: [{ type: "text", text: result }],
                details: { model_hint: hint, result },
            };
        },
    });
}
