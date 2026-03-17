from fastapi import FastAPI, HTTPException
from app.models.journal_model import JournalEntryRequest, JournalAnalysisResponse
from app.services.journal_services import analyze_journal, save_journal, get_all_journals, get_journal_by_id

app = FastAPI(title="Journal AI Analyser")


@app.post("/analyze-journal", response_model=JournalAnalysisResponse)
async def analyze(request: JournalEntryRequest):
    try:
        result = analyze_journal(request.journal_entry)
        await save_journal(request.journal_entry, result)
        return JournalAnalysisResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/journals")
async def list_journals():
    journals = await get_all_journals()
    return journals


@app.get("/journals/{journal_id}")
async def get_journal(journal_id: str):
    journal = await get_journal_by_id(journal_id)
    if not journal:
        raise HTTPException(status_code=404, detail="Journal not found")
    return journal
