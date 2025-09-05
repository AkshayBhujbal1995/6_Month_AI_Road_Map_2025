import streamlit as st
import cv2
import numpy as np
import imutils
from imutils.object_detection import non_max_suppression
from PIL import Image
import tempfile

st.set_page_config(page_title="Pedestrian Detection", layout="wide")

# ---------------- Custom CSS ----------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    h1, h2, h3 {
        color: #00c4cc;
    }
    .stButton>button {
        background-color: #1f2937;
        color: #00c4cc;
        border: 1px solid #00c4cc;
        border-radius: 6px;
        padding: 6px 16px;
    }
    .stButton>button:hover {
        background-color: #00c4cc;
        color: #0e1117;
    }
    /* Make uploader label text white */
    .stFileUploader label {
        color: white !important;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Pedestrian Detection")
st.write("Upload an image or video to detect pedestrians using OpenCV HOG + SVM.")

@st.cache_resource
def init_detector():
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    return hog

hog = init_detector()

def detect_people(frame_bgr):
    frame = imutils.resize(frame_bgr, width=800)
    rects, _ = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
    if len(rects) > 0:
        rects_np = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        picks = non_max_suppression(rects_np, probs=None, overlapThresh=0.65)
    else:
        picks = []
    for (xA, yA, xB, yB) in picks:
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

mode = st.radio("Choose Input Type", ["Image", "Video"])

if mode == "Image":
    uploaded_img = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if uploaded_img:
        image = Image.open(uploaded_img).convert("RGB")
        bgr = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        result = detect_people(bgr)
        st.image(result, channels="RGB", caption="Detected Pedestrians", use_container_width=True)

else:
    uploaded_vid = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])
    if uploaded_vid:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_vid.read())
        cap = cv2.VideoCapture(tfile.name)

        stframe = st.empty()
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            result = detect_people(frame)
            stframe.image(result, channels="RGB", use_container_width=True)
        cap.release()
