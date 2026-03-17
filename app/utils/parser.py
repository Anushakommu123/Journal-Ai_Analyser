import json


def parse_llm_response(raw_response: str) -> dict:
    """Parse the LLM response string into a Python dictionary.

    Handles common LLM output issues:
    - Markdown code block wrappers (```json ... ```)
    - Extra text before/after JSON
    - Whitespace formatting
    """
    cleaned = raw_response.strip()

    # Remove markdown code block wrappers if present
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    cleaned = cleaned.strip()

    # If there's extra text, try to extract the JSON block
    if not cleaned.startswith("{"):
        start = cleaned.find("{")
        if start != -1:
            cleaned = cleaned[start:]

    if not cleaned.endswith("}"):
        end = cleaned.rfind("}")
        if end != -1:
            cleaned = cleaned[: end + 1]

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse LLM response as JSON: {e}")
