from PIL import Image, ImageDraw

# Create a black canvas
width, height = 400, 400
canvas = Image.new('RGB', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(canvas)

# Set the colors
black = (0, 0, 0)
dark_gray = (40, 40, 40)
light_gray = (160, 160, 160)

# Draw the head shape
draw.ellipse([(20, 20), (380, 380)], fill=dark_gray)

# Draw the ears
draw.pieslice([(20, 20), (180, 180)], start=0, end=180, fill=light_gray)
draw.pieslice([(220, 20), (380, 180)], start=0, end=180, fill=light_gray)

# Draw the eyes
draw.ellipse([(130, 130), (170, 170)], fill=black)
draw.ellipse([(230, 130), (270, 170)], fill=black)

# Draw the nose
draw.polygon([(200, 200), (185, 240), (215, 240)], fill=black)

# Draw the mouth
draw.arc([(150, 280), (250, 350)], start=0, end=180, fill=black)

# Display the image
canvas.show()
