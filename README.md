# AudioRecorder
This is a simple Audio Recorder Application developed with python,tkinter

## Description

This application allows users to record audio, save it as a WAV file, and play back the recorded audio. The application is built using Python and utilizes libraries such as sounddevice, soundfile, pygame, and tkinter for functionality and user interface.

## Features
- **Record Audio:** Start and stop recording audio.
- **Save Recording:** Save the recorded audio as a WAV file.
- **Play Audio:** Open a separate window to play the recorded audio with controls for play, pause, and resume.
  
## Requirements

Ensure you have the following Python libraries installed:

- `sounddevice`
- `soundfile`
- `numpy`
- `pygame`
- `tkinter`

You can install the required libraries using pip:

```bash
pip install sounddevice soundfile numpy pygame```
```

Note: tkinter is included with Python standard library, so you typically don't need to install it separately.

## How to Run
Clone the Repository:

```bash
git clone https://github.com/your-username/voice-recorder.git
cd voice-recorder
```

Run the Application:

```bash
python voice_recorder.py
```
Make sure you are in the directory containing voice_recorder.py or provide the full path to the script.

## Usage
1. Start Recording:

- Click the "Start Recording" button to begin recording audio.
- A label will indicate that recording is in progress.
- 
2. Stop Recording:

- Click the "Stop Recording" button to stop the recording.
- Enter a name for the file in the dialog that appears, and the recording will be saved as a WAV file in the recordings folder.

3. Open Audio Player:

- Click the "Open Audio Player" button to open a new window where you can play, pause, and resume the audio playback.
- Use the progress bar to view the playback status.

## Folder Structure
- voice_recorder.py - Main Python script for the voice recorder application.
- recordings/ - Folder where the recorded audio files are saved.

## Known Issues
- Ensure the recordings folder exists in the same directory as the script. If not, you may need to create it manually.
