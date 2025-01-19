import wikipedia
import os
import webbrowser
import time
import pyautogui
import datetime
import pyttsx3
import speech_recognition as sr
import subprocess

# Function to greet the user based on the time of day
def wishme(name):
    now = datetime.datetime.now().hour
    if(0 <= now < 12):
        speak(f"Good Morning {name}, What's for today?")
    elif(12 <= now < 16):
        speak(f"Good Afternoon {name}, How's your day going?")
    elif(16 <= now < 19):
        speak(f"Good Evening {name}, Wanna chill or complete some tasks?")
    else:
        speak(f"It's late {name}, but still, how can I help?")

# Function to speak the text (TTS) using subprocess (Festival)
def speak(text):
    print(f"Computer said: {text}")
    subprocess.run(f'echo {text} | festival --tts', shell=True)

# Function to take voice input from the user
def takeIN():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=1)
        print("Listening.....")
        audio = r.listen(mic)
        print("Recognizing.....")
        try:
            query = r.recognize_google(audio, language='en-in').lower()
            print(f"You said: {query}")
            return query
        except(sr.UnknownValueError):
            print("Sorry, I couldn't understand that.")
            return None
        except(sr.RequestError):
            speak("There's some issue with your internet or proxy")
            return None

# Function to get the user's name from a file (if it exists) or ask for it
def get_user_name():
    # Try to read the user's name from a file
    try:
        with open("user_name.txt", "r") as file:
            name = file.read().strip()
            if name:
                return name
    except FileNotFoundError:
        pass  # If the file doesn't exist, ask for the name
    
    # If no name found, prompt the user for their name
    speak("Please tell me, what would you like to call yourself?")
    name = input("Enter your name: ")  # Collect user input for name
    # Save the name to a file for future sessions
    with open("user_name.txt", "w") as file:
        file.write(name)
    return name

# Function to update the name if the user requests a change
def change_user_name():
    speak("Sure! Please tell me, what would you like to call yourself?")
    new_name = input("Enter your new name: ")  # Prompt for new name
    # Save the new name to the file
    with open("user_name.txt", "w") as file:
        file.write(new_name)
    return new_name

# Main execution
if __name__ == "__main__":
    user_name = get_user_name()  # Get the user's name (or read it from file)
    wishme(user_name)  # Greet the user

    while True:
        query = takeIN()  # Listen for user command

        if query:
            if "hello" in query:
                speak(f"Hey {user_name}, how can I assist you today?")
            
            elif "exit" in query:
                speak("Goodbye, have a great day!")
                break

            elif "wikipedia" in query:
                speak("Searching Wikipedia, please wait...")
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=1)
                    speak(f"{results}")
                    print(results)
                except wikipedia.PageError:
                    speak("Sorry, I couldn't find anything on Wikipedia.")

            elif "the time" in query:
                current_time = datetime.datetime.now().strftime("%I:%M:%S")
                speak(f"The time is {current_time}")

            elif "open chrome" in query:
                speak("Opening Chrome...")
                os.popen("chromium")  # Update with your browser if different
                time.sleep(4)
                pyautogui.moveTo(597, 460)  # Dynamic positioning can be done if needed
                pyautogui.click()

            elif "update the system" in query:
                speak("Updating the system, please wait...")
                os.popen("konsole")  # Customize terminal command as needed
                time.sleep(5)
                pyautogui.typewrite("sudo apt update && sudo apt upgrade")
                pyautogui.press('enter')
                pyautogui.typewrite("password_here")  # Replace with correct password or mechanism
                pyautogui.press('enter')

            elif "shutdown the system" in query:
                speak("Shutting down the system...")
                subprocess.run(["shutdown", "-h", "now"])

            elif "restart the system" in query:
                speak("Restarting the system...")
                subprocess.run(["reboot"])

            # Command to change the user name
            elif "change my name" in query:
                user_name = change_user_name()  # Change the name and update it
                wishme(user_name)  # Greet with the new name

            # Add more custom commands here if needed (e.g., opening apps, websites, etc.)
            else:
                speak("Sorry, I didn't quite catch that. Can you please repeat?")
        else:
            speak("I'm listening... Please say something.")
