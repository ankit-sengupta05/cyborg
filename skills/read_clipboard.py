import logging
import sys
from typing import Any, Dict

try:
    # Using pyperclip as a more standard and often preferred library for clipboard access 
    # in Python scripting environments, especially when pyautogui might be overkill or fail.
    import pyperclip
except ImportError:
    print("Pyperclip not found. Please install it using: pip install pyperclip")
    sys.exit(1)

# --- Setup Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def read_system_clipboard() -> str:
    """Reads the content of the system clipboard using pyperclip."""
    try:
        # pyperclip handles reading text from the clipboard reliably across platforms.
        clipboard_content = pyperclip.paste()
        logger.info("Successfully read content from the system clipboard.")
        return clipboard_content
    except pyperclip.PyperclipException as e:
        logger.error(f"Failed to read system clipboard using pyperclip: {e}")
        # Re-raise as a RuntimeError to maintain consistency with the original structure's error handling
        raise RuntimeError(f"Could not access the clipboard via pyperclip. Ensure necessary permissions are granted or that a clipboard manager is running. Error: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred while reading the system clipboard: {e}")
        raise RuntimeError(f"Unexpected error accessing clipboard: {e}")

def execute(**kwargs) -> Dict[str, Any]:
    """
    Main entry point for the skill module. Reads and returns the system clipboard content.

    This function is designed to be generic, accepting keyword arguments 
    though it currently only uses its core functionality (reading the clipboard).

    Args:
        **kwargs: Arbitrary keyword arguments passed to the skill execution environment.

    Returns:
        A dictionary containing the result of the operation.
    """
    logger.info("--- Starting read_system_clipboard Skill Execution ---")
    try:
        # The core task is reading the clipboard, which requires no external parameters 
        # beyond what's available in the system environment.
        content = read_system_clipboard()

        result = {
            "success": True,
            "operation": "read_system_clipboard",
            "data": content,
            "message": f"Clipboard successfully read. Content length: {len(content)}"
        }
        return result
    except RuntimeError as e:
        logger.error(f"Skill execution failed due to clipboard error: {e}")
        return {
            "success": False,
            "operation": "read_system_clipboard",
            "error": str(e),
            "message": "Failed to read the system clipboard."
        }
    except Exception as e:
        logger.error(f"An unexpected error occurred during skill execution: {e}")
        return {
            "success": False,
            "operation": "read_system_clipboard",
            "error": str(e),
            "message": "An unexpected error occurred."
        }

# --- Module Metadata (Self-Contained Structure) ---
"""
Skill: read_clipboard
Description: Reads the content of the system clipboard.
Category: automation
Usage: read_clipboard(**kwargs)
Parameters: None required for basic operation.
"""