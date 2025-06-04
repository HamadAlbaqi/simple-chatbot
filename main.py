import requests
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/api/messages")
async def messages(request: Request):
    data = await request.json()
    print("Incoming:", data)

    service_url = data["serviceUrl"]
    conversation_id = data["conversation"]["id"]
    reply_to_url = f"{service_url}v3/conversations/{conversation_id}/activities"

    reply_activity = {
        "type": "message",
        "text": f"You said: {data.get('text')} - Hamad is the best!"
    }

    # For now — NO auth → will likely need bearer token for production
    response = requests.post(reply_to_url, json=reply_activity)
    print("Reply response:", response.status_code, response.text)

    return {}
