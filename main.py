from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/api/messages")
async def messages(request: Request):
    data = await request.json()
    print("Incoming:", data)

    # Extract user text
    user_text = data.get("text", "")
    reply_text = f"You said: {user_text} - Hamad is the best!"

    # Build reply
    reply = {
        "type": "message",
        "text": reply_text
    }

    print(reply)

    return JSONResponse(content=reply)

# python -m uvicorn main:app --port 3978 --host localhost
# .\cloudflared.exe tunnel --url http://localhost:3978 --protocol h2mux
