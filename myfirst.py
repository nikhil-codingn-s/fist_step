from PIL import Image

# List of image filenames
list_im = ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']

# Open the images
images = [Image.open(x) for x in list_im]

# Get image dimensions
widths, heights = zip(*(i.size for i in images))

# Calculate total width and maximum height
total_width = sum(widths)
max_height = max(heights)

# Create a new image with the calculated dimensions
new_im = Image.new('RGB', (total_width, max_height))

# Paste each image horizontally
x_offset = 0
for im in images:
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]

# Save the concatenated image
new_im.save('test.jpg')

print ("hello,world")