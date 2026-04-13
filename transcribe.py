import whisper
import time
import os

def load_model(model_size="base"):
    """Load Whisper model. Use 'base' for speed, 'small' for better accuracy."""
    print(f"Loading Whisper {model_size} model...")
    model = whisper.load_model(model_size)
    print("Model loaded!")
    return model

def transcribe_audio(model, file_path):
    """
    Transcribe an audio file and return text, language, and time taken.
    Returns a dict with: text, language, duration_seconds
    """
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}
    
    start_time = time.time()
    
    result = model.transcribe(file_path)
    
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    
    return {
        "text": result["text"].strip(),
        "language": result["language"],
        "time_taken_seconds": time_taken
    }


if __name__ == "__main__":
    model = load_model("base")
    
    print("\nWhisper model loaded successfully!")
    print("Now run: streamlit run app.py")