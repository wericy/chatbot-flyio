from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model.chatbot import CustomizedTransformer
import uvicorn

app = FastAPI()
model = CustomizedTransformer(model_dir="app/model")

class Query(BaseModel):
    prompt: str

@app.post("/v1/chat/completions")
def chat_completion(query: Query):
    try:
        response = model.predict(query.prompt)
        return {
            "id": "chatcmpl-mockid",
            "object": "chat.completion",
            "choices": [{
                "message": {
                    "role": "assistant",
                    "content": response
                },
                "finish_reason": "stop",
                "index": 0
            }]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Local testing
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
