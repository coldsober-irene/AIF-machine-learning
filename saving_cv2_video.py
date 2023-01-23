import cv2

# define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# capture frames from a camera or load them from a file
for i in range(100):
    ret, frame = cap.read()
    if ret == True:
        # write the frame to the output video file
        out.write(frame)
    else:
        break

# release the VideoWriter object
out.release()
