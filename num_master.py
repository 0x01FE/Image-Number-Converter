from lib2to3.pytree import convert
import cv2
import pygame as pg
from math import ceil, floor
from PIL import Image
TEXT_WIDTH = 6 # on font size 12 monocraft medium
TEXT_HEIGHT = 11
RESOLUTION_FACTOR = 2
WHITE = (255,255,255)
number_of_shades = 2
numbers = []
for i in range(0,number_of_shades):
    numbers.append(str(i))

def convert_num(image_path):
    if image_path[-3:] != "png":
        im1 = Image.open(image_path)
        image_path = image_path[:-3]+"png"
        im1.save(image_path)
    pg.init()
    font = pg.font.SysFont("Monocraft Medium", 12)
    img = cv2.imread(image_path, 0)
    HEIGHT, WIDTH = img.shape
    WIDTH *= RESOLUTION_FACTOR
    HEIGHT *= RESOLUTION_FACTOR
    GRID_WIDTH = WIDTH // TEXT_WIDTH
    GRID_HEIGHT = HEIGHT // TEXT_HEIGHT
    w = pg.display.set_mode((GRID_WIDTH * TEXT_WIDTH, GRID_HEIGHT * TEXT_HEIGHT))
    img = cv2.resize(img, (GRID_WIDTH, GRID_HEIGHT), interpolation=cv2.INTER_AREA)
    for pixel_x in range(GRID_WIDTH):
        for pixel_y in range(GRID_HEIGHT):
            brightness = img[pixel_y][pixel_x]
            num = ceil(brightness / (255/number_of_shades))  # Map to 0-1, 255/num
            if num == 0:
                continue
            r_num = None # rendered num
            r_num = font.render(numbers[num-1],1,WHITE)
            w.blit(r_num,(pixel_x*TEXT_WIDTH,pixel_y*TEXT_HEIGHT))
    pg.display.update()
    pg.image.save(w, image_path[:-4]+"_num.png")
    pg.quit()

convert_num("example.png")