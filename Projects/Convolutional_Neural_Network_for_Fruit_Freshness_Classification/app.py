import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TF warnings

import tensorflow as tf
import numpy as np
import gradio as gr
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ================================
# 📌 Dummy Model Definition (Moved to top-level for scope)
# ================================
class DummyModel:
    def predict(self, img):
        logging.info("Using DummyModel for prediction.")
        # Simulate a prediction (ensure it's a 1D array of probabilities)
        # Example distribution for 6 classes
        probs = np.random.rand(6)
        return np.array([probs / probs.sum()]) # Normalize to sum to 1

# ================================
# 📌 Load Trained Model
# ================================
loaded_model = None # Initialize to None
try:
    loaded_model = tf.keras.models.load_model("fruit_cnn_model.h5")
    logging.info("Successfully loaded fruit_cnn_model.h5")
except Exception as e:
    logging.error(f"Error loading model: {e}. Falling back to DummyModel.")
    loaded_model = DummyModel() # Assign the dummy model if real model fails

# Class labels (without emojis)
labels = {
    0: "Fresh Apple",
    1: "Fresh Banana",
    2: "Fresh Orange",
    3: "Rotten Apple",
    4: "Rotten Banana",
    5: "Rotten Orange"
}

img_size = (150, 150)

# ================================
# 📌 Prediction Function
# ================================
def predict_image(img):
    logging.info(f"predict_image called with img type: {type(img)}")
    if img is None:
        logging.warning("No image provided to predict_image function.")
        return "<div class='result-box'>Please upload an image or use the webcam.</div>"

    try:
        # Ensure img is a numpy array.
        if not isinstance(img, np.ndarray):
            logging.error(f"Input image is not a numpy array. Type: {type(img)}")
            # Attempt conversion if it's a PIL Image or similar
            if hasattr(img, 'convert'): # Check if it's a PIL Image
                img = np.array(img.convert("RGB"))
            else:
                raise ValueError("Image input is not a numpy array or a recognizable image object.")


        # Check image shape and convert if necessary
        if img.ndim == 2: # Grayscale image
            img = np.stack([img, img, img], axis=-1) # Convert to 3 channel RGB
            logging.info("Converted 2D grayscale image to 3D RGB.")
        elif img.ndim == 3 and img.shape[-1] == 4: # RGBA image (often from webcam)
            img = img[:, :, :3] # Take only RGB channels
            logging.info("Converted 4-channel RGBA image to 3-channel RGB.")
        elif img.ndim == 3 and img.shape[-1] == 3: # Already RGB
            logging.info("Image is already 3-channel RGB.")
        else:
            raise ValueError(f"Unexpected image dimensions or channels: {img.shape}")

        # Now, ensure loaded_model is not None before proceeding.
        # This check is technically redundant if `loaded_model` is always assigned
        # either a real model or DummyModel, but good for clarity.
        if loaded_model is None:
             raise RuntimeError("Model was not loaded successfully and dummy model was not assigned.")


        if isinstance(loaded_model, DummyModel):
            prediction_array = loaded_model.predict(img)[0]
            logging.info("Dummy model predicted.")
        else:
            # Preprocessing for actual model
            img_tensor = tf.convert_to_tensor(img, dtype=tf.float32)
            img_tensor = tf.image.resize(img_tensor, img_size)
            img_tensor = img_tensor / 255.0 # Normalize
            img_tensor = np.expand_dims(img_tensor, axis=0) # Add batch dimension
            prediction_array = loaded_model.predict(img_tensor)[0]
            logging.info("Actual model predicted.")

        class_id = np.argmax(prediction_array)
        predicted_label = labels[class_id]
        confidence = float(prediction_array[class_id]) * 100 # Convert to percentage

        status_color = "#28a745" if "Fresh" in predicted_label else "#dc3545" # Green for Fresh, Red for Rotten
        
        html_output = f"""
        <div class='result-box' style='border-left: 8px solid {status_color};'>
            <div class='result-label'>{predicted_label}</div>
            <div class='result-confidence' style='color: {status_color};'>{confidence:.2f}% Confidence</div>
            <div class='result-detail'>
                Based on the image, the model predicts this fruit is 
                <span style='font-weight: bold; color: {status_color};'>{predicted_label}</span>.
            </div>
        </div>
        """
        logging.info(f"Prediction successful: {predicted_label} with {confidence:.2f}% confidence.")
        return html_output

    except Exception as e:
        logging.error(f"Error during prediction: {e}", exc_info=True)
        return f"<div class='result-box error-message'>Prediction Error: {e}<br>Please try again or check the image format.</div>"

# ================================
# 📌 Enhanced Gradio UI with Advanced CSS
# ================================
custom_css = """
/* Import Poppins font from Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

/* General Body and Background */
body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
    /* Richer, more complex animated gradient */
    background: linear-gradient(135deg,
                #FFD700 0%,     /* Gold */
                #FFA07A 25%,    /* Light Salmon */
                #FF6347 50%,    /* Tomato */
                #A200FF 75%,    /* Electric Purple */
                #00C9FF 100%    /* Bright Blue */
                );
    background-size: 600% 600%; /* Even larger for more dramatic shift */
    animation: gradientShift 20s ease infinite alternate; /* Slower, alternates direction */
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    100% { background-position: 100% 50%; }
}

/* Main Gradio Container Styling */
.gradio-container {
    max-width: 1100px; /* Slightly wider */
    margin: 50px auto;
    padding: 35px;
    border-radius: 25px; /* More rounded */
    background: rgba(255, 255, 255, 0.98); /* Almost opaque white */
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25); /* Deeper, more distinct shadow */
    backdrop-filter: blur(12px); /* Stronger frosted glass */
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.5s ease-in-out; /* Smooth transitions for container */
}

.gradio-container:hover {
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.35); /* Even more lift on hover */
}


/* Headers */
h1 {
    color: #FF6347; /* Tomato Red */
    text-align: center;
    font-size: 3.2em; /* Even larger heading */
    margin-bottom: 0.4em;
    font-weight: 800; /* Extra bold */
    text-shadow: 3px 3px 7px rgba(0,0,0,0.15); /* Stronger text shadow */
    letter-spacing: 1.5px; /* Slightly spaced letters */
}

h2 {
    color: #36454F; /* Charcoal Grey */
    text-align: center;
    font-size: 1.8em;
    margin-top: 0;
    font-weight: 600;
}

/* Markdown for descriptions */
.gr-markdown {
    text-align: center;
    color: #444;
    font-size: 1.15em;
    line-height: 1.7;
    margin-bottom: 2.5em;
    padding: 0 20px; /* Some padding for longer lines */
}

/* Custom styling for specific Gradio components - Buttons */
.gr-button {
    border: none;
    border-radius: 12px; /* More rounded buttons */
    padding: 15px 30px;
    font-size: 1.25em;
    font-weight: 700; /* Bold */
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1); /* Slower, smoother transition */
    text-transform: uppercase; /* Uppercase button text */
    letter-spacing: 0.8px;
    position: relative;
    overflow: hidden; /* For the "light effect" */
}

/* Specific button colors and glows */
.gr-button:nth-child(1) { /* First button (Predict) */
    background-color: #00C9FF; /* Bright Blue */
    color: #fff;
    box-shadow: 0 7px 20px rgba(0, 201, 255, 0.4);
}
.gr-button:nth-child(1):hover {
    background-color: #00B5E0; /* Darker blue */
    box-shadow: 0 10px 25px rgba(0, 201, 255, 0.6);
    transform: translateY(-3px);
}

/* Light effect on button hover */
.gr-button::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.2);
    transition: all 0.5s ease;
    transform: skewX(-20deg);
}
.gr-button:hover::after {
    left: 100%;
}


/* Styling for Input and Output areas (card-like) */
.gr-image, .gr-html-container { /* Target gr-html-container for the new output */
    background: rgba(255, 255, 255, 0.9);
    border-radius: 18px;
    padding: 25px;
    box-shadow: 0 7px 20px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(200, 200, 200, 0.6);
    transition: all 0.4s ease;
    min-height: 250px; /* Ensure a good height */
    display: flex;
    flex-direction: column;
    justify-content: center; /* Center content vertically */
    align-items: center; /* Center content horizontally */
}

.gr-image:hover, .gr-html-container:hover {
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
    transform: translateY(-3px);
}

/* Specific input image styling */
.gr-image img {
    border-radius: 15px; /* Slightly more rounded images */
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

/* Custom styling for the HTML prediction output */
.result-box {
    width: 100%;
    padding: 20px 30px;
    border-radius: 15px;
    background: #f9f9f9;
    box-shadow: inset 0 0 15px rgba(0,0,0,0.05); /* Inner shadow */
    text-align: center;
    line-height: 1.5;
    font-size: 1.1em;
    color: #333;
    max-width: 450px; /* Keep it neat */
}

.result-label {
    font-size: 2.2em;
    font-weight: 700;
    margin-bottom: 5px;
    text-transform: capitalize;
}

.result-confidence {
    font-size: 1.6em;
    font-weight: 600;
    margin-bottom: 15px;
}

.result-detail {
    font-size: 0.95em;
    color: #666;
}

.error-message {
    color: #dc3545; /* Red for error messages */
    font-weight: 600;
    border-left: 8px solid #dc3545 !important;
}

/* Gradio labels for input/output components */
.gr-image label, .gr-html-container label {
    font-size: 1.1em;
    font-weight: 600;
    color: #444;
    margin-bottom: 10px;
}


/* Footer (keeping it hidden) */
footer {
    visibility: hidden !important;
    height: 0 !important;
}

/* Responsive adjustments */
@media (max-width: 900px) {
    .gradio-container {
        margin: 20px;
        padding: 25px;
    }
    h1 {
        font-size: 2.5em;
    }
    .gr-markdown {
        font-size: 1em;
    }
    .gr-button {
        font-size: 1.1em;
        padding: 12px 25px;
    }
    .result-label {
        font-size: 1.8em;
    }
    .result-confidence {
        font-size: 1.3em;
    }
}

@media (max-width: 600px) {
    .gradio-container {
        margin: 15px;
        padding: 15px;
    }
    h1 {
        font-size: 2em;
    }
    .gr-button {
        font-size: 1em;
        padding: 10px 20px;
    }
    .gr-row { /* Stacks columns on small screens */
        flex-direction: column;
    }
    .gr-image, .gr-html-container {
        margin-bottom: 20px; /* Space between stacked elements */
    }
}
"""

with gr.Blocks(css=custom_css) as demo:

    gr.Markdown("""
    # Fresh vs Rotten Fruit Classifier  
    **Upload an image or use your webcam to check if a fruit is Fresh or Rotten.**  
    Built with **Convolutional Neural Networks (CNN)** | TensorFlow | Keras | Gradio  
    """)

    with gr.Row():
        with gr.Column(scale=1):
            input_img = gr.Image(
                type="numpy",
                label="Upload or Capture Fruit Image",
                sources=["upload", "webcam"],
                image_mode="RGB",
            )
            predict_btn = gr.Button("Predict Fruit Condition")
        with gr.Column(scale=1):
            output_html = gr.HTML(
                value="<div class='result-box'>Upload an image or use the webcam to see the prediction here!</div>",
                label="Prediction Result"
            )

    gr.Markdown("""
    ---
    ### Project Information  
    **Model:** Convolutional Neural Network (CNN)  
    **Dataset:** Kaggle – Fresh & Rotten Fruits  
    **Features:** Image Upload, Webcam Capture, Real-time Prediction  
    """)

    predict_btn.click(fn=predict_image, inputs=input_img, outputs=output_html)

# ================================
# 📌 Launch App
# ================================
if __name__ == "__main__":
    demo.launch()