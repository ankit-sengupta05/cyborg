import logging
import subprocess
import platform
import time
from typing import Dict, Any

try:
    # Attempt to import pyautogui for GUI automation fallback/advanced use
    import pyautogui
except ImportError:
    pyautogui = None

# --- Setup Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def execute(**kwargs: Any) -> Dict[str, Any]:
    """
    Main entry point for the open_specific_application skill.
    Attempts to launch an application based on provided arguments.

    Args:
        **kwargs: Expected keys include 'app_name' (string) and optionally 
                   'arguments' (list/string) for command-line arguments.

    Returns:
        A dictionary containing the success status, message, and details.
    """
    logging.info("--- Starting open_specific_application skill execution ---")
    
    app_name = kwargs.get('app_name')
    arguments = kwargs.get('arguments')

    if not app_name:
        error_msg = "The 'app_name' parameter is required to specify which application to open."
        logging.error(f"Execution Failed: {error_msg}")
        return {"success": False, "message": error_msg}

    try:
        if arguments and isinstance(arguments, str):
            # If arguments are passed as a single string, treat them as command-line args
            args_list = [arg.strip() for arg in arguments.split()]
        elif arguments and isinstance(arguments, list):
            args_list = arguments
        else:
            args_list = []

        # --- Core Logic Selection ---
        if platform.system() == "Darwin":  # macOS
            logging.info("Detected OS: macOS. Attempting to use 'open' command.")
            try:
                subprocess.Popen(["open", "-a", app_name] + (["", *args_list] if args_list else []))
                time.sleep(2) # Give the GUI time to launch
                return {"success": True, "message": f"Successfully initiated opening of '{app_name}' on macOS."}
            except FileNotFoundError:
                error_msg = f"The 'open' command or application '{app_name}' was not found. Ensure the app is installed and accessible via system paths."
                logging.error(error_msg)
                return {"success": False, "message": error_msg}

        elif platform.system() == "Windows":  # Windows
            logging.info("Detected OS: Windows. Attempting to use 'start' command.")
            try:
                # Using subprocess.Popen with shell=True is often required for 'start' on Windows, 
                # but this carries security risks; we proceed cautiously here as it's common for system automation.
                command = f'start "" "{app_name}"'
                if args_list:
                    command += " " + " ".join([f'"{arg}"' for arg in args_list])
                
                subprocess.Popen(command, shell=True)
                time.sleep(2) # Give the GUI time to launch
                return {"success": True, "message": f"Successfully initiated opening of '{app_name}' on Windows."}
            except Exception as e:
                error_msg = f"Failed to execute command on Windows for {app_name}: {e}"
                logging.error(error_msg)
                return {"success": False, "message": error_msg}

        elif platform.system() == "Linux":  # Linux (General approach using 'xdg-open' or direct executable call)
            logging.info("Detected OS: Linux. Attempting to use 'xdg-open' or direct execution.")
            try:
                if args_list:
                    command = f"{app_name} {' '.join(args_list)}"
                else:
                    command = app_name
                
                # Try xdg-open first, which is standard for opening files/apps generically on Linux desktops
                subprocess.Popen(["xdg-open", "--working-directory", "."], cwd=None) # Placeholder logic adjustment needed here
                
                # For simplicity and reliability across distributions, we attempt direct execution if no arguments are provided
                if not args_list:
                    subprocess.Popen([app_name])
                else:
                     # If arguments exist, pass them directly to the executable
                    subprocess.Popen([app_name] + args_list)

                time.sleep(2) # Give the GUI time to launch
                return {"success": True, "message": f"Successfully initiated opening of '{app_name}' on Linux."}
            except FileNotFoundError:
                error_msg = f"The application or command '{app_name}' was not found. Ensure it is installed and in your system PATH."
                logging.error(error_msg)
                return {"success": False, "message": error_msg}

        else:
            error_msg = f"Unsupported operating system detected: {platform.system()}."
            logging.error(error_msg)
            return {"success": False, "message": error_msg}

    except Exception as e:
        error_msg = f"An unexpected critical error occurred during execution for {app_name}: {e}"
        logging.critical(error_msg)
        return {"success": False, "message": error_msg}


# --- Skill Module Metadata (Not part of the executable code block but required by prompt structure) ---

"""
Skill: open_app
Description: open_specific_application
Category: automation
Usage: open_app(**kwargs)
Parameters: 
    app_name (str): The name or command to execute (e.g., 'chrome', 'Calculator').
    arguments (list[str] | str, optional): Optional arguments to pass to the application.
"""

# Example usage placeholder (optional, but good practice for testing)
if __name__ == '__main__':
    print("\n--- Testing open_app Skill ---")
    
    # 1. Test Case: Opening a common app (Requires manual setup/testing on target OS)
    print("\n[Test 1: Attempting to open Calculator (or equivalent)]")
    result = execute(app_name="notepad" if platform.system() == "Windows" else "Calculator", arguments=None)
    print("Result:", result)

    # 2. Test Case: Opening an app with arguments (e.g., opening a specific URL in browser)
    if platform.system() != "Windows": # Windows 'start' handling for URLs is complex, skipping advanced arg test for simplicity here
        print("\n[Test 2: Attempting to open Google Chrome with a dummy argument]")
        # Note: Replace 'google-chrome' with the actual command name on your system if needed.
        result = execute(app_name="google-chrome", arguments=["https://www.google.com"])
        print("Result:", result)

    # 3. Test Case: Missing parameter test
    print("\n[Test 3: Testing missing app_name]")
    result = execute(arguments=["test"])
    print("Result:", result)