Voice Assistant Program
This simple command-line voice assistant performs tasks like web searches, playing YouTube videos, and fetching news using the following features:

Features
Text-to-Speech
Integrates pyttsx3 for vocal responses to user commands and news headlines.
Google Search
Command: open Google
Prompts for a query and opens results in the web browser.
YouTube Search & Playback
Commands: open YouTube, play
Constructs a YouTube search URL based on user input and opens it in the browser.
News Fetching
Command: news
Retrieves and reads top U.S. headlines using NewsAPI.
Interactive Commands
test_spice1 to start the assistant.
quit to exit the program.
Error Handling
Includes basic error management to handle invalid input or API issues.
Dependencies
pyttsx3: for text-to-speech.
requests: for API interactions.
webbrowser: for opening URLs.
