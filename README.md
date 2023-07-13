# speechrate-calculation

INTRODUCTION:
The Python code allows measuring the speech rate of the streaming microphone input in real time. This documentation provides an overview of the basic code structure and usage.
CODE STRUCTURE:
The TTS code typically consists of the following steps:
1. Required Libraries
•	pyaudio: Used for audio stream handling.
•	pocketsphinx: Used for speech recognition.
2. Constants
•	CHUNK_SIZE: Number of audio frames per buffer.
•	SAMPLE_RATE: Sampling rate of the audio stream.
 3. Recording and Speech Recognition Setup
1.	Import the necessary libraries: pyaudio, time, and pocketsphinx.
2.	Initialize the pyaudio module and create an instance of the PyAudio class.
3.	Set up the audio stream with the desired parameters using the open() method of the PyAudio instance.
4.	Start the audio stream by calling the start_stream() method.
SPEECH RATE CALCULATION:
1.	Create an instance of the LiveSpeech class from the pocketsphinx library.
2.	Initialize variables for tracking the speech rate calculation: start_time (to measure the elapsed time) and word_count (to count the number of recognized words).
3.	Enter a loop to continuously process the recognized speech:
4.	The LiveSpeech instance iterates over the recognized phrases.
5.	Count the number of words in each recognized phrase and update the word count variable.
6.	Calculate the elapsed time since the start of the loop.
7.	If the elapsed time exceeds 10 seconds:
i.	Calculate the speech rate by dividing the word count by the elapsed time (in minutes).
ii.	Print the calculated speech rate in words per minute (WPM).
iii.	Reset the start_time to the current time.
iv.	Reset the word_count to zero.
v.	The loop continues indefinitely until the audio stream is stopped manually.
Now, if you want to change the Usage Example:
Here’s an example of using the TTS code to convert text to speech:

