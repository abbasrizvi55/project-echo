from fastapi import FastAPI

app = FastAPI(
    title="Project Echo API",
    description="AI Sales Employee Backend",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {
        "project": "Project Echo",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }