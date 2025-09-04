import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam")

# Define HSV ranges for multiple colors
color_ranges = {
    "Red": ([0, 120, 70], [10, 255, 255]),
    "Dark Red": ([170, 120, 70], [180, 255, 255]),
    "Green": ([36, 25, 25], [86, 255, 255]),
    "Light Blue": ([90, 50, 50], [110, 255, 255]),
    "Dark Blue": ([111, 84, 46], [131, 255, 255]),
    "Yellow": ([20, 100, 100], [30, 255, 255]),
    "Orange": ([10, 100, 20], [25, 255, 255]),
    "Purple": ([129, 50, 70], [158, 255, 255]),
    "Pink": ([160, 50, 70], [170, 255, 255])
}

# Map color names to BGR values (for bounding box colors)
color_bgr = {
    "Red": (0, 0, 255),
    "Dark Red": (0, 0, 200),
    "Green": (0, 255, 0),
    "Light Blue": (255, 200, 100),
    "Dark Blue": (200, 100, 50),
    "Yellow": (0, 255, 255),
    "Orange": (0, 165, 255),
    "Purple": (128, 0, 128),
    "Pink": (180, 105, 255)
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, (lower, upper) in color_ranges.items():
        lower_np = np.array(lower)
        upper_np = np.array(upper)

        # Create mask for each color
        mask = cv2.inRange(hsv, lower_np, upper_np)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 1000:  # Ignore small noise
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color_bgr[color_name], 3)
                cv2.putText(frame, color_name, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color_bgr[color_name], 2, cv2.LINE_AA)

    # Show original frame with colored bounding boxes
    cv2.imshow("Color Detection", frame)

    # Exit on Esc key
    if cv2.waitKey(1) & 0xFF == 27:  # 27 = Esc
        break

cap.release()
cv2.destroyAllWindows()
