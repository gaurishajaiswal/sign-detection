import cv2

def capture_image(camera_index=0, save_path='captured_image.jpg'):
    # Open the camera
    cap = cv2.VideoCapture(camera_index)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a single frame
    ret, frame = cap.read()

    # Check if the frame is captured successfully
    if not ret:
        print("Error: Could not capture frame.")
        cap.release()
        return

  
    cv2.imwrite(save_path, frame)

    cap.release()

    print(f"Image captured and saved as {save_path}")

if _name_ == "_main_":
    # You can specify the camera index (use 0 for the default camera)
    camera_index = 0

    # You can specify the path where you want to save the captured image
    save_path = 'captured_image.jpg'

    # Capture the image
    capture_image(camera_index, save_path)
