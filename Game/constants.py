import pygame
import os
import sys
import time
import json
import random

WIDTH, HEIGHT = 800, 600
FONT_NAME = "microsoftyahei"
FONT_SIZE = 20
MAP_TOP, MAP_LEFT = 50, 20
PIC_WIDTH, PIC_HEIGHT = 40, 40
OFFSET_X, OFFSET_Y = 70, 70
CONFIG = {
    "THEME": 1,
    "ROWS": 10,
    "COLS": 10,
    "PIC_NUM": 10
}
BLANK = -1
RANKING_FILE = "rankings.json"

LINK_WAV = "assets/ow/link.wav"
PIC_WAV = "assets/ow/click.wav"
BGM = "assets/ow/bgm.mp3"

def load_image(folder, filename, size=None):
    path = os.path.join("assets", folder, filename)
    image = pygame.image.load(path).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image