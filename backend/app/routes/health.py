from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["health"])

@router.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Human vs AI Assessment API is running"}
