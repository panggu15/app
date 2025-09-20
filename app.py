from fastapi import FastAPI, Request
from pydantic import BaseModel


app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: Message):
    user_input = request.message
    
    gpt_response = user_input
    
    return {"response": gpt_response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
