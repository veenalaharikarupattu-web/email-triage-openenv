from fastapi import FastAPI
import uvicorn
from env import EmailTriageEnv

app = FastAPI()
env = EmailTriageEnv()

@app.get("/")
def home():
    return {"status": "Running", "info": "Scaler X Meta Round 1"}

# This fixes "openenv reset post failed"
@app.post("/reset")
def reset():
    observation = env.reset()
    return {"observation": observation}

@app.post("/step")
def step(action: dict):
    # This handles the action dictionary sent by the bot
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
