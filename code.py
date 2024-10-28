
import requests
import json

# Replace with your Hugging Face API token
HF_API_TOKEN = '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'


# Set up headers with authorization
headers = {
    'Authorization': f'Bearer {HF_API_TOKEN}',
    'Content-Type': 'application/json'
}

# Define the prompt you want to generate an image for
prompt = "Blue sky with red clouds and eagles flying"

# Make a request to the Hugging Face text-to-image endpoint
response = requests.post(
    "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
    headers=headers,
    json={"inputs": prompt}
)

# Check for a successful response
if response.status_code == 200:
    # Get the image content
    image_bytes = response.content
    # Save the image to a file
    with open("generated_image.png", "wb") as f:
        f.write(image_bytes)
    print("Image generated and saved as 'generated_image.png'")
else:
    print(f"Failed to generate image: {response.status_code} - {response.text}")
