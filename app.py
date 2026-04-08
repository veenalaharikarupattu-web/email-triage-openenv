from fastapi import FastAPI
import uvicorn
from env import EmailTriageEnv

app = FastAPI()
env = EmailTriageEnv()

@app.get("/")
def home():
    return {"status": "Running", "info": "Scaler X Meta Round 1"}

@app.post("/step")
def step(action: dict):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
