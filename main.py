import cv2
import numpy as np

# Load image
planets = cv2.imread(r'C:\Users\Atif Traders\Videos\wepon\cicle\img.jpg')

# Convert to grayscale
gray_img = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)

# Apply median blur
img = cv2.medianBlur(gray_img, 5)

# Convert back to BGR
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# Detect circles using HoughCircles
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 120, param1=100, param2=30, minRadius=0, maxRadius=0)

# Ensure circles are found
if circles is not None:
    circles = np.uint16(np.around(circles))

    # Draw detected circles
    for i in circles[0,:]:
        # Draw the outer circle
        cv2.circle(planets, (i[0], i[1]), i[2], (0, 255, 0), 6)
        # Draw the center of the circle
        cv2.circle(planets, (i[0], i[1]), 2, (0, 0, 255), 3)

    # Display the image with circles
    cv2.imshow("HoughCircles", planets)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("No circles detected.")
