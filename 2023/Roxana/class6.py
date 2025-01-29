import os
import random


score = 0
images = os.listdir(r"C:\Users\saeed\Documents\Students\Arshia\images")

numbers = []
symbols = []
colors = []
fillings = []


random_images = random.choices(images, k=3)


for random_image in random_images:
    splited_image = random_image.split(" ")
    
    number = splited_image[0]
    symbol = splited_image[1]
    color = splited_image[3]
    filling = splited_image[5]

    numbers.append(number)
    symbols.append(symbol)
    colors.append(color)
    fillings.append(filling)


if len(set(numbers)) == 1 or len(set(symbols)) == 1 or len(set(colors)) == 1 or len(set(fillings)) == 1:
    score += 2

print(set(numbers), set(symbols), set(colors), set(fillings))
print("Score: ", score)
    
