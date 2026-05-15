import datetime
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def execute(**kwargs):
    """
    Main entry point for the get_current_system_date skill.
    Retrieves and returns the current system date in a standardized format.

    This function is designed to be generic, accepting no specific parameters
    but providing a reliable system time retrieval mechanism.

    Args:
        **kwargs: Keyword arguments passed to the skill (unused for this simple read operation).

    Returns:
        str: A formatted string representing the current date, or an error message.
    """
    try:
        # 1. Get the current system time using standard library
        current_date = datetime.datetime.now()

        # 2. Format the output to be standardized and readable (YYYY-MM-DD format)
        formatted_date = current_date.strftime("%Y-%m-%d")

        logging.info(f"Successfully retrieved system date: {formatted_date}")
        return f"The current system date is: {formatted_date}"

    except Exception as e:
        # 3. Robust error handling
        error_message = f"Error retrieving the system date: {e}"
        logging.error(error_message)
        return f"Failed to get the system date. Please check system time services or try again. Details: {type(e).__name__}"

# --- Skill Metadata Placeholder (For documentation/discovery systems) ---
# In a real framework, this would be registered automatically.
SKILL_METADATA = {
    "Skill": "get_system_date",
    "Description": "Retrieves the current date from the operating system.",
    "Category": "automation",
    "Usage": "get_current_system_date(**kwargs)",
    "Parameters": "" # No parameters needed for this specific task
}

# To make it self-contained and runnable, we'll structure the module around the execute function.
# If pyautogui were required, imports and safety checks would be added here.
# Since only standard library is used, no extra dependencies are needed beyond what was imported.