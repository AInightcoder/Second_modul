import sounddevice
from scipy.io.wavfile import write


fps=44100
duration=10

print("Recording yor voice...")
recorder=sounddevice.rec(int(fps*duration), samplerate=fps, channels=2)
sounddevice.wait()
print("Finsihed !")

write("output.wav",fps,recorder)