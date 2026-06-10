from fastapi import FastAPI

app = FastAPI(title="InsureTech API", version="0.1.0")


@app.get("/")
async def root():
    return {"message": "InsureTech API is running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
