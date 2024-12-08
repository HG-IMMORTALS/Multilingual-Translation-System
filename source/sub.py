import os
import time
import pygame
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator

# Initialize translator and mixer
translator = Translator()
pygame.mixer.init()

# Map language names to codes
language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_language_code(language_name):
    """Retrieve the language code for a given language name."""
    return language_mapping.get(language_name, language_name)

def translator_function(spoken_text, from_language, to_language):
    """Translate text from one language to another."""
    try:
        translated = translator.translate(spoken_text, src=from_language, dest=to_language)
        return translated.text  # Return the translated text only
    except Exception as e:
        return f"Translation Error: {e}"

def text_to_voice(text_data, to_language, voice_speed):
    """Convert translated text to voice output."""
    try:
        if not text_data.strip():  # Handle empty strings
            raise ValueError("Text data is empty and cannot be converted to speech.")
        
        myobj = gTTS(text=text_data.strip(), lang=to_language, slow=(voice_speed < 1.0))
        myobj.save("cache_file.mp3")
        pygame.mixer.Sound("cache_file.mp3").play()
        time.sleep(2)  # Wait for audio playback
        os.remove("cache_file.mp3")
    except Exception as e:
        st.error(f"Audio Playback Error: {e}")

def generate_subtitle_file(history):
    """Generate subtitles in .srt format."""
    srt_content = ""
    for idx, item in enumerate(history):
        start_time = item['start_time']
        end_time = item['end_time']
        spoken = item['spoken']
        translated = item['translated']
        
        srt_content += f"{idx + 1}\n"
        srt_content += f"{format_time(start_time)} --> {format_time(end_time)}\n"
        srt_content += f"{translated}\n\n"
    
    return srt_content

def format_time(seconds):
    """Convert seconds to SRT format time (HH:MM:SS,MMM)."""
    millis = int((seconds - int(seconds)) * 1000)
    seconds = int(seconds)
    minutes = seconds // 60
    hours = minutes // 60
    seconds = seconds % 60
    minutes = minutes % 60
    
    return f"{hours:02}:{minutes:02}:{seconds:02},{millis:03}"

def main_process(output_placeholder, from_language, to_language, voice_speed, listening_timeout):
    """Main processing loop for listening, translating, and speaking."""
    rec = sr.Recognizer()
    start_time = time.time()  # Track the start time of the session
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source, duration=1)
        while st.session_state.is_running:
            try:
                output_placeholder.info("Listening...")
                audio = rec.listen(source, timeout=listening_timeout)
                
                # Recognize speech
                spoken_text = rec.recognize_google(audio, language=from_language)
                output_placeholder.success(f"You said: {spoken_text}")

                # Translate spoken text
                translated_text = translator_function(spoken_text, from_language, to_language)
                if "Error" in translated_text:
                    output_placeholder.error(translated_text)
                    continue

                output_placeholder.success(f"Translated: {translated_text}")

                # Store translation in history with timestamps
                end_time = time.time()
                st.session_state['translation_history'].append({
                    "spoken": spoken_text,
                    "translated": translated_text,
                    "start_time": start_time,
                    "end_time": end_time
                })
                start_time = end_time  # Update the start time for the next chunk

                # Play translated text
                text_to_voice(translated_text, to_language, voice_speed)
            except sr.WaitTimeoutError:
                output_placeholder.warning("No speech detected. Please try again.")
            except sr.UnknownValueError:
                output_placeholder.error("Could not understand the audio. Please try again.")
            except Exception as e:
                output_placeholder.error(f"Error: {e}")

# Streamlit UI Layout
st.set_page_config(page_title="Multilingual Translator", layout="wide")
st.title("Multilingual Real-Time Translation")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    from_language_name = st.selectbox("Source Language (or Auto-Detect):", ["Auto-Detect"] + list(LANGUAGES.values()))
    to_language_name = st.selectbox("Target Language:", list(LANGUAGES.values()))
    voice_speed = st.slider("Voice Speed:", min_value=0.5, max_value=1.5, value=1.0)
    listening_timeout = st.slider("Listening Timeout (seconds):", min_value=5, max_value=30, value=10)

# Map language names to codes
from_language = "auto" if from_language_name == "Auto-Detect" else get_language_code(from_language_name)
to_language = get_language_code(to_language_name)

# Initialize session state for translation history
if 'translation_history' not in st.session_state:
    st.session_state['translation_history'] = []

if 'is_running' not in st.session_state:
    st.session_state.is_running = False

# Main interface
output_placeholder = st.empty()
col1, col2 = st.columns(2)

with col1:
    if st.button("Start Listening"):
        st.session_state.is_running = True
        main_process(output_placeholder, from_language, to_language, voice_speed, listening_timeout)

with col2:
    if st.button("Stop Listening"):
        st.session_state.is_running = False
        st.write("Translation stopped.")

# Display translation history
st.subheader("Translation History")
for item in st.session_state['translation_history']:
    st.write(f"**You said:** {item['spoken']}")
    st.write(f"**Translated:** {item['translated']}")

# Download translation history
if st.session_state['translation_history']:
    history_text = "\n\n".join([f"You said: {item['spoken']}\nTranslated: {item['translated']}" 
                                for item in st.session_state['translation_history']])
    st.download_button("Download Translation History", data=history_text, file_name="translation_history.txt", mime="text/plain")

# Generate and download subtitles
if st.session_state['translation_history']:
    srt_content = generate_subtitle_file(st.session_state['translation_history'])
    st.download_button("Download Subtitles", data=srt_content, file_name="subtitles.srt", mime="text/plain")
