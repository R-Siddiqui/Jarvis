import requests
import base64
from typing import Tuple, Optional
import os
from jarvis import *
from dotenv import load_dotenv; load_dotenv() # Load environment variables from .env file

def generate(prompt: str, seed: int=1800647681, width: int=1024, height: int=576, steps: int=4, enhance: bool=True, safety_filter: bool=True, image_path: str="C:\\Users\\rihan\\OneDrive\\Pictures\\dump\\img.jpeg") -> Tuple[bool, Optional[str]]:
    """
    Generates an image based on the given parameters and saves it to a file.

    Parameters:
    - prompt (str): Description of the image to generate.
    - seed (int): Seed for the image generation process.
    - width (int): Width of the generated image.
    - height (int): Height of the generated image.
    - steps (int): Number of steps for the image generation process. More the Steps More Clear and Realistic Image 
    - enhance (bool): Whether to enhance the image quality.
    - safety_filter (bool): Whether to apply a safety filter to the image.

    - For Square Image Size: 768x768
    - For Portrait Image Size: 1024x576
    - For Landscape Image Size: 576x1024

    Returns:
    - Tuple[bool, Optional[str]]: A tuple containing a boolean indicating the success of the API call,
      and an optional string with the file path where the image is saved if successful.
    """

    # Define the URL and headers for the API call
    url = "https://turbo.decohere.ai/generate/turbo"
    headers = {
        "Authorization": f"Bearer {os.environ.get('DECOHERE_AI')}",
    }

    # Define the payload for the POST request
    payload = {
        "prompt": prompt,
        "seed": seed,
        "width": width,
        "height": height, 
        "steps": steps,
        "enhance": enhance,
        "safety_filter": safety_filter,
    }

    # Make the POST request to the API
    response = requests.post(url, headers=headers, json=payload)

    # Check the response status code
    if response.status_code == 200:
        # Extract base64 encoded image data
        base64_image_data = response.json().get('image', '')
        # Decode base64 encoded image data to bytes
        image_bytes = base64.b64decode(base64_image_data)
        # Write the bytes to a file as an image
        with open(image_path, "wb") as image_file:
            image_file.write(image_bytes)
        return True, image_path
    else:
        print(f"API call failed with status code {response.status_code}")
        return False, response.text
    
# Example usage:
if __name__ == "__main__":
    prompt = takecommand().lower()



    success, file_path = generate(prompt)
    if success: print(f"Image saved at {file_path}")
    else: print("Failed to generate the image.")