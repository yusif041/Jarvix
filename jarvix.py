import speech_recognition as sr
import pyttsx3
import pyautogui
import time
import sounddevice as sd
import soundfile as sf
import os
import keyboard

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(f"Jarvix: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    duration = 5
    sample_rate = 44100
    print("Listening...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    filename = "temp_audio.wav"
    sf.write(filename, recording, sample_rate)
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
    
    time.sleep(0.1)
    try:
        query = recognizer.recognize_google(audio_data, language='en-in')
        print(f"User: {query}")
        os.remove(filename)
        return query.lower()
    except:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass
        return ""

def search_windows(query):
    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write(query)
    time.sleep(0.5)
    pyautogui.press('enter')

def main():
    print("jarvix is online... Press ESC to stop.")
    speak("jarvix is online.")
    while True:
        if keyboard.is_pressed('esc'):
            print("\nStopping...")
            break
            
        text = listen()
        if text:
            if "jarvix" in text:
                print("Yes sir!")
                speak("Yes sir!")
            else:
                print(f"Searching for: {text}")
                search_windows(text)
        else:
            message = "I think you didn't say something or I couldn't hear you. Please tell again."
            print(message)
            speak(message)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting down...")