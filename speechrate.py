import pyaudio
import time
from pocketsphinx import LiveSpeech

CHUNK_SIZE = 1024  # Number of audio frames per buffer
SAMPLE_RATE = 16000  # Sampling rate of the audio stream

# Create audio stream and start recording
audio = pyaudio.PyAudio()

# Initialize audio stream parameters
stream = audio.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=SAMPLE_RATE,
    input=True,
    frames_per_buffer=CHUNK_SIZE
)

# Start the audio stream
stream.start_stream()

print("Recording Started, please speak!")

# Initialize speech recognizer
speech = LiveSpeech()

# Variables for speech rate calculation
start_time = time.time()
word_count = 0

# Calculate speech rate in real-time
for phrase in speech:
    word_count += len(str(phrase).split())

    elapsed_time = time.time() - start_time
    if elapsed_time > 10:
        speech_rate = word_count / (elapsed_time / 60)
        print("Speech Rate (WPM):", speech_rate)
        start_time = time.time()
        word_count = 0

# Stop and close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()
