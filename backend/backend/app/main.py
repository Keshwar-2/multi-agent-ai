from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import orchestrate

app = FastAPI()

class TaskRequest(BaseModel):
    goal: str
    options: dict = {}

@app.post("/submit")
async def submit_task(req: TaskRequest):
    job_id = await orchestrate(req.goal, req.options)
    return {"job_id": job_id}
