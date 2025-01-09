from ui import *

def launch_ui() :
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        CLOCK.tick(60)
        SCREEN.fill(clr_background)
        draw_text("Download Cleaner:", FONT_LILITAONE_50, clr_text, SCREEN_WIDTH // 2 - 30, 45)
        draw_text("© TraZe 2025", FONT_LILITAONE_10, clr_text, SCREEN_WIDTH - 30, SCREEN_HEIGHT - 5)

        if bouton.draw():
            clean_download()
        
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
        launch_ui()