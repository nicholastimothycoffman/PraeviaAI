# TODO – Praevia.AI

A structured development checklist to build a full-stack AI-powered platform for analyzing and predicting market trends in computer science-related companies.

## REMINDER: UPDATE STRUCTURE SNAPSHOT

With each addition, removal, or reorganization of files/folders, regenerate `project_structure.md` with:

```bash
./update_structure.sh

---

- [ ] Initialize Git repo and set `main` as default branch
- [ ] Add `.gitignore` and `README.md`
- [ ] Create initial folder structure
- [ ] Set up Python virtual environment
- [ ] Install required packages (`requirements.txt`)
- [ ] Push clean project baseline to GitHub
- [ ] Implement `fetch_data.py` to download historical stock prices (via `yfinance`)
- [ ] Create `transform.py` to clean and standardize time series data
- [ ] Tag companies with tech themes (AI, Quantum, Cloud, etc.)
- [ ] Save processed data to `/data/processed/`
- [ ] Unit test data ingestion and transformation logic
- [ ] Design LSTM or GRU model to predict stock prices
- [ ] Build training/validation script in `lstm_model.py`
- [ ] Evaluate model using RMSE/MAE in `evaluate.py`
- [ ] Save models and predictions to `/models/` and `/data/processed/`
- [ ] Compare predictions with actuals over time
- [ ] Track model accuracy using a rolling error window
- [ ] Implement `generate_insights.py` to translate model output into human-readable insights
- [ ] Use rule-based logic or OpenAI API for narrative generation
- [ ] Example insight: “Our model overestimated NVDA due to post-earnings volatility.”
- [ ] Set up FastAPI in `/src/api/main.py`
- [ ] Implement endpoints:
  - `/predict/{ticker}`
  - `/insights/{ticker}`
  - `/metrics`
- [ ] Serve processed data and model outputs via API
- [ ] Document API with Swagger UI (via FastAPI auto-doc)
- [ ] Scaffold frontend in `/frontend/` with React
- [ ] Build dashboard components:
  - Stock chart (actual vs. predicted)
  - Accuracy tracker
  - Insight display
- [ ] Connect frontend to FastAPI backend
- [ ] Write unit tests in `/tests/`
- [ ] Create CI workflow (e.g., GitHub Actions)
- [ ] Dockerize application
- [ ] Deploy API to Render, Railway, or AWS (optional)
- [ ] Add badges to `README.md` (build passing, coverage, etc.)
- [ ] Add animated GIF demo to `README.md`
- [ ] Add project write-up or blog post link
- [ ] Submit project to relevant forums (e.g., Dev.to, LinkedIn)
