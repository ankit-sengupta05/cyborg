import pyautogui
import pyperclip
import time
import logging
from typing import Optional, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def _capture_screenshot() -> Optional[bytes]:
    """
    Captures the entire screen and returns the screenshot as bytes.
    Uses pyautogui to capture the entire screen.
    Returns:
        Optional[bytes]: The screenshot data or None if an error occurs.
    """
    try:
        # Safety check: Introduce a small delay before capturing
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        return bytes(screenshot)
    except Exception as e:
        logging.error(f"Error during screenshot capture: {e}")
        return None

def _save_to_clipboard(screenshot_data: bytes) -> bool:
    """
    Saves the given byte data to the system clipboard.
    Uses pyperclip to copy the data.
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        pyperclip.copy(screenshot_data.decode('utf-8'))
        logging.info("Screenshot successfully copied to clipboard.")
        return True
    except Exception as e:
        logging.error(f"Error saving screenshot to clipboard: {e}")
        return False

def execute(**kwargs) -> Dict[str, Any]:
    """
    Main entry point for the screenshot_to_clipboard skill.
    Executes the screenshot capture and clipboard copy process.
    
    Parameters:
        **kwargs: Optional arguments. Currently accepts no specific parameters.
    
    Returns:
        Dict[str, Any]: A dictionary containing the result status and details.
    """
    logging.info("Starting screenshot_to_clipboard execution.")
    
    screenshot_result = _capture_screenshot()
    
    if screenshot_result is None:
        return {"status": "failed", "reason": "Failed to capture screenshot."}

    success = _save_to_clipboard(screenshot_result)
    
    if success:
        return {"status": "success", "message": "Screenshot saved to clipboard successfully."}
    else:
        return {"status": "failed", "reason": "Failed to copy screenshot to clipboard."}

if __name__ == '__main__':
    # Example usage demonstration (requires pyautogui and pyperclip installed)
    print("--- Running example test ---")
    result = execute()
    print(f"Final Result: {result}")