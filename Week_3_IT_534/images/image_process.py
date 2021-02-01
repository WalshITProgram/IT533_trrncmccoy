from PIL import Image
from PIL import ExifTags
from PIL import ImageFont
from PIL import ImageDraw


my_image = Image.open("clancy_stuart.jpg")

print(my_image.size)
exif_data = {}
for key, value in my_image._getexif().items():
    if key in ExifTags.TAGS:
        exif_data[ExifTags.TAGS[key]] = value
#print(exif_data)

draw_text = ImageDraw.Draw(my_image)
font = ImageFont.truetype("Syne-Regular.otf", 24)
draw_text.text((0,0), "Sample Text",(255, 0, 0) , font)
my_image.save("sample-output_files.jpg")

