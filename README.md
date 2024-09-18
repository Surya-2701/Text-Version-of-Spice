
Voice Assistant Program
This program is a simple command-line-based voice assistant that performs tasks such as web searching, playing YouTube videos, and fetching news. The program uses the following key features:

Features
Text-to-Speech Integration:
The program can speak responses using the pyttsx3 library, providing a vocal output for user commands and news headlines.

Google Search:
Users can input commands like "open Google", after which the program prompts the user to specify their search query. It automatically opens the search results in a web browser.

YouTube Search and Playback:
By entering commands like "open YouTube" or "play", the user can search for videos on YouTube. The program constructs a search URL and opens it in a browser.

News Fetching:
The program retrieves top headlines from the U.S. using the NewsAPI. News headlines are displayed in the console, and the program reads them aloud using the text-to-speech engine.

Interactive Command Interface:
The program listens for specific keywords in user input to perform actions and responds accordingly. Users can type commands such as:
test_spice1 to initiate the assistant
quit to exit the program
Error Handling:
Basic error handling is implemented to ensure the program does not crash due to unexpected input or API errors.
Dependencies
The program requires the following libraries:
pyttsx3 for text-to-speech
requests for making HTTP requests to external APIs
webbrowser for opening URLs in the default web browser

Setup

Clone this repository.
Install the required dependencies using:
bash
Copy code
pip install pyttsx3 requests
Replace YOUR_KEY in the code with your actual NewsAPI key to enable news fetching.
Run the program:
bash
Copy code
python textinput.py
Usage
Start the program and type test_spice1 to begin.
Enter one of the available commands to perform actions:
Google Search: Type "open Google" and enter your search query.
YouTube Search: Type "open YouTube" or "play" and specify what you want to search.
News: Type "news" to get the latest top headlines from the U.S.
Quit: Type "quit" to exit the program.
