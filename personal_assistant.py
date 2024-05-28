import speech_recognition as sr
import pyttsx3

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice commands
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

# Main function to handle commands
def main():
    speak("Hello! I'm your personal assistant. How can I help you today?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "how are you" in command:
            speak("I'm doing well, thank you for asking.")
        elif "thank you" in command:
            speak("You're welcome!")
        elif "goodbye" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
