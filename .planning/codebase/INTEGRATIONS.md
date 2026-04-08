# External Integrations

**Analysis Date:** 2026-04-08

## APIs & External Services

**LLM - Azure OpenAI:**
- Purpose: Code summarization, documentation generation
- SDK/Client: `openai` Python package v1.91.0+
- Auth: API key in `AZURE_OPENAI_API_KEY` env var
- Configuration:
  - `OPENAI_API_TYPE = azure`
  - `OPENAI_API_VERSION = 2024-08-01-preview`
  - `AZURE_OPENAI_ENDPOINT` - Azure resource endpoint URL
- Endpoints: Chat completions for code analysis/summarization
- Usage: Tested with structured outputs for summarizing C code blocks

**LLM - NVIDIA NIMs:**
- Purpose: Alternative LLM inference endpoint (potentially for local/self-hosted models)
- SDK/Client: `openai` Python package (OpenAI-compatible API)
- Auth: API key in `NIMS_API_KEY` env var
- Configuration:
  - `NIMS_BASE_URL = https://integrate.api.nvidia.com/v1`
- Status: Configured but primary usage appears to be Azure OpenAI
- Note: Uses OpenAI-compatible interface via NVIDIA's API gateway

**Tested Models:**
- `gemma2:9b-instruct-q8_0` - Local Ollama model tested for structured output generation
- Tested on: `bootp.c` from Linux kernel (Alpha architecture boot code)
- Finding: Structured outputs work but quality varies by model size

## Data Storage

**Graph Database - Kuzu:**
- Purpose: Index and query Linux kernel codebase structure as a graph
- Client: `kuzu` Python package v0.10.0+
- Storage: Local embedded database in `kuzu_db/` directory (gitignored)
- Visualization: `yfiles-jupyter-graphs` + `yfiles-jupyter-graphs-for-kuzu` for interactive graph rendering in notebooks
- Usage: Querying file extensions, code structure, relationships between kernel components

## Reference Data (Git Submodules)

**Linux Kernel Source:**
- Source: `https://github.com/torvalds/linux.git`
- Purpose: Primary codebase for documentation agent development
- Size: ~35,587 C files, ~26,992 H files, thousands of other file types
- Integration: Read-only source for analysis pipeline
- Location: `00-supporting-files/data/linux-kernel/`

**AG2 Framework:**
- Source: `https://github.com/ag2ai/ag2.git`
- Purpose: Reference for multi-agent AI patterns and architecture
- Size: Full Python framework with extensive test suite
- Integration: Reference material for agent design decisions
- Location: `00-supporting-files/data/ag2-framework/`

## Authentication & Identity

**No application-level auth exists yet.** API keys are managed via:
- `.env` files (gitignored, template in `00-supporting-files/data/sample.env.file`)
- python-dotenv for loading environment variables
- No user authentication system

## Monitoring & Observability

**None configured.**
- No error tracking (Sentry, etc.)
- No analytics
- No structured logging
- Notebook output serves as the only observability mechanism

## CI/CD & Deployment

**None configured.**
- No CI pipeline
- No automated deployment
- No staging/production environments
- Manual git push to origin

## Environment Configuration

**Development:**
- Required env vars: `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`
- Optional: `NIMS_BASE_URL`, `NIMS_API_KEY`
- Secrets location: `.env` file in supporting files directory (gitignored)
- Template: `00-supporting-files/data/sample.env.file`

**Staging/Production:**
- Not applicable (no deployment target yet)

## Webhooks & Callbacks

**None.** No incoming or outgoing webhooks.

---

*Integration audit: 2026-04-08*
*Update when adding/removing external services*
