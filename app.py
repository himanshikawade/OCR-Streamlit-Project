import cv2
import time
import numpy as np
import pymysql
import streamlit as st
from keras.models import load_model
from PIL import Image
from datetime import datetime

# Load OCR model
@st.cache_resource
def load_ocr_model():
    return load_model("model/ocr_model.h5")

ocr_model = load_ocr_model()

# Database connection helper
def get_database_connection():
    try:
        connection = pymysql.connect(
            host="localhost",  # Replace with your XAMPP host if different
            user="root",       # Default XAMPP user
            password="12345",       # Default password
            database="ocr",
              
        )
        return connection
    except pymysql.MySQLError as e:
        st.error(f"Error connecting to the database: {e}")
        return None

# Save detected variable to the database
def save_to_database(variable_text):
    connection = get_database_connection()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO detected_variables (variable_text) VALUES (%s)"
                cursor.execute(sql, (variable_text,))
                connection.commit()
                st.info(f"Successfully saved to database: {variable_text}")
        except pymysql.MySQLError as e:
            st.error(f"Error inserting into database: {e}")
        finally:
            connection.close()
    else:
        st.error("Database connection failed. Data not saved.")

# Function to process frame with OCR model
def process_frame(frame):
    # Convert the frame to grayscale (1 channel)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Resize the image to the expected size of (28, 28)
    img_resized = cv2.resize(gray_frame, (28, 28))  # Adjust to model's expected input size
    
    # Normalize pixel values to [0, 1]
    img_normalized = img_resized / 255.0
    
    # Add batch dimension and channel dimension (1, 28, 28, 1)
    img_array = np.expand_dims(img_normalized, axis=(0, -1))
    
    # Make predictions using the OCR model
    predictions = ocr_model.predict(img_array)
    
    # Convert predictions to the desired output format
    detected_text = np.argmax(predictions)  # This assumes that your model outputs class probabilities
    
    return str(detected_text)





# Streamlit UI
st.title("Live OCR with Streamlit")
st.markdown("This app captures live video feed from an RTSP connection and detects variables every 30 seconds.")

# Start RTSP video feed
RTSP_URL = "rtsp://192.168.1.200/live/ch00_0"  # Replace with your RTSP stream URL
video_capture = cv2.VideoCapture(RTSP_URL)

if not video_capture.isOpened():
    st.error("Could not access the RTSP stream. Ensure the URL is correct and reachable.")
else:
    FRAME_INTERVAL = 10  # seconds
    last_captured_time = time.time()

    stframe = st.empty()  # Placeholder for video stream

    # Place the stop button outside the loop
    stop_button = st.button("Stop Stream")  # Unique button placed once

    while not stop_button:  # Check the state of the button
        ret, frame = video_capture.read()
        if not ret:
            st.error("Failed to read from the RTSP stream.")
            break

        # Display video frame
        stframe.image(frame, channels="BGR")

        # Capture and process frame every FRAME_INTERVAL seconds
        current_time = time.time()
        if current_time - last_captured_time >= FRAME_INTERVAL:
            last_captured_time = current_time

            # Process frame through OCR
            detected_text = process_frame(frame)
            st.success(f"Detected Text: {detected_text}")

            # Save detected text to the database
            save_to_database(detected_text)

    video_capture.release()
    cv2.destroyAllWindows()