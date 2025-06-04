import requests
from fastapi import FastAPI, Request

# Bot credentials (put in environment variables for security)
MICROSOFT_APP_ID = "f66e0608-a899-4060-a7e4-2c1b2de5a582"
MICROSOFT_APP_PASSWORD = "tC98Q~Gidg~-Ee4Np2iEiZg4m~nVkSnkESP4pcYW"

app = FastAPI()

@app.post("/api/messages")
async def messages(request: Request):
    data = await request.json()
    print("Incoming:", data)

    # Get serviceUrl and conversationId
    service_url = data["serviceUrl"]
    conversation_id = data["conversation"]["id"]

    # Compose reply message
    reply_text = f"You said: {data.get('text')} - Hamad is the best!"
    reply_activity = {
        "type": "message",
        "text": reply_text
    }

    # STEP 1 — Acquire access token
    token_url = "https://login.microsoftonline.com/botframework.com/oauth2/v2.0/token"
    token_data = {
        "grant_type": "client_credentials",
        "client_id": MICROSOFT_APP_ID,
        "client_secret": MICROSOFT_APP_PASSWORD,
        "scope": "https://api.botframework.com/.default"
    }

    token_response = requests.post(token_url, data=token_data)
    token_response.raise_for_status()  # Raise error if failed
    access_token = token_response.json()["access_token"]
    print("Access token acquired.")

    # STEP 2 — Post reply to conversation
    reply_url = f"{service_url}v3/conversations/{conversation_id}/activities"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    post_response = requests.post(reply_url, headers=headers, json=reply_activity)
    print("Reply POST response:", post_response.status_code, post_response.text)

    return {}

# python -m uvicorn main:app --port 3978 --host localhost
# .\cloudflared.exe tunnel --url http://localhost:3978 --protocol h2mux
