import pygame
import random
import time
import os
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
                    return  

        WINDOWS.fill(BLACK)
        WINDOWS.blit(title, title_rect)

        start_button.draw(WINDOWS)

        pygame.display.update()
        Clock.tick(60)

title_screen()



#above is title screen code
#below is game code


IMAGE_SHIP = pygame.image.load('Assests/ship.png').convert_alpha()
PLAYER_SHIP = pygame.transform.scale(IMAGE_SHIP, (150, 150))
MISSLE = pygame.image.load('Assests/missile.png').convert_alpha()
BACKGROUND_IMAGE = pygame.image.load('Assests/space-background-spaceship-arcade-game-090062351_prevstill.jpg').convert_alpha()
MEME_SUN = pygame.image.load('Assests/meme-baby.png').convert_alpha()
EVIL_ALIEN = pygame.image.load('Assests/LGM.png').convert_alpha()
TEXT = font.render('PLASMA SHOOTER', True, 'White')
WHITE_COLOR = (255,255,255)

DEFAULT_IMAGE_ALIEN = (100, 100)

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
                
    def move(self, vel):
        self.y += vel
        
    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)
    
    def clash(self, obj):
        return collide(self, obj)
    
    
    
    
    

class Ship:
    COOLDOWN = 30
    
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        
    
    def draw(self, window):
        WINDOWS.blit(self.ship_img, (self.x, self.y))

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
    
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
            
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
                
    def tallness(self):
        return self.ship_img.get_height()
    
    def fatness(self):
        return self.ship_img.get_width()           
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = PLAYER_SHIP
        self.laser_img = MISSLE
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.clash(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                            
                            
EVIL_ALIEN = pygame.transform.scale(EVIL_ALIEN, DEFAULT_IMAGE_ALIEN)
EVIL_ALIEN_HEIGHT = EVIL_ALIEN.get_height()

class Alien(Ship):
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img = EVIL_ALIEN 
        self.laser_img = None
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x #objects corners 
    offset_y = obj2.y - obj1.y 
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None #if the offsets of the corners overlap then it collides 

def main():
    run = True
    level = 0
    lives = 5
    wave_length = 5
    evil_alien_speed = 2 
    #evil_alien_move_down = random.randint(200, 400)  
    #evil_alien_direction = random.choice([-1, 1])  
    #num_direction_changes = 0 old code for different alien spawn method, didnt work LOL
    player_pixel =  5
    player = Player(300, 650)
    aliens = []
    laser_speed = 5
    lose = False
    lose_counter = 0
    clock = pygame.time.Clock()
    
    def window_refresh():
        
        WINDOWS.fill(WHITE_COLOR)
        BG = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
        WINDOWS.blit(BG, (0, 0))
        
        meme_sun_x = WIDTH // 2 - MEME_SUN.get_width() // 2
        meme_sun_y = HEIGHT // 2 - MEME_SUN.get_height() // 2
        WINDOWS.blit(MEME_SUN, (meme_sun_x, meme_sun_y))
        
        text_x = WIDTH // 2 - TEXT.get_width() // 2
        text_y = meme_sun_y + MEME_SUN.get_height() + 20  # Adjust the spacing as needed
        WINDOWS.blit(TEXT, (text_x, text_y))
                     
        lives_display = font.render(f"Lives: {lives}", 1, (0,255,0))
        level_display = font.render(f"Level: {level}", 1, (225,0,0))
        WINDOWS.blit(lives_display, (10, 10))
        WINDOWS.blit(level_display, (WIDTH - level_display.get_width() - 10, 10))
        
        for alien in aliens:
            alien.draw(WINDOWS)
  
        player.draw(WINDOWS)
        
        if lose:
            YOU_LOSE = font.render("YOU LOSEEEE LLLL", 1, (225,0,0))
            WINDOWS.blit(YOU_LOSE, (WIDTH/2 - YOU_LOSE.get_width()/2, 500))
         
        pygame.display.update()
    
    while run:
        clock.tick(60)
        
        window_refresh()
        if lives <= 0 or player.health <= 0:
            lose = True
            lose_counter += 1
            
        if lose:
            if lose_counter > 60 * 3:
                run = False
            else:
                continue
            
        if len(aliens) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                alien = Alien(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), EVIL_ALIEN)
                aliens.append(alien)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        #this is for user input 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_pixel > 0: 
            player.x -= player_pixel
        if keys[pygame.K_d] and player.x + player_pixel + player.fatness() < WIDTH:
            player.x += player_pixel
        if keys[pygame.K_w] and player.y - player_pixel > 0:
            player.y -= player_pixel
        if keys[pygame.K_s] and player.y + player_pixel + player.tallness() < HEIGHT:
            player.y += player_pixel
        if keys[pygame.K_SPACE]:
            player.shoot()
        
        
        for alien in aliens[:]:
            alien.move(evil_alien_speed)
            alien.move_lasers(laser_speed, player)
            if alien.y + alien.tallness() > HEIGHT:
                lives -= 1
                aliens.remove(alien)
            
        player.move_lasers(-laser_speed, aliens)
        window_refresh()

    pygame.quit()



        
main()