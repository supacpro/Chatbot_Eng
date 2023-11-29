import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="en-US")
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")
        return None

def voice_assistant():
    speak("Hello! I am your voice assistant. How can I help you today?")

    while True:
        command = listen()

        if command:
            if "stop" in command.lower():
                speak("Goodbye! Have a great day.")
                break
            elif "search" in command.lower():
                speak("What would you like to search for?")
                search_query = listen()
                speak(f"Searching for {search_query}...")
                # Implement your search functionality here
            else:
                speak("I'm sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    voice_assistant()
