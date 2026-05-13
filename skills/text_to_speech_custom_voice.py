"""
Skill: text_to_speech_custom_voice
Description: convert text to speech with custom voice settings
Category: automation
Usage: text_to_speech_custom_voice(**kwargs)
Parameters: 
    - text (str): The text to convert to speech
    - voice_id (str): Identifier for the voice to use
    - rate (int): Speech rate in words per minute (default: 200)
    - volume (float): Volume level between 0.0 and 1.0 (default: 1.0)
    - output_file (str): Optional path to save audio file
"""

import os
import sys
import logging
from typing import Dict, Any, Optional

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def execute(**kwargs) -> Dict[str, Any]:
    """
    Main entry point for text to speech conversion with custom voice settings
    
    Args:
        **kwargs: Keyword arguments for text-to-speech parameters
        
    Returns:
        Dict containing execution results and status
    """
    try:
        # Extract parameters with defaults
        text = kwargs.get('text', '')
        voice_id = kwargs.get('voice_id', 'default')
        rate = kwargs.get('rate', 200)
        volume = kwargs.get('volume', 1.0)
        output_file = kwargs.get('output_file', None)
        
        # Validate required parameters
        if not text:
            raise ValueError("Text parameter is required")
            
        # Validate voice_id
        if not isinstance(voice_id, str):
            raise ValueError("Voice ID must be a string")
            
        # Validate rate
        if not isinstance(rate, int) or rate < 50:
            raise ValueError("Rate must be an integer >= 50")
            
        # Validate volume
        if not isinstance(volume, (int, float)) or not 0.0 <= volume <= 1.0:
            raise ValueError("Volume must be a float between 0.0 and 1.0")
            
        # Execute text to speech conversion
        result = _convert_text_to_speech(
            text=text,
            voice_id=voice_id,
            rate=rate,
            volume=volume,
            output_file=output_file
        )
        
        logger.info(f"Text-to-speech completed successfully for: {text[:50]}...")
        return {
            'status': 'success',
            'message': 'Text converted to speech successfully',
            'result': result
        }
        
    except Exception as e:
        error_msg = f"Error in text_to_speech_custom_voice: {str(e)}"
        logger.error(error_msg)
        return {
            'status': 'error',
            'message': error_msg,
            'result': None
        }

def _convert_text_to_speech(text: str, voice_id: str, rate: int, volume: float, output_file: Optional[str]) -> Dict[str, Any]:
    """
    Internal function to perform text-to-speech conversion
    
    Args:
        text (str): Text to convert
        voice_id (str): Voice identifier
        rate (int): Speech rate
        volume (float): Volume level
        output_file (str): Optional output file path
        
    Returns:
        Dict with conversion details
    """
    try:
        # Import platform-specific modules
        if sys.platform.startswith('win'):
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            
            # Set voice
            if voice_id != 'default':
                # Note: This is a simplified approach - actual implementation 
                # would need to enumerate available voices
                pass
                
            # Set rate and volume
            speaker.Rate = rate - 200  # Convert to SAPI scale (range -10 to 10)
            speaker.Volume = int(volume * 100)  # Convert to percentage
            
            if output_file:
                # Save to file using SAPI
                speaker.SaveToWaveFile(output_file, text)
                logger.info(f"Audio saved to {output_file}")
            else:
                # Speak aloud
                speaker.Speak(text)
                
        elif sys.platform.startswith('darwin'):
            # macOS - use system say command
            import subprocess
            cmd = ['say', text]
            if output_file:
                cmd.extend(['-o', output_file])
            subprocess.run(cmd, check=True)
            
        else:
            # Linux and other platforms - use espeak
            import subprocess
            cmd = ['espeak', '-s', str(rate), '-v', voice_id, '-a', str(int(volume*100)), text]
            if output_file:
                cmd.extend(['-w', output_file])
            subprocess.run(cmd, check=True)
            
        return {
            'text': text,
            'voice_id': voice_id,
            'rate': rate,
            'volume': volume,
            'output_file': output_file
        }
        
    except Exception as e:
        logger.error(f"Failed to convert text to speech: {str(e)}")
        raise

# For testing purposes only
if __name__ == "__main__":
    # Example usage
    result = execute(
        text="Hello, this is a test of the text to speech conversion.",
        voice_id="default",
        rate=180,
        volume=0.9,
        output_file=None
    )
    print(result)