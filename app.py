import uvicorn
from fastapi import FastAPI
from env import EmailTriageEnv

app = FastAPI()
env = EmailTriageEnv()

@app.get("/")
def home():
    return {"status": "OpenEnv Email Triage is Running"}

@app.post("/step")
def step(action: dict):
    # This connects the OpenEnv logic to the web
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)