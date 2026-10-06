from flask import Flask, render_template, request, send_from_directory
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import os


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"


# ---------------------------------------
# Load BLIP model
# ---------------------------------------

print("Loading BLIP model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("BLIP model loaded successfully.")


# ---------------------------------------
# Home page
# ---------------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    caption = None
    image_path = None
    error = None

    if request.method == "POST":

        if "image" not in request.files:
            error = "Please select an image."

        else:

            image = request.files["image"]

            if image.filename == "":
                error = "Please select an image."

            else:

                try:

                    # Create uploads folder
                    os.makedirs("uploads", exist_ok=True)

                    # Save uploaded image
                    saved_path = os.path.join(
                        "uploads",
                        image.filename
                    )

                    image.save(saved_path)

                    image_path = image.filename

                    # Open image
                    img = Image.open(
                        saved_path
                    ).convert("RGB")

                    # Process image
                    inputs = processor(
                        images=img,
                        return_tensors="pt"
                    )

                    # Generate caption
                    with torch.no_grad():

                        output = model.generate(
                            **inputs,
                            max_new_tokens=30
                        )

                    # Convert output to text
                    caption = processor.decode(
                        output[0],
                        skip_special_tokens=True
                    )

                except Exception as e:

                    error = str(e)


    return render_template(
        "index.html",
        caption=caption,
        image_path=image_path,
        error=error
    )

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory("uploads", filename)
# ---------------------------------------
# Start application
# ---------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )
