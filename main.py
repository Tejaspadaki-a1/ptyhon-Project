from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import smtplib

Builder.load_string(
    '''
<MyBoxLayout>:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(10)

    MDTextField:
        id: query_input
        hint_text: 'Enter your query'

    MDRaisedButton:
        text: 'Submit'
        on_press: app.process_query(query_input.text)
'''
)

class MyBoxLayout(MDBoxLayout):
    pass

class MyApp(MDApp):
    def build(self):
        return MyBoxLayout()

    def process_query(self, query):
        # Add logic to process the query here
        print(f"Processing query: {query}")

        # Add your existing voice-controlled logic here
        if 'wikipedia' in query:
            self.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            self.speak("According to Wikipedia")
            print(results)
            self.speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        # ... (Add other voice-controlled logic as needed)

    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()

if __name__ == "__main__":
    MyApp().run()
