import pyttsx3

def convert_text_to_speech(text, language='en', speed=1.0):
    """
    Convert text to speech using pyttsx3.

    Parameters:
        text (str): The text to be converted.
        language (str): Language code for the desired output language (default 'en').
        speed (float): Speed of speaking (default 1.0).

    Returns:
        None
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', int(speed * 250))
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[language].id)
    engine.say(text)
    engine.runAndWait()

# Example usage: convert_text_to_speech("Hello, how are you?", language='en', speed=1.5)