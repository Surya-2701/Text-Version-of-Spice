import webbrowser
import pyttsx3
import requests

# Initialize the text-to-speech engine
text_to_speech = pyttsx3.init()

# Replace with your actual API key and music link
NEWS_API_KEY = "YOUR_API_KEY"
MUSIC_LINK = "Your_music_link"

def speak(text):
    """Convert text to speech."""
    text_to_speech.say(text)
    text_to_speech.runAndWait()

def search_google():
    """Search Google for a user-provided query."""
    search_query = input("What do you want to search on Google? ")
    if search_query.strip():
        google_search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
        print(f"Searching for: {search_query}")
        webbrowser.open(google_search_url)
    else:
        print("No search query provided.")
