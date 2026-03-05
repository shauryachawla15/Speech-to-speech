from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key="sk_72033a1df852e94c67692aabbd6be9a2ebb66a4744a49e5f"
)

# Convert speech-to-speech (returns a generator stream)
audio_stream = client.speech_to_speech.convert(
    voice_id="jUjRbhZWoMK4aDciW36V",
    audio=open("input.wav", "rb"),
)

# Save properly
with open("output.wav", "wb") as f:
    for chunk in audio_stream:
        if chunk:
            f.write(chunk)

print(" Done! Saved as output.wav")