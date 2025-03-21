praevia_ai/
│
├── app/                        # Main application logic
│   ├── __init__.py
│   ├── main.py                 # FastAPI app instance + routes
│   ├── routes/
│   │   ├── __init__.py
│   │   └── notify.py           # Endpoint to trigger/send notifications
│   ├── services/
│   │   ├── __init__.py
│   │   ├── fetch_sources.py    # Web scraping, RSS parsing
│   │   ├── summarizer.py       # LLM summarization logic
│   │   ├── classifier.py       # Importance tagging via GPT
│   │   ├── vector_store.py     # FAISS or ChromaDB interactions
│   │   └── notifier.py         # Telegram/Slack/email push logic
│   ├── agents/
│   │   ├── __init__.py
│   │   └── trend_agent.py      # LangChain agent logic (multi-tool chains)
│   └── models/
│       ├── __init__.py
│       └── content.py          # Pydantic models (e.g., Article, Summary)
│
├── data/                       # Saved content (raw, summarized, embeddings)
│   ├── raw_articles/
│   ├── summaries/
│   └── embeddings/
│
├── scripts/                    # Optional cronjobs / CLI tools
│   ├── cron_daily_update.py    # Scrapes → summarizes → stores → notifies
│   └── dev_test_runner.py
│
├── tests/                      # Pytest-compatible unit tests
│   ├── test_fetch_sources.py
│   └── test_summarizer.py
│
├── .env                        # Environment variables (API keys, secrets)
├── requirements.txt            # Package dependencies
├── README.md                   # Project overview, setup, usage
└── run.py                      # Entry point for development/debug

