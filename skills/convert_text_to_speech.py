import pyautogui

def execute(**kwargs):
    """
    Converts text to speech and plays it using the default system audio player.

    Parameters:
        - text (str): The text to be converted into speech.
        - speed (float, optional): Speed of speech. Default is 1.0.
        - volume (int, optional): Volume level from 0-100. Default is 50.
    """
    try:
        pyautogui.speak(text=kwargs.get('text'), rate=kwargs.get('speed', 1.0), volume=kwargs.get('volume', 50))
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
execute(text="Hello, this is a test", speed=2.0, volume=75)