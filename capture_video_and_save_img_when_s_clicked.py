import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)
while True:
    # Capture a frame from the video
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("Live Video", frame)

    # Check if the 's' key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        # Save the image
        cv2.imwrite("captured_image.jpg", frame)
        print("Image saved!")

    # Check if the 'q' key is pressed
    if key == ord("q"):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()
