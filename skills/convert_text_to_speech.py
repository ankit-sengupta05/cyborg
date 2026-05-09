import logging

# Configure logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_text_to_speech(text):
    """
    Converts text to speech using a generic method.

    Parameters:
    -----------
    text: str
        The text you want to convert to speech.
    
    Returns:
    --------
    None
    
    Example Usage:
    ---------------
    >>> convert_text_to_speech("Hello, this is a test.")
    # This will generate speech output with the given text.
    """
    # Placeholder for actual conversion logic (e.g., using pyttsx3)
    logging.info(f"Converting text: {text}")

# Example usage
convert_text_to_speech("This is an example of converting text to speech.")