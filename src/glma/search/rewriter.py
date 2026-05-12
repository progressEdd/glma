"""LLM query rewriting for improved code search."""

from typing import Optional


DEFAULT_REWRITE_PROMPT = (
    "You are a code search assistant. Rewrite the user's query to be more effective "
    "at matching code documentation and summaries.\n\n"
    "Rules:\n"
    "- Expand abbreviations to full terms (auth → authentication, db → database, cfg → configuration)\n"
    "- Add likely descriptive terms that would appear in developer-focused code summaries\n"
    "- Preserve technical terms and exact identifiers (function names, class names, API paths)\n"
    "- Keep the original intent — do not add unrelated concepts\n"
    "- Use natural descriptive language about what code does (purpose, behavior, inputs, outputs)\n"
    "- Return ONLY the rewritten query string, no explanation"
)


def rewrite_query(
    query: str,
    base_url: str,
    model: str,
    rewrite_prompt: Optional[str] = None,
    timeout: float = 120.0,
    max_tokens: int = 100,
) -> str:
    """Rewrite a user search query using an LLM for better code search results.

    Args:
        query: Original user search query.
        base_url: OpenAI-compatible API base URL.
        model: Model name to use.
        rewrite_prompt: Custom system prompt. Uses DEFAULT_REWRITE_PROMPT if None.
        timeout: Request timeout in seconds.
        max_tokens: Maximum response tokens.

    Returns:
        Rewritten query string, or original query if rewrite fails/returns empty.

    Raises:
        ImportError: If the 'openai' package is not installed.
    """
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError(
            "Query rewriting requires the 'openai' package. "
            "Install with: pip install glma[ai]"
        )

    client = OpenAI(base_url=base_url, api_key="not-needed")

    system_prompt = rewrite_prompt if rewrite_prompt else DEFAULT_REWRITE_PROMPT

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
        max_tokens=max_tokens,
        timeout=timeout,
    )

    result = response.choices[0].message.content.strip()
    if not result:
        return query
    return result
