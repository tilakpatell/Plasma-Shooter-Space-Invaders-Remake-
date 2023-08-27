import pygame
import random
pygame.init

WIDTH, HEIGHT= 1920, 1080
WINDOWS = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Lets PLAY!")
Clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.Font('Font/Minecraft.ttf', 50)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
    
BACKGROUND_IMAGE = pygame.image.load('Assests/space-background-spaceship-arcade-game-090062351_prevstill.webp')
MEME_SUN = pygame.image.load('Assests/meme-baby.png')
TEXT = font.render('PLASMA SHOOTER', True, 'White')
WHITE_COLOR = (255,255,255)

WINDOWS.fill(WHITE_COLOR)
WINDOWS.blit(BACKGROUND_IMAGE,(0,0))
WINDOWS.blit(MEME_SUN, (750,100))
WINDOWS.blit(TEXT, (700, 650))




pygame.display.update()
Clock.tick(60)

main()




