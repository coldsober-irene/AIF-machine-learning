import cv2

# define the codec and create a VideoWriter object
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# capture frames from a camera or load them from a file
while True:
    success, frame = cap.read()
    if success:
        out.write(frame)

# release the VideoWriter object
out.release()
