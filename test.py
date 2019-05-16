from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

img = Image.open('temp.png')
text = pytesseract.image_to_string(img)

print(text)
