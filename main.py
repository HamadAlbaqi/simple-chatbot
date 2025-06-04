from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/api/messages")
async def messages(request: Request):
    data = await request.json()
    user_input = data.get("text", "")

    answer = "Hamad is the best"
    full_answer = user_input + answer

    return {
        "type": "message",
        "text": full_answer
    }

# python -m uvicorn main:app --port 3978 --host localhost
# .\cloudflared.exe tunnel --url http://localhost:3978 --protocol h2mux