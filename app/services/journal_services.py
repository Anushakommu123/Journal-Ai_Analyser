from datetime import datetime
from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL, TEMPERATURE, MAX_TOKENS
from app.prompts.journal_prompt import SYSTEM_PROMPT, USER_PROMPT
from app.utils.parser import parse_llm_response
from app.database import journal_collection


client = OpenAI(api_key=OPENAI_API_KEY)


def analyze_journal(journal_entry: str) -> dict:
    """Send journal entry to OpenAI and return structured analysis."""
    user_message = USER_PROMPT.format(journal_entry=journal_entry)

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )

    raw_content = response.choices[0].message.content
    return parse_llm_response(raw_content)


async def save_journal(journal_entry: str, analysis: dict) -> str:
    """Save journal entry and its analysis to MongoDB."""
    document = {
        "journal_entry": journal_entry,
        "analysis": analysis,
        "created_at": datetime.utcnow(),
    }
    result = await journal_collection.insert_one(document)
    return str(result.inserted_id)


async def get_all_journals() -> list[dict]:
    """Fetch all saved journal records from MongoDB."""
    journals = []
    cursor = journal_collection.find().sort("created_at", -1)
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        journals.append(doc)
    return journals


async def get_journal_by_id(journal_id: str) -> dict | None:
    """Fetch a single journal record by ID."""
    from bson import ObjectId
    doc = await journal_collection.find_one({"_id": ObjectId(journal_id)})
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc
