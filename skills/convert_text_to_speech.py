import pyttsx3

def execute(text):
    """
    Convert text to speech using pyttsx3.

    Parameters:
        text (str): The text that needs to be converted into speech.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    if not voices:
        raise ValueError("No available voice")
    
    engine.setProperty('voice', voices[0].id)  # Using the first available voice
    
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    
    engine.say(text)
    engine.runAndWait()

# Example usage: convert text to speech
execute("Hello, this is a test of converting text to speech.")