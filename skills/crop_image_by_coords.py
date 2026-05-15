import logging
from typing import Dict, Any

try:
    import pyautogui
except ImportError:
    print("Warning: pyautogui not found. Image automation features will be disabled.")
    pyautogui = None

# --- Configuration and Setup ---

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def execute(**kwargs: Any) -> Dict[str, str]:
    """
    Main entry point for the crop_image_by_coordinates skill.

    This function crops an image based on coordinates provided in the keyword arguments.
    It is designed to be generic and reusable for any coordinate-based cropping task.

    Args:
        **kwargs: A dictionary expected to contain at least 'source_image_path' (str),
                   and bounding box coordinates: 'left', 'top', 'width', 'height' (int).

    Returns:
        A dictionary containing the status message and potentially a path to the cropped image.
    """
    logging.info("--- Starting crop_image_by_coordinates skill execution ---")

    # 1. Validate Required Parameters
    required_keys = ['source_image_path', 'left', 'top', 'width', 'height']
    missing_keys = [key for key in required_keys if key not in kwargs]

    if missing_keys:
        error_msg = f"Missing required arguments for cropping. Please provide: {', '.join(required_keys)}."
        logging.error(error_msg)
        return {"status": "failure", "message": error_msg}

    try:
        # Extract parameters with type checking/casting
        source_image_path = str(kwargs['source_image_path'])
        left = int(kwargs['left'])
        top = int(kwargs['top'])
        width = int(kwargs['width'])
        height = int(kwargs['height'])

    except (ValueError, TypeError) as e:
        error_msg = f"Invalid data type provided for coordinates or path. Ensure left, top, width, and height are integers, and source_image_path is a string. Error: {e}"
        logging.error(error_msg)
        return {"status": "failure", "message": error_msg}

    # 2. Core Logic Execution (Using Pillow/PIL for robust image manipulation if available, otherwise pyautogui fallback)
    try:
        from PIL import Image
        img = Image.open(source_image_path)
        logging.info(f"Successfully opened source image: {source_image_path}")

        # Define the bounding box (left, top, right, bottom) required by Pillow
        right = left + width
        bottom = top + height
        crop_box = (left, top, right, bottom)

        # Perform the crop operation
        cropped_img = img.crop(crop_box)

        # 3. Saving the Result (Making it reusable by allowing an output path override)
        output_path = kwargs.get('output_image_path', 'cropped_output.png')
        if not output_path:
             output_path = f"cropped_{logging.getLogger().name}_{hash(source_image_path)}.png"

        # Save the cropped image
        cropped_img.save(output_path)

        result_message = (f"Image successfully cropped from {source_image_path} "
                          f"using coordinates ({left}, {top}) to ({right}, {bottom}). "
                          f"Saved result to: {output_path}")
        logging.info(result_message)
        return {"status": "success", "message": result_message, "cropped_image_path": output_path}

    except ImportError:
        # Fallback if PIL is not installed (though the prompt implies standard libs + pyautogui)
        error_msg = "Pillow (PIL) library is required for robust image cropping. Please install it (`pip install Pillow`)."
        logging.warning(error_msg)
        return {"status": "failure", "message": error_msg}

    except FileNotFoundError:
        error_msg = f"The source image file was not found at the specified path: {source_image_path}"
        logging.error(error_msg)
        return {"status": "failure", "message": error_msg}

    except Exception as e:
        # Catch-all for other potential errors (e.g., invalid dimensions, permission issues)
        error_msg = f"An unexpected error occurred during image processing: {type(e).__name__} - {str(e)}"
        logging.error(error_msg)
        return {"status": "failure", "message": error_msg}

# --- Skill Metadata (As required by the prompt structure, though not executable code) ---
"""
Skill: crop_image_by_coords
Description: Crops an image file based on user-specified pixel coordinates.
Category: automation
Usage: crop_image_by_coords(**kwargs)
Parameters: 
    source_image_path (str): The absolute or relative path to the image file to be cropped.
    left (int): The starting X coordinate of the desired crop area.
    top (int): The starting Y coordinate of the desired crop area.
    width (int): The width of the desired crop area in pixels.
    height (int): The height of the desired crop area in pixels.
    output_image_path (str, optional): Where to save the resulting cropped image. Defaults to 'cropped_output.png'.
"""