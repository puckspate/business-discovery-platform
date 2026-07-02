from fastapi import FastAPI

app = FastAPI(
    title="Business Discovery Platform",
    version="0.1.0",
    description="AI Powered Business Discovery Platform"
)


@app.get("/")
def root():
    return {
        "application": "Business Discovery Platform",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }