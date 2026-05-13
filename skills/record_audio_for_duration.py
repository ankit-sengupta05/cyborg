"""
Skill: record_audio_for_duration
Description: record audio for specified duration
Category: automation
Usage: record_audio_for_duration(**kwargs)
Parameters: 
    - duration (int): Duration to record in seconds
    - output_file (str): Path to save the recorded audio file
    - sample_rate (int): Audio sample rate (default: 44100)
    - channels (int): Number of audio channels (default: 2)
    - chunk_size (int): Audio chunk size (default: 1024)
"""

import os
import sys
import logging
import time
from contextlib import contextmanager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    import pyaudio
    import wave
except ImportError as e:
    logger.error(f"Missing required dependency: {e}")
    raise ImportError("Please install pyaudio: pip install pyaudio")

def execute(**kwargs):
    """
    Record audio for specified duration
    
    Args:
        **kwargs: Keyword arguments including duration, output_file, sample_rate, channels, chunk_size
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Extract parameters with defaults
        duration = kwargs.get('duration', 5)
        output_file = kwargs.get('output_file', 'recorded_audio.wav')
        sample_rate = kwargs.get('sample_rate', 44100)
        channels = kwargs.get('channels', 2)
        chunk_size = kwargs.get('chunk_size', 1024)
        
        # Validate inputs
        if duration <= 0:
            raise ValueError("Duration must be positive")
        if not output_file:
            raise ValueError("Output file path is required")
            
        logger.info(f"Starting audio recording for {duration} seconds to {output_file}")
        
        # Record audio
        record_audio(duration, output_file, sample_rate, channels, chunk_size)
        
        logger.info("Audio recording completed successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error during audio recording: {e}")
        return False

def record_audio(duration, output_file, sample_rate, channels, chunk_size):
    """
    Record audio for specified duration
    
    Args:
        duration (int): Duration to record in seconds
        output_file (str): Path to save the recorded audio file
        sample_rate (int): Audio sample rate
        channels (int): Number of audio channels
        chunk_size (int): Audio chunk size
    """
    # Initialize PyAudio
    p = pyaudio.PyAudio()
    
    try:
        # Open stream
        stream = p.open(
            format=pyaudio.paInt16,
            channels=channels,
            rate=sample_rate,
            input=True,
            frames_per_buffer=chunk_size
        )
        
        logger.info("Recording started...")
        
        # Prepare to store audio data
        frames = []
        total_frames = int(sample_rate / chunk_size * duration)
        
        # Record audio in chunks
        for i in range(total_frames):
            data = stream.read(chunk_size, exception_on_overflow=False)
            frames.append(data)
            
        logger.info(f"Recorded {len(frames)} chunks")
        
        # Stop and close stream
        stream.stop_stream()
        stream.close()
        
        # Save audio to file
        with wave.open(output_file, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))
            
        logger.info(f"Audio saved to {output_file}")
        
    except Exception as e:
        logger.error(f"Error during recording: {e}")
        raise
    finally:
        # Terminate PyAudio
        p.terminate()

# Example usage function (not required but for reference)
def example_usage():
    """
    Example of how to use the record_audio_for_duration skill
    """
    result = execute(
        duration=10,
        output_file="test_recording.wav",
        sample_rate=44100,
        channels=2,
        chunk_size=1024
    )
    return result

if __name__ == "__main__":
    # Example usage when run directly
    if len(sys.argv) > 1:
        duration = int(sys.argv[1]) if sys.argv[1].isdigit() else 5
        execute(duration=duration, output_file="output.wav")
    else:
        execute(duration=5, output_file="output.wav")