import sounddevice as sd
import soundfile as sf
import numpy as np
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(duration_seconds: float = 5.0, samplerate: int = 44100, channels: int = 1, filename: str = "output.wav"):
    """
    Records audio from the default microphone for a specified duration and saves it to a file.

    Parameters:
        duration_seconds (float): The length of the recording in seconds. Defaults to 5.0 seconds.
        samplerate (int): The sample rate of the audio (samples per second). Defaults to 44100 Hz.
        channels (int): The number of audio channels (1 for mono, 1 for stereo, etc.). Defaults to 1.
        filename (str): The name of the file to save the recorded audio. Defaults to "output.wav".

    Returns:
        str: The path to the saved audio file, or None if an error occurred.
    """
    logging.info(f"Starting audio recording for {duration_seconds} seconds...")
    try:
        # Use sounddevice to record audio
        recording = sd.rec(int(duration_seconds * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
        sd.rec(int(duration_seconds * samplerate), samplerate=samplerate, channels=channels, dtype='int16', callback=lambda channel, indata, frames, time, status: None)
        sd.wait()  # Wait until recording is finished

        # Save the recorded data to a WAV file
        sf.write(filename, recording, samplerate)
        logging.info(f"Audio successfully saved to {filename}")
        return filename
    except Exception as e:
        logging.error(f"An error occurred during audio recording: {e}")
        return None

def execute(**kwargs):
    """
    Main entry point for the skill execution.
    Parses arguments and calls the appropriate function based on the provided keyword arguments.
    """
    # In a real skill environment, kwargs would contain parameters passed directly to the skill.
    print("--- Skill Execution Initiated ---")
    
    # Example usage demonstration:
    if 'duration' in kwargs:
        duration = kwargs['duration']
        print(f"Executing record_audio with duration={duration}")
        result = record_audio(duration_seconds=duration)
        if result:
            print(f"Execution successful. Result: {result}")
        else:
            print("Execution failed.")
    elif 'filename' in kwargs:
        filename = kwargs['filename']
        print(f"Executing record_audio with filename={filename}")
        result = record_audio(filename=filename)
        if result:
            print(f"Execution successful. Result: {result}")
        else:
            print("Execution failed.")
    else:
        print("No recognized parameters provided. Please provide 'duration' or 'filename'.")

# Example of how this module might be used (for testing purposes)
if __name__ == '__main__':
    print("--- Testing Module Locally ---")
    # Test 1: Record 3 seconds and save to test_test.wav
    record_audio(duration_seconds=3, filename="test_test.wav")

    # Test 2: Record 5 seconds with default settings
    record_audio()
    
    print("\n--- Local Testing Complete ---")