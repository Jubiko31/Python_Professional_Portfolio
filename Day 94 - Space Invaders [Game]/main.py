import pygame
from player import Player
from alien import Alien

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

bg = pygame.image.load("assets/imgs/bg.jpg")

display_mode = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

class Game():
    def __init__(self, player, aliens, player_bullets, alien_bullets):
        self.round_number = 1
        self.score = 0
        self.player = player
        self.aliens = aliens
        self.player_bullets = player_bullets
        self.alien_bullets = alien_bullets
        self.font = pygame.font.Font("assets/Facon.ttf", 32)
        
        # Game Sounds:
        self.new_round_soundtrack = pygame.mixer.Sound("assets/sounds/new_round.wav")
        self.breach_sound = pygame.mixer.Sound("assets/sounds/breach.wav")
        self.player_hit_sound = pygame.mixer.Sound("assets/sounds/player_hit.wav")
        self.alient_hit_sound = pygame.mixer.Sound("assets/sounds/alien_hit.wav")
        
    def update(self):
            self.shift_aliens()
            self.check_collisions()
            self.check_round_complete()
    # HUD
    def draw(self):
        # score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = SCREEN_WIDTH // 2
        score_rect.top = 10
        # round
        round_text = self.font.render(f"Round: {self.round_number}", True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (20, 10)
        # player lives
        lives_text = self.font.render(f"Lives: {self.player.lives}", True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (SCREEN_WIDTH - 20, 10)

        display_mode.blit(score_text, score_rect)
        display_mode.blit(round_text, round_rect)
        display_mode.blit(lives_text, lives_rect)
        pygame.draw.line(display_mode, WHITE, (0, 50), (SCREEN_WIDTH, 50), 4)
        pygame.draw.line(display_mode, WHITE, (0, SCREEN_HEIGHT - 100), (SCREEN_WIDTH, SCREEN_HEIGHT - 100), 4)        
        
    def shift_aliens(self):
        shift = False
        for alien in (self.aliens.sprites()):
            if alien.rect.left <= 0 or alien.rect.right >= SCREEN_WIDTH:
                shift = True
        if shift:
            breach = False
            for alien in (self.aliens.sprites()):
                alien.rect.y += 10 * self.round_number
                alien.direction = -1 * alien.direction
                alien.rect.x += alien.direction * alien.velocity
                if alien.rect.bottom >= SCREEN_HEIGHT - 100:
                    breach = True
            
            if breach:
                self.breach_sound.play()
                self.player.lives -= 1
                self.check_game_status("Aliens Beached the Line!", "Press Enter to Continue")
    
    def check_collisions(self):
        # Player hits alien
        if pygame.sprite.groupcollide(self.player_bullets, self.aliens, True, True):
            self.alient_hit_sound.play()
            self.score += 100
        # Player gets hit
        if pygame.sprite.spritecollide(self.player, self.alien_bullets, True):
            self.player_hit_sound.play()
            self.player.lives -= 1
            
            self.check_game_status("You've Been Hit!", "Press Enter to Continue")
    
    def check_round_complete(self):
        if not (self.aliens):
            self.score += 1000 * self.round_number
            self.round_number += 1
            self.next_round()
    
    def next_round(self):
        for col in range(11):
            for row in range(5):
                alien = Alien(64+col*64, 64+row*64, self.round_number, self.alien_bullets)
                self.aliens.add(alien)
        
        self.new_round_soundtrack.play()
        self.pause_game(f"Space Invaders Round - {self.round_number}", "Press Enter to Begin")
    
    def check_game_status(self, main_text, sub_text):
        self.alien_bullets.empty()
        self.player_bullets.empty()
        self.player.reset()
        for alien in self.aliens:
            alien.reset()

        if self.player.lives == 0:
            self.reset_game()
        else:
            self.pause_game(main_text, sub_text)
    
    def pause_game(self, main_text, sub_text):
        global running
        is_paused = True

        main_text = self.font.render(main_text, True, WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        sub_text = self.font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 64)

        display_mode.fill(BLACK)
        display_mode.blit(main_text, main_rect)
        display_mode.blit(sub_text, sub_rect)
        pygame.display.update()

        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                # Quit game
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
    
    def reset_game(self):
        self.pause_game(f"Final Score: {self.score}", "Press Enter to Play Again")
        
        self.score = 0
        self.round_number = 1
        self.player.lives = 5
        self.aliens.empty()
        self.player_bullets.empty()
        self.alien_bullets.empty()
        
        self.next_round()
        
player_bullet_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()

player_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()

player = Player(player_bullet_group)
player_group.add(player)

# Game
game = Game(player, alien_group, player_bullet_group, alien_bullet_group)
game.next_round()

on = True
while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()
    
    display_mode.blit(bg, (0, 0))
    
    player_group.update()
    player_group.draw(display_mode)
    alien_group.update()
    alien_group.draw(display_mode)
    player_bullet_group.update()
    player_bullet_group.draw(display_mode)
    alien_bullet_group.update()
    alien_bullet_group.draw(display_mode)
    
    game.update()
    game.draw()

    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
