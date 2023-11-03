# import speech_recognition as sr
# import pyttsx3
# import datetime
# import webbrowser
# import os

# # Initialize the speech recognition engine
# recognizer = sr.Recognizer()

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Function to speak text
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Function to recognize speech
# def listen():
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#         command = ""
#         try:
#             command = recognizer.recognize_google(audio)
#             print("You said: " + command)
#         except sr.UnknownValueError:
#             print("Sorry, I couldn't understand that.")
#         return command

# # Main program
# if __name__ == "__main__":
#     speak("Hello! How can I assist you today?")

#     while True:
#         command = listen().lower()

#         if "time" in command:
#             current_time = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"The current time is {current_time}")

#         elif "search" in command:
#             speak("What do you want to search for?")
#             search_query = listen()
#             url = f"https://www.google.com/search?q={search_query}"
#             webbrowser.open(url)

#         elif "exit" in command:
#             speak("Goodbye!")
#             exit()


import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/api/command", methods=["POST"])
def process_command():
    data = request.get_json()
    command = data["command"].lower()
    response = "Sorry, I don't understand that command."

    if "hello" in command:
        response = "Hello! How can I help you?"
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {current_time}"
    elif "exit" in command:
        response = "Goodbye! Have a great day....!!"
    else:
        response = "Sorry, I didn't understand ."

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
