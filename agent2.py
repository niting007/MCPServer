import requests
import time

AGENT_ID = "agent2"
SERVER = "http://127.0.0.1:8000"

# Register agent
requests.post(f"{SERVER}/register", json={"agent_id": AGENT_ID})

while True:
    # Ask for task
    response = requests.get(f"{SERVER}/get_task/{AGENT_ID}").json()
    task = response.get("task")
    if task is None:
        print("No task. Sleeping...")
        time.sleep(3)
        continue

    print(f"Received task: {task}")
    # Simulate doing work
    if "hello" in task.lower():
        result = "Hello from Agent 1!"
    elif "add" in task.lower():
        result = "Result is 5"
    else:
        result = "Unknown task"

    # Send result
    requests.post(f"{SERVER}/submit_result", json={"agent_id": AGENT_ID, "result": result})
    time.sleep(1)
