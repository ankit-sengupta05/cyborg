import time
import logging
from typing import List, Dict, Any

try:
    import pyautogui
except ImportError:
    print("Warning: pyautogui not installed. Keystroke simulation will be limited.")
    pyautogui = None

# --- Setup Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def simulate_keystroke_sequence(**kwargs: Any) -> Dict[str, Any]:
    """
    Skill: sim_keystrokes
    Description: Simulates a sequence of keystrokes and mouse actions for GUI automation.
    Category: automation
    Usage: sim_keystrokes(actions: List[Dict], delay: float = 0.1)
    Parameters:
        actions (list): A list of dictionaries, where each dict defines an action.
            Example structure: [{'type': 'type', 'text': 'hello'}, {'type': 'press', 'key': 'enter'}]
        delay (float): The delay in seconds to wait between actions. Defaults to 0.1s.
    Returns:
        A dictionary containing the status of the execution.
    """
    logging.info("--- Starting Keystroke Simulation ---")

    if not kwargs.get('actions') or not isinstance(kwargs['actions'], list):
        logging.error("Missing or invalid 'actions' parameter. Must be a non-empty list.")
        return {"status": "failure", "message": "The 'actions' argument is required and must be a list."}

    actions: List[Dict] = kwargs['actions']
    delay: float = kwargs.get('delay', 0.1)

    if pyautogui is None:
        logging.warning("PyAutoGUI is not available. Simulation will only log actions without executing them.")
        return {"status": "warning", "message": "pyautogui not found. Actions were logged but not executed."}


    try:
        # Safety check for PyAutoGUI (optional, but good practice)
        logging.info("Moving mouse to a safe starting point...")
        pyautogui.moveTo(100, 100, duration=0.5) # Move to a known spot first

        for i, action in enumerate(actions):
            action_type = action.get('type', '').lower()
            logging.info(f"Executing Step {i+1}/{len(actions)}: Type={action_type}")

            try:
                if action_type == 'type':
                    text = action.get('text')
                    if text:
                        logging.info(f"Simulating typing of: '{text}'")
                        pyautogui.write(text, interval=0.05) # Use a small interval for realistic typing
                    else:
                        logging.warning("Type action found without 'text'. Skipping.")

                elif action_type == 'press':
                    key = action.get('key')
                    if key:
                        logging.info(f"Simulating pressing and releasing key: '{key}'")
                        pyautogui.press(key)
                    else:
                        logging.warning("Press action found without 'key'. Skipping.")

                elif action_type == 'click':
                    # Assuming click implies a mouse position was set previously or is the target area
                    x = action.get('x')
                    y = action.get('y')
                    if x is not None and y is not None:
                        logging.info(f"Simulating mouse click at coordinates ({x}, {y})")
                        pyautogui.click(x, y)
                    else:
                        logging.warning("Click action found without 'x' or 'y' coordinates. Skipping.")

                elif action_type == 'write':
                    # Alias for typing, useful if the user inputs it differently
                    text = action.get('text')
                    if text:
                        logging.info(f"Simulating writing of: '{text}'")
                        pyautogui.write(text, interval=0.05)

                else:
                    logging.warning(f"Unknown action type encountered: {action_type}. Skipping this step.")

            except pyautogui.FailSafeException:
                logging.error("PyAutoGUI Fail-safe triggered (mouse moved to corner). Stopping execution immediately.")
                return {"status": "failure", "message": "Execution halted by user safety mechanism."}
            except Exception as e:
                logging.error(f"Error during action '{action_type}': {e}")

            # Wait delay between actions, unless it's the last one
            if i < len(actions) - 1:
                time.sleep(delay)

        logging.info("--- Keystroke Simulation Completed Successfully ---")
        return {"status": "success", "message": f"Successfully executed {len(actions)} actions."}

    except Exception as e:
        logging.critical(f"A critical error occurred during the overall simulation process: {e}")
        return {"status": "failure", "message": f"Critical failure during execution: {str(e)}"}


# --- Example Usage (Demonstration purposes only) ---
if __name__ == '__main__':
    print("\n=========================================================")
    print("!!! WARNING !!!")
    print("This script requires pyautogui to run live GUI automation.")
    print("Run this in an environment where you can see the mouse cursor.")
    print("Press Ctrl+C or move mouse to a corner to stop early.")
    print("=========================================================\n")

    # 1. Example: Typing a message and pressing Enter (Simulating form submission)
    typing_actions = [
        {'type': 'click', 'x': 500, 'y': 300}, # Click into a text field first
        {'type': 'type', 'text': 'Hello World! This is an automated test.'},
        {'type': 'press', 'key': 'enter'}
    ]

    print("--- Running Test Case 1: Type and Enter ---")
    result1 = simulate_keystroke_sequence(actions=typing_actions, delay=0.5)
    print("Result 1:", result1)

    time.sleep(2) # Wait for user to observe the result before next test

    # 2. Example: A sequence of clicks and key presses (Simulating navigation)
    navigation_actions = [
        {'type': 'click', 'x': 100, 'y': 50},  # Click a button
        {'type': 'press', 'key': 'tab'},      # Move focus
        {'type': 'write', 'text': 'Search Query'}, # Type into the new field
        {'type': 'press', 'key': 'enter'}   # Submit search
    ]

    print("\n--- Running Test Case 2: Click, Tab, Type, Enter ---")
    result2 = simulate_keystroke_sequence(actions=navigation_actions, delay=0.5)
    print("Result 2:", result2)