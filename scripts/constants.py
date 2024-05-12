from pygame import Vector2, FRect, Surface, Color
from pygame.constants import *
import pygame

pygame.init()
pygame.font.init()

SCREEN_SIZE = Vector2(800, 800)
GAME_TITLE = "Game"
FPS = 60

BACKGROUND_COLOR = Color(10, 10, 10)

FONT_NAME = None
FONT_SIZE = 15
GAME_FONT = pygame.font.SysFont(FONT_NAME, FONT_SIZE)