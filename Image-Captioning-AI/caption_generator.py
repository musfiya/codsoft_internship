from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import os


# ---------------------------------------
# Load the pretrained image-captioning model
# ---------------------------------------

print("Loading image captioning model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("Model loaded successfully.")


# ---------------------------------------
# Ask the user for an image
# ---------------------------------------

image_path = input("\nEnter the path of the image: ").strip().strip('"')


# ---------------------------------------
# Check whether the image exists
# ---------------------------------------

if not os.path.exists(image_path):

    print("\nError: Image file not found.")
    print("Please check the image path and try again.")

else:

    try:

        # Load and convert image to RGB
        image = Image.open(image_path).convert("RGB")

        print("\nImage loaded successfully.")
        print("Generating caption...")


        # Convert image into the format
        # the BLIP model understands
        inputs = processor(
            images=image,
            return_tensors="pt"
        )


        # Generate caption
        with torch.no_grad():

            output = model.generate(
                **inputs,
                max_new_tokens=30
            )


        # Convert model output into normal text
        caption = processor.decode(
            output[0],
            skip_special_tokens=True
        )


        # ---------------------------------------
        # Display result
        # ---------------------------------------

        print("\n==============================")
        print("       GENERATED CAPTION")
        print("==============================")

        print(caption)

        print("==============================\n")


    except Exception as error:

        print("\nUnable to process the image.")
        print("Error:", error)

