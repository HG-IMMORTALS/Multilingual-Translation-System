# original
# import os
# import time
# import pygame
# from gtts import gTTS
# import streamlit as st
# import speech_recognition as sr
# from googletrans import LANGUAGES, Translator

# isTranslateOn = False

# translator = Translator() # Initialize the translator module.
# pygame.mixer.init()  # Initialize the mixer module.

# # Create a mapping between language names and language codes
# language_mapping = {name: code for code, name in LANGUAGES.items()}

# def get_language_code(language_name):
#     return language_mapping.get(language_name, language_name)

# def translator_function(spoken_text, from_language, to_language):
#     return translator.translate(spoken_text, src='{}'.format(from_language), dest='{}'.format(to_language))

# def text_to_voice(text_data, to_language):
#     myobj = gTTS(text=text_data, lang='{}'.format(to_language), slow=False)
#     myobj.save("cache_file.mp3")
#     audio = pygame.mixer.Sound("cache_file.mp3")  # Load a sound.
#     audio.play()
#     os.remove("cache_file.mp3")

# def main_process(output_placeholder, from_language, to_language):
    
#     global isTranslateOn
    
#     while isTranslateOn:

#         rec = sr.Recognizer()
#         with sr.Microphone() as source:
#             output_placeholder.text("Listening...")
#             rec.pause_threshold = 1
#             audio = rec.listen(source, phrase_time_limit=10)
        
#         try:
#             output_placeholder.text("Processing...")
#             spoken_text = rec.recognize_google(audio, language='{}'.format(from_language))
            
#             output_placeholder.text("Translating...")
#             translated_text = translator_function(spoken_text, from_language, to_language)

#             text_to_voice(translated_text.text, to_language)
    
#         except Exception as e:
#             print(e)

# # UI layout
# st.title("Language Translator")

# # Dropdowns for selecting languages
# from_language_name = st.selectbox("Select Source Language:", list(LANGUAGES.values()))
# to_language_name = st.selectbox("Select Target Language:", list(LANGUAGES.values()))

# # Convert language names to language codes
# from_language = get_language_code(from_language_name)
# to_language = get_language_code(to_language_name)

# # Button to trigger translation
# start_button = st.button("Start")
# stop_button = st.button("Stop")

# # Check if "Start" button is clicked
# if start_button:
#     if not isTranslateOn:
#         isTranslateOn = True
#         output_placeholder = st.empty()
#         main_process(output_placeholder, from_language, to_language)

# # Check if "Stop" button is clicked
# if stop_button:
#     isTranslateOn = False

# for working 
# import os
# import time
# import pygame
# from gtts import gTTS
# import streamlit as st
# import speech_recognition as sr
# from googletrans import LANGUAGES, Translator

# # Global flag to manage translation state
# isTranslateOn = False

# # Initialize translator and mixer
# translator = Translator()
# pygame.mixer.init()

# # Map language names to codes
# language_mapping = {name: code for code, name in LANGUAGES.items()}

# def get_language_code(language_name):
#     """Retrieve the language code for a given language name."""
#     return language_mapping.get(language_name, language_name)

# def translator_function(spoken_text, from_language, to_language):
#     """Translate text from one language to another."""
#     try:
#         return translator.translate(spoken_text, src=from_language, dest=to_language)
#     except Exception as e:
#         print(f"Translation Error: {e}")
#         return None

# def text_to_voice(text_data, to_language):
#     """Convert translated text to voice output."""
#     try:
#         myobj = gTTS(text=text_data, lang=to_language, slow=False)
#         myobj.save("cache_file.mp3")
#         pygame.mixer.Sound("cache_file.mp3").play()
#         time.sleep(2)  # Wait for audio playback
#         os.remove("cache_file.mp3")
#     except Exception as e:
#         print(f"Audio Playback Error: {e}")

# def main_process(output_placeholder, from_language, to_language):
#     """Main processing loop for listening, translating, and speaking."""
#     global isTranslateOn
#     rec = sr.Recognizer()

#     while isTranslateOn:
#         with sr.Microphone() as source:
#             output_placeholder.text("Listening...")
#             rec.pause_threshold = 1
#             try:
#                 audio = rec.listen(source, phrase_time_limit=10)
#                 output_placeholder.text("Processing...")
#                 spoken_text = rec.recognize_google(audio, language=from_language)
#                 output_placeholder.text(f"You said: {spoken_text}")

#                 output_placeholder.text("Translating...")
#                 translated_text = translator_function(spoken_text, from_language, to_language)

#                 if translated_text:
#                     output_placeholder.text(f"Translated: {translated_text.text}")
#                     text_to_voice(translated_text.text, to_language)
#             except sr.UnknownValueError:
#                 output_placeholder.text("Could not understand the audio. Please try again.")
#             except Exception as e:
#                 output_placeholder.text(f"Error: {e}")
#                 print(e)

# # Streamlit UI Layout
# st.title("Multilinguistic  Translation System")

# # Dropdowns for language selection
# from_language_name = st.selectbox("Select Source Language:", list(LANGUAGES.values()))
# to_language_name = st.selectbox("Select Target Language:", list(LANGUAGES.values()))

# # Get language codes
# from_language = get_language_code(from_language_name)
# to_language = get_language_code(to_language_name)

# # Buttons to control the translator
# start_button = st.button("Start")
# stop_button = st.button("Stop")

# # Start translation process
# if start_button:
#     if not isTranslateOn:
#         isTranslateOn = True
#         output_placeholder = st.empty()
#         main_process(output_placeholder, from_language, to_language)

# # Stop translation process
# if stop_button:
#     isTranslateOn = False
#     st.write("Translation ended!! Thankyou.")


# after the upgrade 
# import os
# import time
# import pygame
# from gtts import gTTS
# import streamlit as st
# import speech_recognition as sr
# from googletrans import LANGUAGES, Translator

# # Global flag to manage translation state
# isTranslateOn = False

# # Initialize translator and mixer
# translator = Translator()
# pygame.mixer.init()

# # Map language names to codes
# language_mapping = {name: code for code, name in LANGUAGES.items()}

# def get_language_code(language_name):
#     """Retrieve the language code for a given language name."""
#     return language_mapping.get(language_name, language_name)

# def translator_function(spoken_text, from_language, to_language):
#     """Translate text from one language to another."""
#     try:
#         return translator.translate(spoken_text, src=from_language, dest=to_language)
#     except Exception as e:
#         print(f"Translation Error: {e}")
#         return None

# def detect_language(spoken_text):
#     """Detect the language of the spoken text."""
#     try:
#         detected = translator.detect(spoken_text)
#         return detected.lang
#     except Exception as e:
#         print(f"Language Detection Error: {e}")
#         return None

# def text_to_voice(text_data, to_language, voice_speed):
#     """Convert translated text to voice output."""
#     try:
#         myobj = gTTS(text=text_data, lang=to_language, slow=(voice_speed < 1.0))
#         myobj.save("cache_file.mp3")
#         pygame.mixer.Sound("cache_file.mp3").play()
#         time.sleep(2)  # Wait for audio playback
#         os.remove("cache_file.mp3")
#     except Exception as e:
#         print(f"Audio Playback Error: {e}")

# def main_process(output_placeholder, from_language, to_language, voice_speed):
#     """Main processing loop for listening, translating, and speaking."""
#     global isTranslateOn
#     rec = sr.Recognizer()

#     while isTranslateOn:
#         with sr.Microphone() as source:
#             output_placeholder.text("Listening...")
#             rec.pause_threshold = 1
#             try:
#                 audio = rec.listen(source, phrase_time_limit=10)
#                 output_placeholder.text("Processing...")
#                 spoken_text = rec.recognize_google(audio, language=from_language)
#                 output_placeholder.text(f"You said: {spoken_text}")

#                 # Language detection (if source language is set to auto-detect)
#                 detected_language = detect_language(spoken_text) if from_language == 'auto' else from_language
#                 output_placeholder.text(f"Detected Language: {LANGUAGES.get(detected_language, 'Unknown')}")

#                 output_placeholder.text("Translating...")
#                 translated_text = translator_function(spoken_text, detected_language, to_language)

#                 if translated_text:
#                     # Store spoken and translated text in session state
#                     st.session_state['translation_history'].append({
#                         "spoken": spoken_text,
#                         "translated": translated_text.text
#                     })

#                     output_placeholder.text(f"Translated: {translated_text.text}")
#                     text_to_voice(translated_text.text, to_language, voice_speed)
#             except sr.UnknownValueError:
#                 output_placeholder.text("Could not understand the audio. Please try again.")
#             except Exception as e:
#                 output_placeholder.text(f"Error: {e}")
#                 print(e)

# # Streamlit UI Layout
# st.title("Multilingual Translation System")

# # Dropdowns for language selection
# from_language_name = st.selectbox("Select Source Language (or Auto-Detect):", ["Auto-Detect"] + list(LANGUAGES.values()))
# to_language_name = st.selectbox("Select Target Language:", list(LANGUAGES.values()))

# # Get language codes
# from_language = "auto" if from_language_name == "Auto-Detect" else get_language_code(from_language_name)
# to_language = get_language_code(to_language_name)

# # Voice customization options
# voice_speed = st.slider("Select Voice Speed:", min_value=0.5, max_value=1.5, value=1.0)

# # Initialize session state for translation history
# if 'translation_history' not in st.session_state:
#     st.session_state['translation_history'] = []

# # Buttons to control the translator
# start_button = st.button("Start")
# stop_button = st.button("Stop")

# # Start translation process
# if start_button:
#     if not isTranslateOn:
#         isTranslateOn = True
#         output_placeholder = st.empty()
#         main_process(output_placeholder, from_language, to_language, voice_speed)

# # Stop translation process
# if stop_button:
#     isTranslateOn = False
#     st.write("Translation ended! Thank you.")

# # Display translation history
# st.subheader("Translation History")
# for item in st.session_state['translation_history']:
#     st.write(f"**You said:** {item['spoken']}")
#     st.write(f"**Translated:** {item['translated']}")

# # Download translation history as text file
# if st.session_state['translation_history']:
#     history_text = "\n\n".join([f"You said: {item['spoken']}\nTranslated: {item['translated']}" 
#                                 for item in st.session_state['translation_history']])
#     st.download_button(
#         label="Download Translation History",
#         data=history_text,
#         file_name="translation_history.txt",
#         mime="text/plain"
#     )

# # Generate and download subtitles
# if st.session_state['translation_history']:
#     subtitle_content = ""
#     for i, item in enumerate(st.session_state['translation_history']):
#         subtitle_content += f"{i+1}\n00:00:{i*5},000 --> 00:00:{(i+1)*5},000\n{item['spoken']} ({item['translated']})\n\n"
    
#     st.download_button(
#         label="Download Subtitles",
#         data=subtitle_content,
#         file_name="translation_subtitles.srt",
#         mime="text/plain"
#     )

# more upgrade 
# import os
# import time
# import pygame
# from gtts import gTTS
# import streamlit as st
# import speech_recognition as sr
# from googletrans import LANGUAGES, Translator

# # Global flag to manage translation state
# isTranslateOn = False

# # Initialize translator and mixer
# translator = Translator()
# pygame.mixer.init()

# # Map language names to codes
# language_mapping = {name: code for code, name in LANGUAGES.items()}

# def get_language_code(language_name):
#     """Retrieve the language code for a given language name."""
#     return language_mapping.get(language_name, language_name)

# def translator_function(spoken_text, from_language, to_language):
#     """Translate text from one language to another."""
#     try:
#         return translator.translate(spoken_text, src=from_language, dest=to_language)
#     except Exception as e:
#         print(f"Translation Error: {e}")
#         return None

# def detect_language(spoken_text):
#     """Detect the language of the spoken text."""
#     try:
#         detected = translator.detect(spoken_text)
#         return detected.lang
#     except Exception as e:
#         print(f"Language Detection Error: {e}")
#         return None

# def text_to_voice(text_data, to_language, voice_speed):
#     """Convert translated text to voice output."""
#     try:
#         myobj = gTTS(text=text_data, lang=to_language, slow=(voice_speed < 1.0))
#         myobj.save("cache_file.mp3")
#         pygame.mixer.Sound("cache_file.mp3").play()
#         time.sleep(2)  # Wait for audio playback
#         os.remove("cache_file.mp3")
#     except Exception as e:
#         print(f"Audio Playback Error: {e}")

# def main_process(output_placeholder, from_language, to_language, voice_speed):
#     """Main processing loop for listening, translating, and speaking."""
#     global isTranslateOn
#     rec = sr.Recognizer()

#     while isTranslateOn:
#         with sr.Microphone() as source:
#             output_placeholder.text("Listening...")
#             rec.pause_threshold = 1
#             try:
#                 audio = rec.listen(source, phrase_time_limit=10)
#                 output_placeholder.text("Processing...")
#                 spoken_text = rec.recognize_google(audio, language=from_language)
#                 output_placeholder.text(f"You said: {spoken_text}")

#                 # Language detection (if source language is set to auto-detect)
#                 detected_language = detect_language(spoken_text) if from_language == 'auto' else from_language
#                 output_placeholder.text(f"Detected Language: {LANGUAGES.get(detected_language, 'Unknown')}")

#                 output_placeholder.text("Translating...")
#                 translated_text = translator_function(spoken_text, detected_language, to_language)

#                 if translated_text:
#                     # Store spoken and translated text in session state
#                     st.session_state['translation_history'].append({
#                         "spoken": spoken_text,
#                         "translated": translated_text.text
#                     })

#                     output_placeholder.text(f"Translated: {translated_text.text}")
#                     text_to_voice(translated_text.text, to_language, voice_speed)
#             except sr.UnknownValueError:
#                 output_placeholder.text("Could not understand the audio. Please try again.")
#             except Exception as e:
#                 output_placeholder.text(f"Error: {e}")
#                 print(e)

# # Streamlit UI Layout
# st.title("Multilingual Translation System")

# # Dropdowns for language selection
# from_language_name = st.selectbox("Select Source Language (or Auto-Detect):", ["Auto-Detect"] + list(LANGUAGES.values()))
# to_language_name = st.selectbox("Select Target Language:", list(LANGUAGES.values()))

# # Get language codes
# from_language = "auto" if from_language_name == "Auto-Detect" else get_language_code(from_language_name)
# to_language = get_language_code(to_language_name)

# # Voice customization options
# voice_speed = st.slider("Select Voice Speed:", min_value=0.5, max_value=1.5, value=1.0)

# # Initialize session state for translation history
# if 'translation_history' not in st.session_state:
#     st.session_state['translation_history'] = []

# # Buttons to control the translator
# start_button = st.button("Start")
# stop_button = st.button("Stop")

# # Start translation process
# if start_button:
#     if not isTranslateOn:
#         isTranslateOn = True
#         output_placeholder = st.empty()
#         main_process(output_placeholder, from_language, to_language, voice_speed)

# # Stop translation process
# if stop_button:
#     isTranslateOn = False
#     st.write("Translation ended! Thank you.")

# # Display translation history
# st.subheader("Translation History")
# for item in st.session_state['translation_history']:
#     st.write(f"**You said:** {item['spoken']}")
#     st.write(f"**Translated:** {item['translated']}")

# # Download translation history as text file
# if st.session_state['translation_history']:
#     history_text = "\n\n".join([f"You said: {item['spoken']}\nTranslated: {item['translated']}" 
#                                 for item in st.session_state['translation_history']])
#     st.download_button(
#         label="Download Translation History",
#         data=history_text,
#         file_name="translation_history.txt",
#         mime="text/plain"
#     )

# # Generate and download subtitles
# if st.session_state['translation_history']:
#     subtitle_content = ""
#     for i, item in enumerate(st.session_state['translation_history']):
#         subtitle_content += f"{i+1}\n00:00:{i*5},000 --> 00:00:{(i+1)*5},000\n{item['spoken']} ({item['translated']})\n\n"
    
#     st.download_button(
#         label="Download Subtitles",
#         data=subtitle_content,
#         file_name="translation_subtitles.srt",
#         mime="text/plain"
#     )

# NOT APPROPRIATE 
# import os
# import time
# import pygame
# from gtts import gTTS
# import streamlit as st
# import speech_recognition as sr
# from googletrans import LANGUAGES, Translator

# # Initialize translator and mixer
# translator = Translator()
# pygame.mixer.init()

# # Map language names to codes
# language_mapping = {name: code for code, name in LANGUAGES.items()}

# def get_language_code(language_name):
#     """Retrieve the language code for a given language name."""
#     return language_mapping.get(language_name, language_name)

# def translator_function(spoken_text, from_language, to_language):
#     """Translate text from one language to another."""
#     try:
#         translated = translator.translate(spoken_text, src=from_language, dest=to_language)
#         return translated.text  # Return the translated text only
#     except Exception as e:
#         return f"Translation Error: {e}"

# def text_to_voice(text_data, to_language, voice_speed):
#     """Convert translated text to voice output."""
#     try:
#         if not text_data.strip():  # Handle empty strings
#             raise ValueError("Text data is empty and cannot be converted to speech.")
        
#         myobj = gTTS(text=text_data.strip(), lang=to_language, slow=(voice_speed < 1.0))
#         myobj.save("cache_file.mp3")
#         pygame.mixer.Sound("cache_file.mp3").play()
#         time.sleep(2)  # Wait for audio playback
#         os.remove("cache_file.mp3")
#     except Exception as e:
#         st.error(f"Audio Playback Error: {e}")

# def main_process(output_placeholder, from_language, to_language, voice_speed, listening_timeout):
#     """Main processing loop for listening, translating, and speaking."""
#     rec = sr.Recognizer()
#     with sr.Microphone() as source:
#         rec.adjust_for_ambient_noise(source, duration=1)
#         while st.session_state.is_running:
#             try:
#                 output_placeholder.info("Listening...")
#                 audio = rec.listen(source, timeout=listening_timeout)
                
#                 # Recognize speech
#                 spoken_text = rec.recognize_google(audio, language=from_language)
#                 output_placeholder.success(f"You said: {spoken_text}")

#                 # Translate spoken text
#                 translated_text = translator_function(spoken_text, from_language, to_language)
#                 if "Error" in translated_text:
#                     output_placeholder.error(translated_text)
#                     continue

#                 output_placeholder.success(f"Translated: {translated_text}")

#                 # Store translation in history
#                 st.session_state['translation_history'].append({
#                     "spoken": spoken_text,
#                     "translated": translated_text,
#                 })

#                 # Play translated text
#                 text_to_voice(translated_text, to_language, voice_speed)
#             except sr.WaitTimeoutError:
#                 output_placeholder.warning("No speech detected. Please try again.")
#             except sr.UnknownValueError:
#                 output_placeholder.error("Could not understand the audio. Please try again.")
#             except Exception as e:
#                 output_placeholder.error(f"Error: {e}")

# # Streamlit UI Layout
# st.set_page_config(page_title="Multilingual Translator", layout="wide")
# st.title("Multilingual Real-Time Translation")

# # Sidebar for settings
# with st.sidebar:
#     st.header("Settings")
#     from_language_name = st.selectbox("Source Language (or Auto-Detect):", ["Auto-Detect"] + list(LANGUAGES.values()))
#     to_language_name = st.selectbox("Target Language:", list(LANGUAGES.values()))
#     voice_speed = st.slider("Voice Speed:", min_value=0.5, max_value=1.5, value=1.0)
#     listening_timeout = st.slider("Listening Timeout (seconds):", min_value=5, max_value=30, value=10)

# # Map language names to codes
# from_language = "auto" if from_language_name == "Auto-Detect" else get_language_code(from_language_name)
# to_language = get_language_code(to_language_name)

# # Initialize session state for translation history
# if 'translation_history' not in st.session_state:
#     st.session_state['translation_history'] = []

# if 'is_running' not in st.session_state:
#     st.session_state.is_running = False

# # Main interface
# output_placeholder = st.empty()
# col1, col2 = st.columns(2)

# with col1:
#     if st.button("Start Listening"):
#         st.session_state.is_running = True
#         main_process(output_placeholder, from_language, to_language, voice_speed, listening_timeout)

# with col2:
#     if st.button("Stop Listening"):
#         st.session_state.is_running = False
#         st.write("Translation stopped.")

# # Display translation history
# st.subheader("Translation History")
# for item in st.session_state['translation_history']:
#     st.write(f"**You said:** {item['spoken']}")
#     st.write(f"**Translated:** {item['translated']}")

# # Download translation history
# if st.session_state['translation_history']:
#     history_text = "\n\n".join([f"You said: {item['spoken']}\nTranslated: {item['translated']}" 
#                                 for item in st.session_state['translation_history']])
#     st.download_button("Download Translation History", data=history_text, file_name="translation_history.txt", mime="text/plain")

# import os
# import time
# import pygame
# from gtts import gTTS
# import streamlit as st
# import speech_recognition as sr
# from googletrans import LANGUAGES, Translator

# # Initialize translator and mixer
# translator = Translator()
# pygame.mixer.init()

# # Map language names to codes
# language_mapping = {name: code for code, name in LANGUAGES.items()}

# def get_language_code(language_name):
#     """Retrieve the language code for a given language name."""
#     return language_mapping.get(language_name, language_name)

# def translator_function(spoken_text, from_language, to_language):
#     """Translate text from one language to another."""
#     try:
#         translated = translator.translate(spoken_text, src=from_language, dest=to_language)
#         return translated.text  # Return the translated text only
#     except Exception as e:
#         return f"Translation Error: {e}"

# def text_to_voice(text_data, to_language, voice_speed):
#     """Convert translated text to voice output."""
#     try:
#         if not text_data.strip():  # Handle empty strings
#             raise ValueError("Text data is empty and cannot be converted to speech.")
        
#         myobj = gTTS(text=text_data.strip(), lang=to_language, slow=(voice_speed < 1.0))
#         myobj.save("cache_file.mp3")
#         pygame.mixer.Sound("cache_file.mp3").play()
#         time.sleep(2)  # Wait for audio playback
#         os.remove("cache_file.mp3")
#     except Exception as e:
#         st.error(f"Audio Playback Error: {e}")

# def main_process(output_placeholder, from_language, to_language, voice_speed, listening_timeout):
#     """Main processing loop for listening, translating, and speaking."""
#     rec = sr.Recognizer()
#     with sr.Microphone() as source:
#         rec.adjust_for_ambient_noise(source, duration=1)
#         while st.session_state.is_running:
#             try:
#                 output_placeholder.info("Listening...")
#                 audio = rec.listen(source, timeout=listening_timeout)
                
#                 # Recognize speech
#                 spoken_text = rec.recognize_google(audio, language=from_language)
#                 output_placeholder.success(f"You said: {spoken_text}")

#                 # Translate spoken text
#                 translated_text = translator_function(spoken_text, from_language, to_language)
#                 if "Error" in translated_text:
#                     output_placeholder.error(translated_text)
#                     continue

#                 output_placeholder.success(f"Translated: {translated_text}")

#                 # Store translation in history
#                 st.session_state['translation_history'].append({
#                     "spoken": spoken_text,
#                     "translated": translated_text,
#                 })

#                 # Play translated text
#                 text_to_voice(translated_text, to_language, voice_speed)
#             except sr.WaitTimeoutError:
#                 output_placeholder.warning("No speech detected. Please try again.")
#             except sr.UnknownValueError:
#                 output_placeholder.error("Could not understand the audio. Please try again.")
#             except Exception as e:
#                 output_placeholder.error(f"Error: {e}")

# # Streamlit UI Layout
# st.set_page_config(page_title="Multilingual Translator", layout="wide")
# st.title("Multilingual Real-Time Translation")

# # Sidebar for settings
# with st.sidebar:
#     st.header("Settings")
#     from_language_name = st.selectbox("Source Language (or Auto-Detect):", ["Auto-Detect"] + list(LANGUAGES.values()))
#     to_language_name = st.selectbox("Target Language:", list(LANGUAGES.values()))
#     voice_speed = st.slider("Voice Speed:", min_value=0.5, max_value=1.5, value=1.0)
#     listening_timeout = st.slider("Listening Timeout (seconds):", min_value=5, max_value=30, value=10)

# # Map language names to codes
# from_language = "auto" if from_language_name == "Auto-Detect" else get_language_code(from_language_name)
# to_language = get_language_code(to_language_name)

# # Initialize session state for translation history
# if 'translation_history' not in st.session_state:
#     st.session_state['translation_history'] = []

# if 'is_running' not in st.session_state:
#     st.session_state.is_running = False

# # Main interface
# output_placeholder = st.empty()
# col1, col2 = st.columns(2)

# with col1:
#     if st.button("Start Listening"):
#         st.session_state.is_running = True
#         main_process(output_placeholder, from_language, to_language, voice_speed, listening_timeout)

# with col2:
#     if st.button("Stop Listening"):
#         st.session_state.is_running = False
#         st.write("Translation stopped.")

# # Display translation history
# st.subheader("Translation History")
# for item in st.session_state['translation_history']:
#     st.write(f"**You said:** {item['spoken']}")
#     st.write(f"**Translated:** {item['translated']}")

# # Download translation history
# if st.session_state['translation_history']:
#     history_text = "\n\n".join([f"You said: {item['spoken']}\nTranslated: {item['translated']}" 
#                                 for item in st.session_state['translation_history']])
#     st.download_button("Download Translation History", data=history_text, file_name="translation_history.txt", mime="text/plain")


import os
import time
import pygame
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator
import pyttsx3
from gtts.lang import tts_langs

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
        # Check if the language is supported by gTTS
        supported_languages = tts_langs()
        if to_language not in supported_languages:
            st.warning(f"gTTS does not support '{to_language}', using pyttsx3 instead.")

            # Use pyttsx3 for languages unsupported by gTTS
            engine = pyttsx3.init()
            engine.setProperty('rate', int(voice_speed * 150))  # Adjust rate based on speed
            engine.setProperty('volume', 1)  # Max volume
            engine.setProperty('voice', to_language)  # Set voice language
            engine.say(text_data.strip())
            engine.runAndWait()
            return

        # Try using gTTS first
        if not text_data.strip():  # Handle empty strings
            raise ValueError("Text data is empty and cannot be converted to speech.")
        
        myobj = gTTS(text=text_data.strip(), lang=to_language, slow=(voice_speed < 1.0))
        myobj.save("cache_file.mp3")
        pygame.mixer.Sound("cache_file.mp3").play()
        time.sleep(2)  # Wait for audio playback
        os.remove("cache_file.mp3")

    except Exception as e:
        st.warning(f"Error with gTTS: {e}. Switching to pyttsx3.")
        
        # Fallback to pyttsx3 if gTTS fails
        engine = pyttsx3.init()
        engine.setProperty('rate', int(voice_speed * 150))  # Adjust rate based on speed
        engine.setProperty('volume', 1)  # Max volume
        engine.setProperty('voice', to_language)  # Set voice language
        engine.say(text_data.strip())
        engine.runAndWait()

def main_process(output_placeholder, from_language, to_language, voice_speed, listening_timeout, spoken_text=None):
    """Main processing loop for listening, translating, and speaking."""
    if spoken_text:
        # If text is provided (typed), handle it directly
        output_placeholder.success(f"You typed: {spoken_text}")
        # Translate typed text
        translated_text = translator_function(spoken_text, from_language, to_language)
        if "Error" in translated_text:
            output_placeholder.error(translated_text)
        else:
            output_placeholder.success(f"Translated: {translated_text}")
            # Play translated text
            text_to_voice(translated_text, to_language, voice_speed)
    else:
        # If no typed text, handle speech recognition
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            rec.adjust_for_ambient_noise(source, duration=1)
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
                    return

                output_placeholder.success(f"Translated: {translated_text}")

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

# Add typed input field
typed_text = st.text_area("Or type your text to translate:")

# Handle typed translation
if typed_text:
    if st.button("Translate Typed Text"):
        main_process(output_placeholder, from_language, to_language, voice_speed, listening_timeout, typed_text)

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
