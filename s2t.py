import time
import os
import psutil
import requests
import pyperclip
import speech_recognition as sr

# Diagnostics: Measuring system resource utilization
def resource_utilization():
    print(f"CPU usage: {psutil.cpu_percent()}%")
    print(f"Memory usage: {psutil.virtual_memory().percent}%")

# Diagnostics: Measuring network latency to Google API
def check_network_latency():
    start_time = time.time()
    try:
        response = requests.get("https://www.google.com", timeout=5)
        latency = (time.time() - start_time) * 1000  # Convert to milliseconds
        print(f"Network latency to Google: {latency:.2f} ms")
    except requests.RequestException:
        print("Could not measure latency to Google. Check your internet connection.")

# Initialize recognizer and microphone
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Diagnostics: Measuring time to initialize microphone
start_time = time.time()
with mic as source:
    recognizer.adjust_for_ambient_noise(source, duration=5)  # Adjusting for ambient noise
mic_init_time = (time.time() - start_time) * 1000
print(f"Microphone initialization time: {mic_init_time:.2f} ms")

# Diagnostics: Checking ALSA Configuration
if os.path.exists("/usr/share/alsa/alsa.conf"):
    print("ALSA configuration exists!")
else:
    print("ALSA configuration does not exist or is not in the expected location.")

resource_utilization()
check_network_latency()

print("Please start speaking. Press Enter to stop recording...")
with mic as source:
    audio_data = recognizer.listen(source)
    print("Recognizing...")

    # Diagnostics: Measuring time to establish a connection and get response from Google API
    start_time = time.time()
    try:
        text = recognizer.recognize_google(audio_data)
        api_response_time = (time.time() - start_time) * 1000
        print(f"Time to get response from Google API: {api_response_time:.2f} ms")
        print(f"You said: {text}")
        
        # Copy to clipboard
        pyperclip.copy(text)
        print("Text has been copied to clipboard!")

    except sr.UnknownValueError:
        print("Sorry, I did not catch that.")
    except sr.RequestError:
        print("API unavailable. Check your internet connection.")
