import pygame
import pickle
from vacuum import clean_download

pygame.init()
pygame.display.set_caption("Time Tracker PC")

CLOCK = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 760, 160
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT_LILITAONE_50 = pygame.font.Font("fonts/LilitaOne-Regular.ttf", 50)
FONT_LILITAONE_30 = pygame.font.Font("fonts/LilitaOne-Regular.ttf", 30)
FONT_LILITAONE_10 = pygame.font.Font("fonts/LilitaOne-Regular.ttf", 10)
CLR_WHITE = (255,255,255)
CLR_BLACK = (0,0,0)

pickle_in = open(f'data/data_main', 'rb')
data = pickle.load(pickle_in)
clr_background = data[0]
clr_text = data[1]