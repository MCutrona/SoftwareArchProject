# Import the OpenCV library
import cv2
from datetime import datetime

# Load the pre-trained Haar Cascade model for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open a connection to the first camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

def save_image():
    # Save the image to the 'Demo' folder with the timestamp as the name
    # Get the current time and format it as a string
    timestamp = datetime.now().strftime('%m-%d-%y_%H-%M-%S')
    cv2.imwrite(f'Demo/{timestamp}.jpg', frame)

    # Add the data to the log file
    # add the image time and the number of faces detected to log.txt file
    with open('Demo/log.txt', 'a') as f:
        f.write(f'{timestamp}\t{quads[0]}\t{quads[1]}\t{quads[2]}\t{quads[3]}\n')



# Start an infinite loop to continuously capture frames from the camera
while True:
    # Capture a single frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Get the center of the frame
    center_x = width // 2
    center_y = height // 2

    # ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']
    quads = [False, False, False, False]

    # Draw a rectangle around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Detect what quadrent the faces are in
        # Get the center of the face
        face_x = x + w // 2
        face_y = y + h // 2

        # Determine the quadrant of the face
        if face_x < center_x and face_y < center_y:
            quads[0] = True
        elif face_x >= center_x and face_y < center_y:
            quads[1] = True
        elif face_x < center_x and face_y >= center_y:
            quads[2] = True
        else:
            quads[3] = True
    
    # Display the captured frame in a window named 'frame'
    cv2.imshow('frame', frame)

    # Save the image if the 's' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        save_image()

    # Check if the 'q' key is pressed; if so, break the loop and exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera resource
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
