import pyautogui

def execute(**kwargs):
    """
    Converts text to speech and plays it.

    Parameters:
        - text (str): The text to be converted.
        - speed (float, optional): Speed of the audio output. Default is 100.
        - volume (int, optional): Volume level from 0-100. Default is 50.
    """
    try:
        # Convert text to speech
        pyautogui.speak(text=kwargs.get('text', ''))
        
        # Play the converted audio at specified speed and volume
        pyautogui.playSound(kwargs.get('audio_file'), speed=kwargs.get('speed', 100), volume=kwargs.get('volume', 50))
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# execute(text="Hello, this is a test.", audio_file="test.mp3", speed=200, volume=75)