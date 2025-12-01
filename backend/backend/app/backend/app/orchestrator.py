import uuid
from app.agents.planner_stub import plan_goal

async def orchestrate(goal: str, options: dict):
    job_id = str(uuid.uuid4())
    plan = plan_goal(goal, options)
    # For MVP we just print plan; later we'll persist & schedule tasks
    print(f"Job {job_id} plan: {plan}")
    return job_id
