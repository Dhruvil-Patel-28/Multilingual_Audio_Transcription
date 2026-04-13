# Multilingual Audio Transcription

A Streamlit app for multilingual audio transcription using OpenAI Whisper.

## Overview

- `app.py` is the Streamlit application.
- `transcribe.py` contains helper functions for loading Whisper and transcribing audio.
- `requirements.txt` lists the Python dependencies.
- `.gitignore` excludes the local virtual environment and temporary/runtime files.

## Features

- Upload audio files in `mp3`, `wav`, `m4a`, `ogg`, or `flac` formats.
- Automatic language detection and transcription via Whisper.
- Transcript preview with download as `.txt`.
- Displays detected language and transcription time.

## Setup

1. Activate the local virtual environment:

   ```powershell
   .\boli\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```powershell
   streamlit run app.py
   ```

## Usage

- Open the app in your browser after Streamlit starts.
- Upload an audio file.
- Click `Transcribe` to start transcription.
- Download the transcript as a `.txt` file.

## Validation

- `app.py` and `transcribe.py` compile successfully with `python -m py_compile`.
- When using the local `boli` virtual environment, the required packages import correctly.

## Notes

- If the system Python environment does not have Whisper installed, use the local environment in `boli/`.
- The `.gitignore` file already excludes `boli/`, Python cache files, editor files, logs, and temporary audio files.

## File Structure

```text
app.py
transcribe.py
requirements.txt
README.md
.gitignore
boli/                # local virtual environment (ignored by git)
```
