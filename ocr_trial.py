from PIL import Image
import pytesseract
print(pytesseract.image_to_string(Image.open("sample_trial.png")))
# print(pytesseract.image_to_string("sample_trial.png"))
from PIL import Image, ImageDraw
import pytesseract

img = Image.open("paper.tiff")

data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

draw = ImageDraw.Draw(img)
words = []

for i in range(len(data["text"])):
    word = data["text"][i].strip()
    if word != "":
        x = data["left"][i]
        y = data["top"][i]
        w = data["width"][i]
        h = data["height"][i]
        draw.rectangle([x, y, x + w, y + h], outline="green", width=2)
        words.append(word)
img=img.convert("RGB")
print(" ".join(words))
print("Word count:", len(words))

img.save("annotated.jpeg")
