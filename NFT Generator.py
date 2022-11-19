import random
import json
import os
import cv2
import numpy as np
from PIL import Image

base_dir = os.path.dirname(os.path.realpath(__file__))


# function to make the background
def create_blank(width, height, rgb_color=(0, 0, 0)):
    image = np.zeros((height, width, 4), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    rgb_color.append(0)

    # Fill image with color 
    for i in range(0, height):
        for j in range(0, width):
            image[i, j, 0] = rgb_color[0] - random.randint(0, rgb_color[0]) * 5 / 100
            image[i, j, 1] = rgb_color[1] - random.randint(0, rgb_color[1]) * 5 / 100
            image[i, j, 2] = rgb_color[2] - random.randint(0, rgb_color[2]) * 5 / 100

    return image


def concat_images(img1, img2):
    # a simple function that overlays img2 over img1

    height, width, channels = img2.shape
    img3 = np.zeros((height, width, channels), np.uint8)
    img3[:, :, 3] = 255
    for i in range(0, height):
        for j in range(0, width):
            if img2[i, j, 3] == 0:
                img3[i, j, 0] = img1[i, j, 0]
                img3[i, j, 1] = img1[i, j, 1]
                img3[i, j, 2] = img1[i, j, 2]
            else:
                img3[i, j, 0] = img2[i, j, 0]
                img3[i, j, 1] = img2[i, j, 1]
                img3[i, j, 2] = img2[i, j, 2]
    return img3


def color_picker(img, color, randomness=0, rand_amount=5 / 100, color_to_pick=0):
    height, width, channels = img.shape
    color.append(255)
    y_var = 0

    # color to pick = RGB color channel to be changed to the color parameter
    # 2 = red
    # 1 = green
    # 0 = blue

    for i in range(0, height):
        for j in range(0, width):
            if img[i, j, color_to_pick] > 0 and img[i, j, 0] == 0 and img[i, j, 1] == 0 and img[i, j, 3] == 255 and color_to_pick == 2:
                y_var = 1
            elif img[i, j, color_to_pick] > 0 and img[i, j, 0] == 0 and img[i, j, 2] == 0 and img[i, j, 3] == 255 and color_to_pick == 1:
                y_var = 1
            elif img[i, j, color_to_pick] > 0 and img[i, j, 1] == 0 and img[i, j, 2] == 0 and img[i, j, 3] == 255 and color_to_pick == 0:
                y_var = 1

            if y_var == 1:
                ratio = img[i, j, color_to_pick] / 255
                if randomness == 1:
                    img[i, j, 0] = (color[0] - random.randint(0, color[0]) * rand_amount) * ratio
                    img[i, j, 1] = (color[1] - random.randint(0, color[1]) * rand_amount) * ratio
                    img[i, j, 2] = (color[2] - random.randint(0, color[2]) * rand_amount) * ratio
                else:
                    img[i, j, 0] = color[0] * ratio
                    img[i, j, 1] = color[1] * ratio
                    img[i, j, 2] = color[2] * ratio
                img[i, j, 3] = 255
            y_var = 0
    return img


def random_color():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


def open_img(path):
    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
    return image


def json_opener(location):
    with open(base_dir + location) as i:
        info = json.load(i)
    return info


def biased_randomizer(value):
    # example: biased_randomizer(0.3) will give a true result 30% of the time

    if random.randint(0, 1) <= value:
        return 1
    else:
        return 0


width, height = 32, 50

color_json = json_opener("/colors.json")


total_nfts = 20
# main loop that creates the nfts
for i in range(0, total_nfts):

    # select part number for each category
    eye_no = random.randint(1, 9)
    mouth_no = random.randint(1, 6)
    nose_no = random.randint(1, 3)

    # use biased_randomizer(x) for optional categories, like hats
    # that are not supposed to be present for all nfts
    # where x represents the percentage for that specific
    # category to be present in an nft
    if biased_randomizer(0.85):
        wig_no = random.randint(1, 20)
    else:
        wig_no = 0
    if biased_randomizer(0.55):
        beard_no = random.randint(1, 20)
    else:
        beard_no = 0
    if biased_randomizer(0.28):
        hat_no = random.randint(1, 18)
    else:
        hat_no = 0
    if biased_randomizer(0.3) == 1:
        glass_no = random.randint(1, 5)
    else:
        glass_no = 0

    # directories for each category
    eye_dir = f"{base_dir}/eyes/eyes_{eye_no}.png"
    mouth_dir = f"{base_dir}/mouths/mouth_{mouth_no}.png"
    wig_dir = f"{base_dir}/wigs/wig_{wig_no}.png"
    beard_dir = f"{base_dir}/beards/beard_{beard_no}.png"
    nose_dir = f"{base_dir}/noses/nose_{nose_no}.png"
    hat_dir = f"{base_dir}/hats/hat_{hat_no}.png"
    glass_dir = f"{base_dir}/glasses/glass_{glass_no}.png"

    # color traits from the color json
    bg_info = random.randint(0, len(color_json[1]) - 1)
    skin_info = random.randint(0, len(color_json[0]) - 1)
    eye_info = random.randint(0, len(color_json[2]) - 1)
    hair_info = random.randint(0, len(color_json[3]) - 1)
    background_color = color_json[1][bg_info]
    skin_color = color_json[0][skin_info]
    eye_color = color_json[2][eye_info]
    hair_color = color_json[3][hair_info]
    hat_color = random_color()

    # background and character frame
    background = create_blank(width, height, background_color)
    character = open_img(base_dir + '/character.png')
    character = color_picker(character, skin_color, 1)

    # categories
    eyes = open_img(eye_dir)
    eyes = color_picker(eyes, hair_color, 1, 20 / 100)
    eyes = color_picker(eyes, eye_color, 0, 0, 1)

    mouth = open_img(mouth_dir)
    mouth = color_picker(mouth, skin_color, 1, 5 / 100, 1)

    wig = open_img(wig_dir)
    wig = color_picker(wig, hair_color, 1)

    beard = open_img(beard_dir)
    beard = color_picker(beard, hair_color, 1)

    nose = open_img(nose_dir)
    nose = color_picker(nose, skin_color, 1)

    hat = open_img(hat_dir)
    hat = color_picker(hat, hat_color, 1, 5 / 100)
    hat = color_picker(hat, background_color, 1, 5 / 100, 2)

    glasses = open_img(glass_dir)

    # combine everything
    result = concat_images(background, character)
    result = concat_images(result, eyes)
    result = concat_images(result, beard)
    result = concat_images(result, mouth)
    result = concat_images(result, nose)
    result = concat_images(result, wig)
    result = concat_images(result, glasses)
    result = concat_images(result, hat)

    result_name = base_dir + '/result/' + str(i + 1) + '.png'

    # scales up the image to 960, 1500, any resolution can be used
    new_image = Image.fromarray(result)
    new_image = new_image.resize((960, 1500), resample=0)
    new_image.save(result_name)

print("Program Finished.")
