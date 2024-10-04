import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen to the microphone and recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)  # Use Google Web Speech API
            print(f"You said: {query}")
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
            return ""
        except sr.RequestError:
            print("Sorry, the service is down.")
            return ""
        return query

# Main function to handle voice commands
def voice_assistant():
    speak("Hello! How can I assist you today?")
    while True:
        query = listen().lower()
        
        if "exit" in query or "bye" in query:
            speak("Goodbye!")
            break
        
        if "how are you" in query:
            speak("I'm doing well, thank you!")
        
        elif "your name" in query:
            speak("I am your voice assistant.")
        
        else:
            speak("Sorry, I can't handle that request yet.")
    
# Run the voice assistant
if __name__ == "__main__":
    voice_assistant()
