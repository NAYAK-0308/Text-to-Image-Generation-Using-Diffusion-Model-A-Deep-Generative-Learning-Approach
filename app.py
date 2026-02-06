import os
from flask import Flask, render_template, request, send_from_directory
from PIL import Image
import numpy as np
from pipeline import generate  # Assuming your generate function is in pipeline.py

app = Flask(__name__)

# Create the output directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    # Get the prompt from the form
    prompt = request.form.get('prompt')
    if not prompt:
        return "Please provide a prompt", 400

    # Generate the image using the generate function from pipeline.py
    try:
        output_image = generate(prompt=prompt, device='cpu')  # Use 'cpu' if no GPU is available

        # Convert the generated image to a PIL image and save it
        image_filename = 'generated_image.png'
        image_path = os.path.join('output', image_filename)
        output_image.save(image_path)

        # Display the image
        output_image.show()

        # Return the generated image in the output folder
        return send_from_directory('output', image_filename)

    except Exception as e:
        return f"Error generating image: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
