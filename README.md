# s2t

This application utilizes the Google Speech Recognition API to convert spoken words into text.

## Prerequisites

- Python 3.x
- Libraries: `speech_recognition`, `psutil`, `requests`, `pyperclip`

To install the required libraries, use the following:
```bash
pip install speech_recognition psutil requests
```

## Features

1. **Quick Recognition**: Transcribes voice data into text using the powerful Google API.
2. **Diagnostics**: Provides insights into:
   - Microphone initialization time
   - Connection to Google API time
   - ALSA Configuration status
   - System resource utilization (CPU and Memory usage)
   - Network latency to Google
3. **Save to clipboard**: Use this application to simplify your workflows. Paste wherever the content is needed.
   
## Usage

1. Run the application:
```
python voice_recognition.py
```

2. Start speaking when prompted. The program will transcribe your speech, copy it to clipboard and display it along with diagnostic metrics.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
