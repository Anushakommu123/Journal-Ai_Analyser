<<<<<<< HEAD
# Journal-Ai_Analyser
=======
# Journal AI Analyser

AI-powered journal entry analyser that extracts skills developed, emotional tone, hashtags, and an encouragement message from your journal entries.

## System Flow

```
User writes journal entry
        |
  Frontend / API request
        |
   FastAPI Backend
        |
 Journal Analyser Service
        |
 Prompt Template + User Journal
        |
   OpenAI LLM API
        |
 LLM generates structured JSON
        |
 API returns analysis to frontend
```

## Project Structure

```
app/
|- main.py                  # FastAPI entry point
|- config.py                # API keys and settings
|- models/
|  |- journal_model.py      # Request/response schemas
|- services/
|  |- journal_services.py   # LLM logic
|- prompts/
|  |- journal_prompt.py     # Prompt template
|- utils/
|  |- parser.py             # JSON parsing helpers
requirements.txt
README.md
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Test the API at `http://127.0.0.1:8000/docs`
>>>>>>> 59b4bd8 (Intial Commit)
