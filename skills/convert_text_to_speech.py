import pyttsx3

def execute(text, **kwargs):
    """
    Convert text to speech using pyttsx3.

    Parameters:
    - text: The text to be converted into speech.
    - kwargs: Additional keyword arguments (not used in this function).

    Returns:
    None
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example usage: convert text to speech
execute("Hello, world!")