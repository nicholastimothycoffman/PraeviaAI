# Praevia.AI

Your AI-powered assistant for staying ahead in Generative AI, NLP, and emerging AI technologies.


## What It Does

Praevia.AI continuously monitors the latest developments in AI across blogs, papers, release notes, and more. It summarizes relevant updates using LLMs, filters by importance, and proactively notifies you with digestible insights.


## Powered By

 • Python 3.11+
 • FastAPI
 • LangChain
 • OpenAI API
 • FAISS / ChromaDB
 • RSS / Web Scraping
 • Telegram or Slack API


## Features

 • Daily digest of GenAI / NLP / RAG news
 • Smart summarization and topic classification
 • Vector-based semantic search of article archive
 • Notifications via Slack, Telegram, or email
 • Chat interface to ask: "What's new in LangChain?" etc


## Getting Started

git clone https://github.com/nicholastimothycoffman/PraeviaAI.git
cd PraeviaAI
pip install -r requirements.txt


## API Endpoints

 • GET /notify/test 	- test notification
 • POST /update		- triggers scraping + summarization

