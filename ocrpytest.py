from PIL import Image
from pytesseract import image_to_string
print(image_to_string(Image.open('final.png')))
print(image_to_string(Image.open('final.png'), lang='eng'))
