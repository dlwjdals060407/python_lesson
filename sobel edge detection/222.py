import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sobel edge detection/img.png', cv2.IMREAD_GRAYSCALE)

dx = cv2.Sobel(img, cv2.CV_64F, 1, 0, 3)
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1, 3)

sobel = cv2.magnitude(dx, dy)
sobel = np.clip(sobel, 0, 255).astype(np.uint8)

plt.figure(figsize=(8,8))
plt.subplot(131), plt.imshow(sobel), plt.axis("off")
plt.subplot(132), plt.imshow(np.abs(dx)), plt.axis("off")
plt.subplot(133), plt.imshow(np.abs(dy)), plt.axis("off")
plt.show()

