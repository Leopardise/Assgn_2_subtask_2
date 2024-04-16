import pygame
import random
import os

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define screen dimensions
WIDTH = 798
HEIGHT = 702

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Run to Destination!")
clock = pygame.time.Clock()

# Load background image
background_img = pygame.image.load("back_3.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))  # Resize to screen size

# Load hunter image
hunter_img = pygame.image.load("hunter.jpg")
hunter_img = pygame.transform.scale(hunter_img, (40, 40))  # Resize to 40x40 pixels

# Load player image
player_img = pygame.image.load("character.jpg")
player_img = pygame.transform.scale(player_img, (40, 40))  # Resize player image


# Define player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img  # Player image
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5

# Define obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = hunter_img  # Replace with hunter image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randrange(5, 10)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()  # Remove obstacle when it goes off-screen

# Create player and obstacle sprites
player = Player()
obstacles = pygame.sprite.Group()

# Game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                # Reset game on spacebar press after game over
                game_over = False
                player.rect.centerx = WIDTH // 2
                player.rect.bottom = HEIGHT - 10
                obstacles.empty()  # Remove all obstacles

    # Check for collision with obstacles during game
    if not game_over and pygame.sprite.spritecollideany(player, obstacles):
        game_over = True

    # Move obstacles and create new ones
    if not game_over:
        for obstacle in obstacles:
            obstacle.update()
        obstacle_chance = random.randrange(100)
        if obstacle_chance < 5:  # Adjust for desired obstacle frequency
            new_obstacle = Obstacle()
            obstacles.add(new_obstacle)

    # Draw game elements
    screen.blit(background_img, (0, 0))  # Draw background
    if not game_over:
        obstacles.draw(screen)
        player.update()
        screen.blit(player.image, player.rect)
    else:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Press Space to Restart", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Set FPS

# Quit Pygame
pygame.quit()
