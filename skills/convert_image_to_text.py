"""
Skill: convert_image_to_text
Description: convert image to text using OCR
Category: automation
Usage: convert_image_to_text(**kwargs)
Parameters: 
    - image_path (str): Path to the image file
    - output_format (str): Format of output text ('plain', 'json') [optional]
    - language (str): Language code for OCR recognition [optional]
"""

import os
import logging
from typing import Dict, Any, Optional, Union
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def execute(**kwargs) -> Dict[str, Any]:
    """
    Main entry point to convert image to text using OCR
    
    Args:
        **kwargs: Keyword arguments including image_path, output_format, language
        
    Returns:
        Dict containing result status and extracted text
    """
    try:
        # Validate required parameters
        if 'image_path' not in kwargs:
            raise ValueError("Missing required parameter: image_path")
        
        image_path = kwargs.get('image_path')
        output_format = kwargs.get('output_format', 'plain')
        language = kwargs.get('language', 'eng')
        
        # Validate image path
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        # Validate file extension
        valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')
        if not Path(image_path).suffix.lower() in valid_extensions:
            raise ValueError("Unsupported image format. Supported formats: PNG, JPG, JPEG, BMP, TIFF, WEBP")
        
        # Perform OCR conversion
        extracted_text = _perform_ocr(image_path, language)
        
        # Format output based on requested format
        if output_format == 'json':
            result = {
                "status": "success",
                "text": extracted_text,
                "format": output_format,
                "language": language
            }
        else:
            result = {
                "status": "success",
                "text": extracted_text,
                "format": output_format,
                "language": language
            }
        
        logger.info(f"Successfully converted image to text: {image_path}")
        return result
        
    except Exception as e:
        error_msg = f"Error converting image to text: {str(e)}"
        logger.error(error_msg)
        return {
            "status": "error",
            "message": error_msg,
            "text": None
        }

def _perform_ocr(image_path: str, language: str) -> str:
    """
    Perform OCR on the given image file
    
    Args:
        image_path (str): Path to the image file
        language (str): Language code for OCR recognition
        
    Returns:
        Extracted text from the image
    """
    try:
        # Import required libraries only when needed
        import pytesseract
        from PIL import Image
        
        # Validate tesseract installation
        if not _is_tesseract_installed():
            raise RuntimeError("Tesseract OCR not installed or not in PATH")
        
        # Open and process image
        image = Image.open(image_path)
        
        # Perform OCR with specified language
        extracted_text = pytesseract.image_to_string(image, lang=language)
        
        # Clean up text (remove extra whitespace)
        cleaned_text = ' '.join(extracted_text.split())
        
        return cleaned_text
        
    except ImportError:
        raise RuntimeError("Missing required dependency: pytesseract or PIL")
    except Exception as e:
        raise RuntimeError(f"OCR processing failed: {str(e)}")

def _is_tesseract_installed() -> bool:
    """
    Check if tesseract is installed and accessible
    
    Returns:
        bool: True if tesseract is installed, False otherwise
    """
    try:
        import pytesseract
        # Try to get tesseract version or check if it's callable
        pytesseract.get_languages()
        return True
    except Exception:
        # Check if tesseract command exists in PATH
        import subprocess
        try:
            subprocess.run(['tesseract', '--version'], 
                          stdout=subprocess.DEVNULL, 
                          stderr=subprocess.DEVNULL)
            return True
        except (subprocess.SubprocessError, FileNotFoundError):
            return False

# For backward compatibility with older versions that might not have this function
def _safe_execute(**kwargs) -> Dict[str, Any]:
    """
    Execute with additional safety checks for GUI automation
    
    Args:
        **kwargs: Keyword arguments for execution
        
    Returns:
        Dict containing result status and extracted text
    """
    try:
        # Add delay to ensure system stability
        import time
        time.sleep(0.1)
        
        return execute(**kwargs)
        
    except Exception as e:
        logger.error(f"Safe execution failed: {str(e)}")
        return {
            "status": "error",
            "message": str(e),
            "text": None
        }