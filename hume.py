from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("HUME_API_KEY")

import requests

API_KEY = "YOUR_API_KEY"

headers = {
    "X-API-Key": API_KEY
}

files = {
    "file": open("input.wav", "rb")
}

data = {
    "target_voice": "VOICE_ID"  # replace with actual target voice
}

response = requests.post(
    "https://api.hume.ai/v0/voice/convert",
    headers=headers,
    files=files,
    data=data
)

if response.status_code == 200:
    with open("hume_output.wav", "wb") as f:
        f.write(response.content)
    print("Voice converted!")
else:
    print("Error:", response.text)