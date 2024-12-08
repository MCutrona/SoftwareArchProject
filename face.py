# use haarcascades to detect cars
# Import the OpenCV library
import cv2
from datetime import datetime
import time

# Load the pre-trained Haar Cascade model for car detection
car_cascade = cv2.CascadeClassifier('cars.xml')

# Open a connection to the first camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

# Start an infinite loop to continuously capture frames from the camera every minute

# Set the time interval for capturing frames (in seconds)
time_interval = 10

while True:
    # Capture a single frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars in the frame
    cars = car_cascade.detectMultiScale(gray, 1.3, 5)

    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Get the center of the frame
    center_x = width // 2
    center_y = height // 2

    # []'Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']
    quads = [False, False, False, False]

    # Draw a rectangle around the detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Detect what quadrent the cars are in

        # Get the center of the car
        car_x = x + w // 2
        car_y = y + h // 2

        # Determine the quadrant of the car
        if car_x < center_x and car_y < center_y:
            quads[0] = True
        elif car_x >= center_x and car_y < center_y:
            quads[1] = True
        elif car_x < center_x and car_y >= center_y:
            quads[2] = True
        else:
            quads[3] = True

    # Save the image to the 'images' folder with the timestamp as the name
    # Get the current time and format it as a string
    timestamp = datetime.now().strftime('%m-%d-%y_%H-%M-%S')
    cv2.imwrite(f'images/{timestamp}.jpg', frame)

    # add the image time and the number of cars detected to log.txt file
    with open('images/log.txt', 'a') as f:
        f.write(f'{timestamp}\t{quads[0]}\t{quads[1]}\t{quads[2]}\t{quads[3]}\n')

    # Display the captured frame in a window named 'frame' Good for debugging
    # cv2.imshow('frame', frame)

    # Wait for a key press and check if the key is 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    time.sleep(time_interval)

# Release the camera resource
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()