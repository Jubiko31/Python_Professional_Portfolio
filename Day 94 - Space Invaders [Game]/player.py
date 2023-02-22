import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

class Player(pygame.sprite.Sprite):    
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/imgs/player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT
        self.lives = 5
        self.velocity = 8
        self.bullet_group = bullet_group
        self.shoot_sound = pygame.mixer.Sound("assets/sounds/player_fire.wav")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.velocity

    def fire(self):
        if len(self.bullet_group) < 2:
            self.shoot_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)

    def reset(self):
        self.rect.centerx = SCREEN_WIDTH // 2
        
class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/imgs/green_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = 10
        bullet_group.add(self)

    def update(self):
        self.rect.y -= self.velocity
        if self.rect.bottom < 0:
            self.kill()