import datetime
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def execute(**kwargs):
    """
    Main entry point for the get_current_system_date skill.

    Retrieves and returns the current system date in a standardized format.

    Args:
        **kwargs: Accepts any keyword arguments, though none are strictly required 
                  for this basic function. They allow for future expansion.

    Returns:
        str: A formatted string representing the current date, or an error message.
    """
    try:
        # Use datetime module for standard system time retrieval
        now = datetime.datetime.now()
        
        # Format the date into a highly readable and standardized format (YYYY-MM-DD HH:MM:SS)
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        
        logging.info(f"Successfully retrieved system date: {formatted_date}")
        return f"The current system date and time is: {formatted_date}"

    except Exception as e:
        # Comprehensive error handling
        error_message = f"Failed to retrieve the system date due to an unexpected error: {e}"
        logging.error(error_message)
        return error_message

# --- Skill Metadata and Documentation Block (As required by prompt structure) ---
"""
Skill: get_system_date
Description: Retrieves the current system date and time from the operating system.
Category: automation
Usage: get_system_date(**kwargs)
Parameters: 
    None are required, but future expansion might include timezone specification (e.g., tz='America/Los_Angeles').
"""

# Note on Pyautogui: Since this task only requires standard OS time retrieval, 
# pyautogui is not necessary and has been omitted to keep the module clean and dependency-minimal.
# If GUI interaction were needed (e.g., reading a clock widget), it would be imported here.
# Example structure if pyautogui was needed:
# import pyautogui
# import time
# def execute_gui(**kwargs):
#     try:
#         time.sleep(1) # Safety delay
#         screenshot = pyautogui.screenshot()
#         return f"Screenshot taken successfully (GUI interaction simulated)."
#     except Exception as e:
#         logging.error(f"Pyautogui failed: {e}")
#         return "Error during GUI capture."

# The module is self-contained and relies only on standard libraries (datetime, logging).