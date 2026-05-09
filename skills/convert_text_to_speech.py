import pyttsx3

def convert_text_to_speech(text, voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_US_Edward_v2', rate=150):
    """
    Convert text to speech using pyttsx3.

    Parameters:
        text (str): The text to be converted.
        voice_id (str, optional): The ID of the voice to use. Defaults to 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_US_Edward_v2'.
        rate (int, optional): The speaking rate in words per minute. Defaults to 150.

    Returns:
        None
    """
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()

# Example usage: convert_text_to_speech("Hello, world!")