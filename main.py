from fastapi import FastAPI, Request
from typing import Dict, Union, List

app = FastAPI()

AGENTS = {}
from typing import Dict

Task = Dict[str, Union[int, str]]
TASKS: List[Task] = [
    {"id": 1, "task": "Say hello"},
    {"id": 2, "task": "Add numbers: 2 + 3"},
    {"id": 3, "task": "Multiply 5 * 6"},
    {"id": 4, "task": "What's your name?"},
]

task_index = 0

@app.post("/register")
async def register_agent(request: Request):
    data = await request.json()
    agent_id = data.get("agent_id")
    AGENTS[agent_id] = {"status": "idle"}
    return {"message": f"Agent {agent_id} registered."}

@app.get("/get_task/{agent_id}")
def get_task(agent_id: str):
    global task_index
    if task_index < len(TASKS):
        task = TASKS[task_index]
        task_index += 1
        AGENTS[agent_id]["status"] = "working"
        return task
    else:
        return {"task": None}

@app.post("/submit_result")
async def submit_result(request: Request):
    data = await request.json()
    agent_id = data["agent_id"]
    result = data["result"]
    AGENTS[agent_id]["status"] = "idle"
    print(f"Agent {agent_id} completed task: {result}")
    return {"message": "Result received"}
