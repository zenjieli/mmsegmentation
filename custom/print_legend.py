from mmseg.datasets.ade import ADE20KDataset
from PIL import Image, ImageDraw, ImageFont

labels = ADE20KDataset.METAINFO['classes']
palette = ADE20KDataset.METAINFO['palette']

# Create a new image with a white background
idx_width = 30
color_width = 20
color_height = 20
coord_width = 130
spacing = 5
width = 1920
height = 1080
col_width = 400
col_height = 1000
legend_image = Image.new('RGB', (width, height), (255, 255, 255))

# Get the drawing context
draw = ImageDraw.Draw(legend_image)

# Set font properties (run `fc-list` terminal command find all the available fonts)
font = ImageFont.truetype("DejaVuSansMono.ttf", 14)

# Calculate the position and spacing for each label and color
x = y = spacing

# Draw the legend items
idx = 0
for idx, (label, color) in enumerate(zip(labels, palette)):
    draw.text((x, y), f'{idx}', font=font, fill=(0, 0, 0))
    draw.rectangle([x+idx_width, y, x+idx_width+color_width, y+color_height], fill=tuple(color))
    draw.text((x+idx_width+color_width+spacing, y), f'{color}', font=font, fill=(0, 0, 0))
    draw.text((x+idx_width+color_width+coord_width+2*spacing, y), label, font=font, fill=(0, 0, 0))

    # Update top coord; Move to the next col if too big
    y += color_height + spacing
    if y > col_height:
        x += col_width
        y = spacing

# Save or display the image
legend_image.save('legend.png')  # Save the image as 'legend.png'
legend_image.show()  # Display the image using the default image viewer
