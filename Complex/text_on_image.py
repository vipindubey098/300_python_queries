from PIL import Image, ImageDraw

img = Image.open("image.png")
text = "Hello"
draw_img = ImageDraw.Draw(img)
draw_img.text((10,20), text, (24,24,54))
img.show()