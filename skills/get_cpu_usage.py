import psutil
import time
import logging

# Setup basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_current_system_cpu_usage(**kwargs):
    """
    Skill: get_cpu_usage
    Description: Get the current system CPU utilization percentage.
    Category: automation
    Usage: get_cpu_usage(interval=1, **kwargs)
    Parameters:
        interval (float): The time interval in seconds to measure CPU usage over. Defaults to 0.5.
        **kwargs: Additional keyword arguments that might be used for future expansion.
    """
    try:
        # Check if an interval was provided, otherwise use a sensible default
        interval = kwargs.get('interval', 0.5)

        if not isinstance(interval, (int, float)) or interval <= 0:
            logging.warning("Invalid or missing 'interval'. Defaulting to 0.5 seconds.")
            interval = 0.5

        logging.info(f"Attempting to measure CPU usage over an interval of {interval} seconds...")

        # psutil.cpu_percent() calculates the percentage since the last call or over a specified interval
        cpu_usage = psutil.cpu_percent(interval=interval)

        if cpu_usage is not None:
            result = f"The current system CPU usage is {cpu_usage:.2f}%."
            logging.info(result)
            return result
        else:
            raise RuntimeError("Failed to retrieve CPU usage data from the operating system.")

    except psutil.AccessDenied as e:
        error_msg = f"Permission denied when accessing CPU metrics. Ensure the script has necessary permissions. Error: {e}"
        logging.error(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"An unexpected error occurred while getting CPU usage: {type(e).__name__} - {str(e)}"
        logging.error(error_msg)
        return error_msg

def execute(**kwargs):
    """
    Main entry point for the get_cpu_usage skill.
    It calls the core logic function, passing along all received arguments.
    """
    logging.info("--- Executing get_cpu_usage Skill ---")
    # Pass all kwargs directly to the specialized function
    return get_current_system_cpu_usage(**kwargs)

# Example usage (for testing purposes, not part of the final module structure if only execute is required)
if __name__ == '__main__':
    print("\n--- Testing Skill Execution ---")
    # Test 1: Default interval
    result_default = execute()
    print(f"\n[Test Result - Default]: {result_default}")

    time.sleep(1) # Wait to ensure a measurable difference for the next test

    # Test 2: Custom interval
    result_custom = execute(interval=1.5)
    print(f"\n[Test Result - Custom Interval]: {result_custom}")