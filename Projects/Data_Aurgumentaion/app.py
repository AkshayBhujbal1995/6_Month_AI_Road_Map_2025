import streamlit as st
import os
import random
import zipfile
import shutil
from io import BytesIO
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
from PIL import Image
import numpy as np
import base64
from datetime import datetime

# ========= CUSTOM STYLING =========
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/avif;base64,{b64}");
            background-size: cover;
            background-position: center;
            color: white;
        }}
        /* Force all labels and headers to white */
        .stSelectbox label, .stNumberInput label, .stFileUploader label, .stMarkdown, .stText {{
            color: white !important;
            font-weight: bold !important;
        }}
        /*  Style normal buttons */
        .stButton button {{
            background: rgba(255, 255, 255, 0.15);
            color: white;
            border: 2px solid #fff;
            border-radius: 12px;
            padding: 0.6em 1.2em;
            font-size: 16px;
            box-shadow: 0px 4px 20px rgba(255, 255, 255, 0.4);
            transition: all 0.3s ease;
        }}
        .stButton button:hover {{
            background: rgba(255, 255, 255, 0.3);
            box-shadow: 0px 6px 25px rgba(255, 255, 255, 0.7);
        }}
        /*  Make Download Button same as other buttons */
        .stDownloadButton button {{
            background: rgba(255, 255, 255, 0.15);
            color: white;
            border: 2px solid #fff;
            border-radius: 12px;
            padding: 0.6em 1.2em;
            font-size: 16px;
            box-shadow: 0px 4px 20px rgba(255, 255, 255, 0.4);
            transition: all 0.3s ease;
        }}
        .stDownloadButton button:hover {{
            background: rgba(255, 255, 255, 0.3);
            box-shadow: 0px 6px 25px rgba(255, 255, 255, 0.7);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background
set_background("bg.avif")

# ========= APP =========
st.title(" Data Augmentation Demo")
st.write("Upload images, choose a fill_mode, number of images, and generate augmented samples.")

# Session state for results
if "generated" not in st.session_state:
    st.session_state.generated = False
    st.session_state.output_dir = None
    st.session_state.all_results = []

# Upload
uploaded_files = st.file_uploader("Upload images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Options
mode = st.selectbox("Choose fill_mode", ["nearest", "reflect", "wrap", "constant", "mix"])
num_images = st.number_input("How many images to generate per mode?", min_value=1, max_value=50, value=5, step=1)

# Augmentation function
def augment_and_save(images, fill_mode, num_samples, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    results = []
    for idx, img in enumerate(images):
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)

        datagen = ImageDataGenerator(
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode=fill_mode
        )

        i = 0
        for batch in datagen.flow(x, batch_size=1):
            new_img = Image.fromarray(batch[0].astype("uint8"))
            file_name = f"{fill_mode}_img_{idx}_{i}.jpg"
            save_path = os.path.join(output_dir, file_name)
            new_img.save(save_path)
            new_img.close()  #  Ensure file is closed
            results.append(save_path)
            i += 1
            if i >= num_samples:
                break
    return results

# Generate button
if st.button("Generate Augmented Images"):
    if uploaded_files:
        images = [Image.open(file).convert("RGB") for file in uploaded_files]

        # Unique timestamped output dir
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_dir = f"augmented_{mode}_{timestamp}"
        os.makedirs(output_dir, exist_ok=True)

        all_results = []
        if mode != "mix":
            results = augment_and_save(images, mode, num_images, output_dir)
            all_results.extend(results)
        else:
            for m in ["nearest", "reflect", "wrap", "constant"]:
                subdir = os.path.join(output_dir, m)
                results = augment_and_save(images, m, num_images, subdir)
                all_results.extend(results)

        st.session_state.generated = True
        st.session_state.output_dir = output_dir
        st.session_state.all_results = all_results

        st.success(f"Generated {len(all_results)} images in folder: {output_dir}")

        # Show first 8 images
        sample_imgs = [Image.open(p) for p in all_results[:8]]
        st.image(sample_imgs, width=150, caption=[f"Sample {i}" for i in range(len(sample_imgs))])

    else:
        st.warning("Please upload at least one image first!")

#  Show Download & Clear only after generation
if st.session_state.generated:
    st.subheader("Next Actions")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Clear"):
            if st.session_state.output_dir and os.path.exists(st.session_state.output_dir):
                shutil.rmtree(st.session_state.output_dir, ignore_errors=True)
            st.session_state.generated = False
            st.session_state.output_dir = None
            st.session_state.all_results = []
            st.info("Cleared generated images.")

    with col2:
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zipf:
            for root, _, files in os.walk(st.session_state.output_dir):
                for file in files:
                    filepath = os.path.join(root, file)
                    zipf.write(filepath, os.path.relpath(filepath, st.session_state.output_dir))
        zip_buffer.seek(0)

        st.download_button(
            label="Download ZIP",
            data=zip_buffer,
            file_name=f"{st.session_state.output_dir}.zip",
            mime="application/zip"
        )
