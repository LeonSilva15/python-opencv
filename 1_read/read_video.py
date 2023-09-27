import cv2

# Use cv2.VideoCapture to read the file
cap = cv2.VideoCapture("../../resources/sample.mp4")

# We need a loop in order to read every frame in the file
while True:
    # cap.read returns a success flag and the captured frame
    success, img = cap.read()
    # Display the frame if captured
    # This will avoid throwing an error when finishing reading the file
    if success:
        cv2.imshow("Video", img)
    # wait 50 milliseconds before displaying the next frame
    # if the user presses q exit the loop
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
        
# As a good practice release the capture
# and destroy all the windows
cap.release()
cv2.destroyAllWindows()