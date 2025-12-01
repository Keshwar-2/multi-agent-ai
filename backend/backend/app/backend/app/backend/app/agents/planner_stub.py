def plan_goal(goal: str, options: dict):
    # Very simple placeholder plan (replace with LLM call later)
    return [
        {"id": "t1", "role": "researcher", "description": f"Gather facts about: {goal}"},
        {"id": "t2", "role": "writer", "description": f"Write a draft for: {goal}"},
        {"id": "t3", "role": "fact_checker", "description": "Verify facts and citations"}
    ]
