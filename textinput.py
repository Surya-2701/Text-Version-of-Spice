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
def search_youtube():
    """Search YouTube for a user-provided query."""
    search_query = input("What do you want to play on YouTube? ")
    if search_query.strip():
        youtube_search_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
        print(f"Searching and playing: {search_query}")
        webbrowser.open(youtube_search_url)
    else:
        print("No search query provided.")
def fetch_news():
    """Fetch and read aloud the top news headlines."""
    try:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}")
        if response.status_code == 200:
            data = response.json()
            if "articles" in data:
                articles = data["articles"]
                if articles:
                    for article in articles[:5]:  # Limit to top 5 headlines
                        title = article.get('title', 'No title available')
                        print(title)
                        speak(title)
                else:
                    print("No news articles available.")
                    speak("No news articles available.")
            else:
                print("Unexpected data format received.")
        else:
            print(f"Failed to fetch news: {response.status_code}")
            speak("I was unable to fetch the news.")
    except requests.RequestException as e:
        print(f"An error occurred while fetching news: {e}")
        speak("An error occurred while fetching the news.")
def giventask(cmd):
    """Execute a command based on user input."""
    if "open google" in cmd:
        search_google()
    elif "open youtube" in cmd or "play" in cmd:
        search_youtube()
    elif "news" in cmd:
        fetch_news()
    else:
        print("Command not recognized. Please try again.")
        speak("Command not recognized. Please try again.")

if __name__ == "__main__":
    print("Starting system, please wait.....")
    speak("Initializing system...")
    while True:
        try:
            initial_cmd = input("Type 'start' to begin or 'quit' to exit: ").strip().lower()
            if initial_cmd == "start":
                print("System initialized. Ready to take commands.")
                speak("System initialized. Ready to take commands.")
                while True:
                    task = input("You can type your command now (or type 'exit' to return): ").strip().lower()
                    if task == "exit":
                        print("Returning to main menu...")
                        speak("Returning to main menu.")
                        break
                    print(f"Executing: {task}")
                    giventask(task)
            elif initial_cmd == "quit":
                print("Exiting system...")
                speak("Goodbye!")
                break
            else:
                print("Invalid input. Please type 'start' to begin or 'quit' to exit.")
                speak("Invalid input. Please type start to begin or quit to exit.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            speak("An unexpected error occurred. Please try again.")
