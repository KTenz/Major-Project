import cv2
import numpy as np

# Initialize the camera objects
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
#
# # Set the camera resolution
# cap1.set(3, 640)
# cap1.set(4, 480)
# cap2.set(3, 640)
# cap2.set(4, 480)

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # Flip the frames horizontally for a mirror effect
    frame1 = cv2.flip(frame1, 1)


    frame2 = cv2.flip(frame2, 1)

    # Merge the frames horizontally
    merged_frame = np.hstack((frame1, frame2))

    # Display the merged frame
    cv2.imshow('Merged Camera Views', merged_frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera objects and destroy the OpenCV window
cap1.release()
cap2.release()
cv2.destroyAllWindows()