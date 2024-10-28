import webbrowser
import pyttsx3
import requests

# Initialize text-to-speech engine
text_to_speech = pyttsx3.init()

# Replace with your actual API key and music link
newsapikey = "YOUR_KEY"
music = "Your_link"

def speak(text):
    """Convert text to speech."""
    text_to_speech.say(text)
    text_to_speech.runAndWait()

def giventask(cmd):
    """Execute a command based on user input."""
    # Open Google and perform a search
    if "open google" in cmd.lower():
        search_query = input("What do you want to search on Google? ")
        google_search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
        print(f"Searching for: {search_query}")
        print(f"Google Search URL: {google_search_url}")
        webbrowser.open(google_search_url)
    
    # Open YouTube and search for a video
    elif "open youtube" in cmd.lower() or "play" in cmd.lower():
        search_query = input("What do you want to play on YouTube? ")
        youtube_search_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
        print(f"Searching and playing: {search_query}")
        print(f"YouTube Search URL: {youtube_search_url}")
        webbrowser.open(youtube_search_url)
    
    # Fetch and read aloud the top news headlines
    elif "news" in cmd.lower():
        req = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapikey}")
        if req.status_code == 200:
            data = req.json()
            if "articles" in data:
                articles = data["articles"]
                for article in articles:
                    print(article['title'])
                    speak(article['title'])
        else:
            print(f"Failed to fetch news: {req.status_code}")

if __name__ == "__main__":
    print("Starting system, please wait.....")
    speak("Initializing test_spice1.....")

    while True:
        try:
            # Await initial command from user
            initial_cmd = input("Type 'test_spice1' to start or 'quit' to exit: ").lower()

            if initial_cmd == "test_spice1":
                print("Yes, I am listening...")
                speak("Yes, I am listening...")

                # Await specific task from user
                task = input("You can type your command now: ").lower()
                print(f"Executing: {task}")
                giventask(task)

            elif initial_cmd == "quit":
                print("Exiting system...")
                speak("Goodbye!")
                break

        except Exception as e:
            print(f"An error occurred: {e}")
