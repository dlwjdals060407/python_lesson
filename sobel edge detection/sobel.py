import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image (replace 'your_image_path.jpg' with the actual path of your image)
img = cv2.imread('sobel edge detection/Lenna.png', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to load the image.")
else:
    # Perform Sobel operations
    dx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    dy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate gradient magnitude and angle
    magnitude, angle = cv2.cartToPolar(dx, dy, angleInDegrees=True)

    # Apply threshold to the gradient magnitude (adjust threshold_value as needed)
    threshold_value = 100  # Adjust this threshold value as needed
    magnitude_thresholded = np.where(magnitude >= threshold_value, magnitude, 0)

    # Display the results using matplotlib
    plt.figure(figsize=(12, 5))
    plt.subplot(151), plt.imshow(img, cmap='gray'), plt.title('Original Image'), plt.axis("off")
    plt.subplot(152), plt.imshow(np.abs(dx), cmap='gray'), plt.title('Sobel X'), plt.axis("off")
    plt.subplot(153), plt.imshow(np.abs(dy), cmap='gray'), plt.title('Sobel Y'), plt.axis("off")
    plt.subplot(154), plt.imshow(magnitude, cmap='gray'), plt.title('Gradient Magnitude'), plt.axis("off")
    plt.subplot(155), plt.imshow(magnitude_thresholded, cmap='gray'), plt.title('Thresholded Magnitude'), plt.axis("off")
    plt.show()
