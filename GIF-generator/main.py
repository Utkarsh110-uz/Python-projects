import imageio.v3 as im
import cv2

filename_list = ["img-1.jpeg", "img-2.jpeg"]
fixed_images = []

for file in filename_list:
    img = im.imread(file)

    # Resize
    img = cv2.resize(img, (256, 256))

    # Convert grayscale to RGB
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    fixed_images.append(img)

# Create GIF
im.imwrite('dark.gif', fixed_images, duration=500, loop=0)
