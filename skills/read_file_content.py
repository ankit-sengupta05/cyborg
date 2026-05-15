import logging
import os

# Setup basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def execute(**kwargs):
    """
    Skill: read_file_content
    Description: Reads the content of a file given its absolute or relative path.
    Category: automation
    Usage: read_file_content(file_path: str, **kwargs)
    Parameters:
        file_path (str): The full or relative path to the file that needs to be read.
        **kwargs: Additional parameters can be passed for future extensions (e.g., encoding).
    """
    logging.info("Attempting to read file content...")

    # 1. Validate required arguments
    if 'file_path' not in kwargs or not isinstance(kwargs['file_path'], str):
        logging.error("Missing or invalid 'file_path'. Please provide the path as a string.")
        return {"status": "failure", "message": "File path is required."}

    file_path = kwargs['file_path']

    # 2. Check if the file exists before attempting to read (Best Practice)
    if not os.path.exists(file_path):
        logging.error(f"The specified file path does not exist: {file_path}")
        return {"status": "failure", "message": f"File not found at path: {file_path}"}

    # 3. Determine encoding (Use provided kwargs or default to UTF-8)
    encoding = kwargs.get('encoding', 'utf-8')
    logging.info(f"Attempting to read file with encoding: {encoding}")

    try:
        # Core logic: Opening and reading the file
        with open(file_path, 'r', encoding=encoding) as f:
            content = f.read()

        logging.info("Successfully read file content.")
        return {"status": "success", "content": content}

    except PermissionError:
        error_msg = f"Permission denied when trying to read the file at {file_path}. Check file permissions."
        logging.error(error_msg)
        return {"status": "failure", "message": error_msg}
    except UnicodeDecodeError as e:
        error_msg = f"Encoding error while reading {file_path}. The specified encoding '{encoding}' might be incorrect. Original Error: {e}"
        logging.warning(error_msg)
        return {"status": "failure", "message": error_msg}
    except IOError as e:
        # Catch other general I/O errors (e.g., file is a directory, path issues)
        error_msg = f"An unexpected I/O error occurred while reading {file_path}: {e}"
        logging.error(error_msg)
        return {"status": "failure", "message": error_msg}
    except Exception as e:
        # Catch all other unforeseen errors for robustness
        error_msg = f"An unexpected error occurred: {type(e).__name__} - {str(e)}"
        logging.critical(error_msg)
        return {"status": "failure", "message": f"An unknown error occurred: {str(e)}"}

# Example usage placeholder (not part of the required module structure, but useful for testing)
if __name__ == '__main__':
    print("--- Testing File Reader Skill ---")
    # To test this block, create a dummy file named 'test_input.txt' in the same directory.
    dummy_file_path = "test_input.txt"

    # Create a dummy file for testing purposes
    try:
        with open(dummy_file_path, 'w') as f:
            f.write("This is a test line.\n")
            f.write("It verifies the skill execution.")
        print(f"\n[SETUP] Created dummy file: {dummy_file_path}")

        # Test Case 1: Success
        result_success = execute(file_path=dummy_file_path)
        print("\n--- Test Case 1: Success ---")
        print(f"Result Status: {result_success.get('status')}")
        if result_success.get('status') == 'success':
            print("Content Snippet:", result_success['content'][:50] + "...")

        # Test Case 2: File Not Found
        result_fail_path = execute(file_path="non_existent_file.xyz")
        print("\n--- Test Case 2: File Not Found ---")
        print(f"Result Status: {result_fail_path.get('status')}")

        # Test Case 3: Encoding Error (Requires creating a file with non-UTF8 content, skipped for simplicity)
        # Test Case 4: Missing Argument
        result_missing = execute()
        print("\n--- Test Case 4: Missing Argument ---")
        print(f"Result Status: {result_missing.get('status')}")

    finally:
        # Cleanup the dummy file
        if os.path.exists(dummy_file_path):
            os.remove(dummy_file_path)
            print(f"\n[CLEANUP] Removed dummy file: {dummy_file_path}")