from fastapi import APIRouter
from app.services.notifier import send_test_notification

router = APIRouter()

@router.get("/test")
async def test_notification():
	"""
	Test endpoint to simulate a notification being sent.
	"""
	result = send_test_notification()
	return {"status": "ok", "message": result}
