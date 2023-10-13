import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

while True:
    # Get user input for text to convert to speech
    text = input("Enter the text you want to convert to speech (or type 'exit' to quit): ")

    # Check if the user wants to exit
    if text.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break

    # Convert text to speech
    engine.say(text)

    # Wait for the speaking to finish before continuing the loop
    engine.runAndWait()
