import pygame
import random
pygame.init

WIDTH, HEIGHT= 1000, 1000
WINDOWS = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Lets PLAY!")
Clock = pygame.time.Clock()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font('Font/Minecraft.ttf', 50)

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 200

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



#above is title screen code
#below is game code





BACKGROUND_IMAGE = pygame.image.load('Assests/space-background-spaceship-arcade-game-090062351_prevstill.jpg').convert_alpha()
MEME_SUN = pygame.image.load('Assests/meme-baby.png').convert_alpha()
EVIL_ALIEN = pygame.image.load('Assests/LGM.png').convert_alpha()
TEXT = font.render('PLASMA SHOOTER', True, 'White')
WHITE_COLOR = (255,255,255)

DEFAULT_IMAGE_ALIEN = (100, 100)

EVIL_ALIEN = pygame.transform.scale(EVIL_ALIEN, DEFAULT_IMAGE_ALIEN)
EVIL_ALIEN_HEIGHT = EVIL_ALIEN.get_height()
class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = EVIL_ALIEN
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

aliens = pygame.sprite.Group()
for _ in range(10):  # Create 10 aliens
    alien = Alien(random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50))
    aliens.add(alien)


def main():
    run = True
    level = 1
    lives = 5
    evil_alien_speed = random.uniform(1, 5)  # You can use uniform for decimal values
    evil_alien_move_down = random.randint(200, 400)  # Adjust as needed
    evil_alien_direction = random.choice([-1, 1])  # Start moving left or right
    num_direction_changes = 0
        
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        for alien in aliens:
            alien.rect.x += evil_alien_speed * evil_alien_direction

            if alien.rect.right >= WIDTH or alien.rect.left <= 0:
                evil_alien_direction *= -1
                num_direction_changes += 1

                if num_direction_changes % 5 == 0:
                    for a in aliens:
                        a.rect.y += evil_alien_move_down
                        
            if alien.rect.top >= HEIGHT:
                alien.rect.bottom = 0
                alien.rect.x = random.randint(0, WIDTH - 50)

        WINDOWS.fill(WHITE_COLOR)
        BG = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
        WINDOWS.blit(BG, (0, 0))
        WINDOWS.blit(MEME_SUN, (750, 100))
        WINDOWS.blit(TEXT, (700, 650))
        
        lives_display = font.render(f"Lives: {lives}", 1, WHITE_COLOR)
        level_display = font.render(f"Level: {level}", 1, WHITE_COLOR)
        WINDOWS.blit(lives_display, (10, 10))
        WINDOWS.blit(level_display, (WIDTH - level_display.get_width() - 10, 10))

        for alien in aliens:
            WINDOWS.blit(EVIL_ALIEN, alien.rect)

        pygame.display.update()
        Clock.tick(60)

    pygame.quit()


pygame.display.update()
Clock.tick(60)

main()




