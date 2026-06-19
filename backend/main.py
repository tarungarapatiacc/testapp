from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import routers
from app.routes import questions, assessment, health
from app.models.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting Human vs AI Assessment Platform")
    print(f"📡 API Documentation available at: http://localhost:{os.getenv('PORT', 8000)}/docs")
    yield
    # Shutdown
    print("🛑 Shutting down application")

app = FastAPI(
    title="Human vs AI Thinking Assessment",
    description="Platform to assess out-of-the-box thinking and compare human reasoning with algorithmic approaches",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router)
app.include_router(questions.router)
app.include_router(assessment.router)

@app.get("/")
def read_root():
    return {
        "message": "Human vs AI Thinking Assessment Platform",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True
    )
