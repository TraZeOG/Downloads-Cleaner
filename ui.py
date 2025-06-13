from ui_settings import *

class Bouton():
    def __init__(self, x, y, width, height, image):
        self.clicked = False
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        reset_click = False
        mouse_cos = pygame.mouse.get_pos()
        SCREEN.blit(self.image, self.rect)
        if self.rect.collidepoint(mouse_cos):
            """handles all the problems with buttons"""
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                reset_click = True
                self.clicked = False
        return reset_click

def draw_text(texte, font, couleur, x, y, centered = True):
    """small function used to draw text"""
    img = font.render(texte, True, couleur)
    if centered:
        text_width, text_height = font.size(texte)
    else:
        text_width, text_height = 0, 0
    SCREEN.blit(img, (x - text_width // 2, y - text_height // 2))

bouton = Bouton(SCREEN_WIDTH // 2 - 65, SCREEN_HEIGHT - 70, 130, 50, pygame.image.load("sprites/img_bouton_start.webp"))


