from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

response = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",       # built-in human-like voice
    input="Hello world!"
)

with open("tts_output.mp3", "wb") as f:
    f.write(response)