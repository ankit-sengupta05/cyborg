import pyaudio
import pyttsx3

def convert_text_to_speech(text):
    """
    Converts text to speech using the pyttsx3 library.

    Parameters:
        text (str): The text to be converted into speech.
    
    Returns:
        None
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example usage: convert_text_to_speech("Hello, this is a test.")