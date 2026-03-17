from pydantic import BaseModel, Field
from datetime import datetime


class JournalEntryRequest(BaseModel):
    journal_entry: str


class DevelopedSkills(BaseModel):
    communication_skills: list[str]
    behaviour_skills: list[str]
    creativity_skills: list[str]


class JournalAnalysisResponse(BaseModel):
    developed_skills: DevelopedSkills
    emotional_tone: str
    hashtags: list[str]
    popup_message: str


class JournalRecord(BaseModel):
    id: str = Field(alias="_id", default=None)
    journal_entry: str
    analysis: JournalAnalysisResponse
    created_at: datetime

    model_config = {"populate_by_name": True}
