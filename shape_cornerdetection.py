import cv2
import numpy as np

img = cv2.imread("shapes.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
print("gray")
print(gray)

corners = cv2.goodFeaturesToTrack(gray, 22, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)
    print(x, y)

print(len(corners))

cv2.imshow("Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
