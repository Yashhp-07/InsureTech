from fastapi import FastAPI

from app.modules.auth.routes import router as auth_router

app = FastAPI(title="InsureTech API", version="0.1.0")

app.include_router(auth_router)

