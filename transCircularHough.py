import cv2
import numpy as np
# Define the Hough transform parameters
rho = 1
theta = np.pi / 180
threshold = 100
min_line_length = 100
max_line_gap = 10

# Read the image
image = cv2.imread('Familia_Simpson.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Hough transform
lines = cv2.HoughLinesP(gray, rho, theta, threshold, min_line_length, max_line_gap)

# Draw the lines on the image
for line in lines:
    print('line',line,'shape',line.shape)
    start_point = [line[0][0],line[0][1]]
    end_point = [line[0][2],line[0][3]]
    print('start_point',start_point,'end_point',end_point)
    cv2.line(image, start_point, end_point, (0, 0, 255), 1)

# Display the image
cv2.imshow('Hough Lines', image)
cv2.waitKey()

# circular 
gray = cv2.medianBlur(gray, 5)

rows = gray.shape[0]
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
param1=200, param2=10,
minRadius=2, maxRadius=30)


if circles is not None:
  circles = np.uint16(np.around(circles))
  for i in circles[0, :]:
    center = (i[0], i[1])

    # circle center
    cv2.circle(image, center, 1, (0, 100, 100), 3)
    # circle outline
    radius = i[2]
    cv2.circle(image, center, radius, (255, 0, 255), 3)


cv2.imshow("detected circles", image)
cv2.waitKey(0)

cv2.destroyAllWindows()
