# cannot ssh into the pi from visual studio code so I am using the terminal on the pi to run the code
# To ssh into the pi run ssh mcutrona@<IPAddress> and enter the password: mcutrona IP Address: 10.0.0.245
# Write the file on the local machine and run in local terminal scp "<FilePath>" mcutrona@<IPAddress>:~/Code
# Start the python environement source .venv/bin/activate
# to copy files back to local machine to view the results run scp -r mcutrona@<IPAddress>:~/Code/images/ <LocalFilePath>
# Haar classifier https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html
# path to .so file /usr/local/lib/python3.11/dist-packages/cv2/python-3.11/cv2.cpython-311-arm-linux-gnueabihf.so
# command ln -s /usr/local/lib/python3.11/dist-packages/cv2/python-3.11/cv2.cpython-311-arm-linux-gnueabihf.so ~/.venv/lib/python3.*/site-packages/cv2.so


# Import the OpenCV library
import cv2

# Open a connection to the first camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

# Start an infinite loop to continuously capture frames from the camera
while True:
    # Capture a single frame from the camera
    ret, frame = cap.read()
    
    # Display the captured frame in a window named 'frame'
    cv2.imshow('frame', frame)

    # Check if the 'q' key is pressed; if so, break the loop and exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera resource
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
