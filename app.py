import streamlit as st
import whisper
import tempfile
import os
import time

st.set_page_config(
    page_title="Multilingual Audio Transcriber",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ Multilingual Audio Transcription")
st.caption("Powered by OpenAI Whisper — supports Hindi, English, and 97 other languages")

# ── Load model (cached so it only loads once) ──────────────────────────────
@st.cache_resource
def load_model():
    with st.spinner("Loading Whisper model... (first time only, ~30 seconds)"):
        model = whisper.load_model("base")
    return model

model = load_model()
st.success("Model ready!", icon="✅")

st.divider()

# ── File Upload Section ────────────────────────────────────────────────────
st.subheader("Upload an audio file")
st.caption("Supported formats: mp3, wav, m4a, ogg, flac")

uploaded_file = st.file_uploader(
    label="Choose an audio file",
    type=["mp3", "wav", "m4a", "ogg", "flac"],
    label_visibility="collapsed"
)

if uploaded_file is not None:
    st.audio(uploaded_file, format=uploaded_file.type)

    if st.button("Transcribe", type="primary", use_container_width=True):
        
        # Save uploaded file to a temp location
        suffix = os.path.splitext(uploaded_file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        with st.spinner("Transcribing... please wait"):
            start = time.time()
            result = model.transcribe(tmp_path)
            elapsed = round(time.time() - start, 2)

        os.unlink(tmp_path)  # clean up temp file

        # ── Results ──────────────────────────────────────────────────────
        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Detected Language", result["language"].upper())
        with col2:
            st.metric("Time Taken", f"{elapsed}s")

        st.subheader("Transcript")
        transcript = result["text"].strip()
        st.text_area(
            label="Output",
            value=transcript,
            height=200,
            label_visibility="collapsed"
        )

        st.download_button(
            label="⬇️ Download transcript as .txt",
            data=transcript,
            file_name=f"{uploaded_file.name}_transcript.txt",
            mime="text/plain",
            use_container_width=True
        )

st.divider()

# ── Info expander ──────────────────────────────────────────────────────────
with st.expander("How does this work?"):
    st.markdown("""
    **OpenAI Whisper** is a speech recognition model trained on 680,000 hours of multilingual audio.

    **Pipeline:**
    1. Your audio file is converted into a **mel spectrogram** (a visual frequency map of sound over time)
    2. The **encoder** (transformer) processes this into embeddings
    3. The **decoder** generates the transcript token by token
    4. Language is auto-detected from the first few seconds of audio — no separate step needed

    **Models available:** `tiny` → `base` → `small` → `medium` → `large`  
    This app uses `base` — good speed on CPU, solid accuracy for clean audio.
    """)