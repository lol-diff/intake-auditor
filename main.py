from fastapi import FastAPI
from src.auth import router as auth_router
from src.auditor import router as auditor_router

app = FastAPI(title="Clio Auditor API")

app.include_router(auth_router, prefix="/auth")
app.include_router(auditor_router, prefix="/audit")

@app.get("/")
def health_check():
    return {"status": "online"}