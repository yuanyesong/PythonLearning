from PIL import Image
import pytesseract

verifycode = Image.open("captcha.png")
code = pytesseract.image_to_string(verifycode)
print(code)