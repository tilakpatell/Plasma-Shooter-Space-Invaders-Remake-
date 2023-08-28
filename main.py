import pygame
import random
pygame.init

WIDTH, HEIGHT= 1920, 1080
WINDOWS = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Lets PLAY!")
Clock = pygame.time.Clock()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font('Font/Minecraft.ttf', 50)

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

class Button(pygame.sprite.Sprite):
    def __init__(self, text, x, y):
        super().__init__()
        self.image = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.text = text

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        text_rendered = font.render(self.text, True, WHITE)
        text_rect = text_rendered.get_rect(center=self.rect.center)
        screen.blit(text_rendered, text_rect)

def title_screen():
    title = font.render('PLASMA SHOOTER', True, WHITE)
    title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 3))

    start_button = Button("START", WIDTH // 2, HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(event.pos):
                    return  # Return to start the game

        WINDOWS.fill(BLACK)
        WINDOWS.blit(title, title_rect)

        start_button.draw(WINDOWS)

        pygame.display.update()
        Clock.tick(60)

title_screen()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
    
BACKGROUND_IMAGE = pygame.image.load('Assests/space-background-spaceship-arcade-game-090062351_prevstill.webp')
MEME_SUN = pygame.image.load('Assests/meme-baby.png')
EVIL_ALIEN = pygame.image.load('Assests/LGM.png')
TEXT = font.render('PLASMA SHOOTER', True, 'White')
WHITE_COLOR = (255,255,255)

WINDOWS.fill(WHITE_COLOR)
WINDOWS.blit(BACKGROUND_IMAGE,(0,0))
WINDOWS.blit(MEME_SUN, (750,100))
WINDOWS.blit(TEXT, (700, 650))
WINDOWS.blit(EVIL_ALIEN, (1000, 500))



pygame.display.update()
Clock.tick(60)

main()




