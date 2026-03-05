import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000   # Most APIs prefer 16kHz
seconds = 7

print("Recording... Speak now.")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("input.wav", fs, recording)
print("Saved as input.wav")