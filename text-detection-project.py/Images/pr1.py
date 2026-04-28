import cv2
from matplotlib import pyplot as plt

# Image path
image_path = "image1.png"

# Read image
image = cv2.imread(image_path)

# Check if image loaded
if image is None:
    print("Error: Image not found. Check the path.")
    exit()

# Convert to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Grayscale Image:")

# Edge detection
edges = cv2.Canny(gray, 100, 200)

# Find contours (possible text regions)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Filter small noise (important)
    if w > 30 and h > 10:
        cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Show original image
plt.figure(figsize=(10,6))
plt.imshow(image_rgb)
plt.title("Detected Text-like Regions")
plt.axis("off")
plt.show()

# Show grayscale
plt.figure(figsize=(10,6))
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

# Show edges
plt.figure(figsize=(10,6))
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")
plt.axis("off")
plt.show()