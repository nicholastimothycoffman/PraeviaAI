from fastapi import FastAPI
from app.routes import notify

app = FastAPI(
	title="PraeviaAI",
	description="An AI-powered assistant for monitoring and notifying about GenAI trends.",
	version="0.1.0"
)

# Include notification routes
app.include_router(notify.router, prefix="/notify", tags=["Notification"])

@app.get("/")
def read_root():
	return {"message": "Welcome to PraeviaAI - your GenAI news assistant"}
