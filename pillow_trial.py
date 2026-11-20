from PIL import Image
import matplotlib.pyplot as plt
im=Image.open("sample_trial.png")
print(im.format,im.size,im.mode)




from PIL import Image, ImageStat
import matplotlib.pyplot as plt

# 1. Open the image
image = Image.open("python.png")

# Convert image to RGB
image = image.convert("RGB")

print("Original dimensions:", image.size)

# 2. Resize the image
width = 800
height = 600

resized_image = image.resize((width, height))

# Save resized image
resized_image.save("resized_image.jpg")

print("Resized dimensions:", resized_image.size)


# 3. Calculate image statistics
stats = ImageStat.Stat(resized_image)

# Mean values
mean_values = stats.mean

print("\nMean RGB values:")
print("Red:", mean_values[0])
print("Green:", mean_values[1])
print("Blue:", mean_values[2])


# 4. Find minimum and maximum pixel values
extrema = resized_image.getextrema()

print("\nMinimum and Maximum RGB values:")

channels = ["Red", "Green", "Blue"]

for i in range(3):
    print(channels[i], ":", extrema[i])


# 5. Extract RGB histogram
histogram = resized_image.histogram()

red_hist = histogram[0:256]
green_hist = histogram[256:512]
blue_hist = histogram[512:768]


# 6. Plot RGB histogram
plt.plot(red_hist, color="red", label="Red")
plt.plot(green_hist, color="green", label="Green")
plt.plot(blue_hist, color="blue", label="Blue")

plt.title("RGB Colour Distribution")
plt.xlabel("Pixel Intensity (0-255)")
plt.ylabel("Number of Pixels")

plt.legend()
plt.grid()

# Save histogram
plt.savefig("rgb_histogram.png")

plt.show()




