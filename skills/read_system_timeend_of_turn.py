import datetime
import logging
from typing import Dict, Any

# Setup basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def execute(**kwargs: Any) -> Dict[str, Any]:
    """
    Skill: read_system_time
    Description: Reads and returns the current system time in a standardized format.
    Category: automation
    Usage: read_system_time(**kwargs)
    Parameters: None (Uses system clock directly)
    """
    logging.info("Attempting to read system time...")
    try:
        # 1. Get the current time object
        now = datetime.datetime.now()

        # 2. Format the output string for readability and consistency
        # Example format: YYYY-MM-DD HH:MM:SS (with timezone info if available)
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Optionally include microseconds or timezone offset if needed for higher precision
        detailed_info = f"The current system time is: {formatted_time}."

        logging.info(f"Successfully retrieved time: {formatted_time}")

        return {
            "success": True,
            "message": detailed_info,
            "timestamp": now.isoformat(),  # ISO format for machine readability
            "raw_datetime": str(now) # Full string representation
        }

    except Exception as e:
        logging.error(f"An unexpected error occurred while reading system time: {e}", exc_info=True)
        return {
            "success": False,
            "message": f"Failed to read the system time due to an internal error: {str(e)}",
            "timestamp": None,
            "raw_datetime": None
        }

# Example of how this module could be extended (Scalability/Reusability Placeholder)
def get_current_time_with_timezone() -> str:
    """Returns the current time including timezone information."""
    try:
        now = datetime.datetime.now(datetime.timezone.utc)
        return now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    except Exception as e:
        logging.warning(f"Could not get time with timezone: {e}")
        return "Timezone information unavailable."

# Note: Since this task only requires reading the system clock, pyautogui is unnecessary.
# If GUI interaction were needed (e.g., clicking a clock widget), we would add:
# import pyautogui
# import time
# def gui_read_time():
#     try:
#         logging.info("Simulating GUI read...")
#         pyautogui.PAUSE = 0.5 # Set global pause for safety
#         time.sleep(1) # Wait for system to settle
#         # pyautogui.screenshot() # Example action
#         return {"success": True, "message": "GUI reading simulated successfully."}
#     except pyautogui.FailSafeException:
#         logging.error("PyAutoGUI failed safe.")
#         return {"success": False, "message": "Automation aborted by user safety mechanism."}

# End of Module Structure
if __name__ == '__main__':
    print("\n--- Testing read_system_time module ---")
    result = execute()
    import json
    print(json.dumps(result, indent=4))
    
    print("\n--- Testing Timezone Extension ---")
    tz_result = get_current_time_with_timezone()
    print(f"Timezone Check: {tz_result}")