import cv2
import os

folder = "/home/sakshi/mywebsite/startbootstrap-personal/dist/assets/profile"
# Load input image and transparent PNG
input_image = cv2.imread(os.path.join(folder, "watercolor.png"), cv2.IMREAD_UNCHANGED)
png_image = cv2.imread(os.path.join(folder, "original.png"), cv2.IMREAD_UNCHANGED)

# Extract the alpha channel from the PNG image
alpha_channel = png_image[:, :, 3]

# Resize input image to match dimensions of PNG image if necessary
if input_image.shape[:2] != png_image.shape[:2]:
    input_image = cv2.resize(input_image, (png_image.shape[1], png_image.shape[0]))

# Create new image with transparent background
cutout_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2BGRA)

# Copy input image onto the new image using alpha channel as mask
cutout_image[:, :, 3] = alpha_channel

# Save the resulting cutout image
cv2.imwrite(os.path.join(folder, "watercolor_trans.png"), cutout_image)
