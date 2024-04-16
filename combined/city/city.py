import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("City Rescue Game")

# Load images
try:
    person_image = pygame.image.load("person.png").convert_alpha()
    hospital_image = pygame.image.load("hospital.jpg").convert_alpha()
    animal_image = pygame.image.load("dog.jpg").convert_alpha()
    city_image = pygame.image.load("city.jpg").convert_alpha()
except pygame.error as e:
    print("Error loading images:", e)
    pygame.quit()
    sys.exit()

# Define display_text function
def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Game variables
animal_health = 100
person_scale = 0.05  # Scale factor for person's image
animal_scale = 0.1  # Scale factor for animal's image
hospital_scale = 0.3  # Scale factor for hospital's image
person_size = (int(person_image.get_width() * person_scale), int(person_image.get_height() * person_scale))
animal_size = (int(animal_image.get_width() * animal_scale), int(animal_image.get_height() * animal_scale))
hospital_size = (int(hospital_image.get_width() * hospital_scale), int(hospital_image.get_height() * hospital_scale))
person_x = SCREEN_WIDTH // 4
person_y = SCREEN_HEIGHT // 2
hospital_x = random.randint(100, SCREEN_WIDTH - 200)  # Random hospital location
hospital_y = random.randint(100, SCREEN_HEIGHT - 200)
animal_health_x = 20
animal_health_y = 20
animal_x = animal_health_x
animal_y = animal_health_y
animal_speed = 2

# Clock for controlling FPS
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the animal (decreases health over time)
    animal_x += animal_speed
    if animal_x >= SCREEN_WIDTH - animal_size[0]:
        animal_x = animal_health_x
    animal_health -= 0.1  # Decrease health over time

    # Control the person's movement within city bounds
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and person_x > 0:
        person_x -= 3
    if keys[pygame.K_RIGHT] and person_x < SCREEN_WIDTH - person_size[0]:
        person_x += 3
    if keys[pygame.K_UP] and person_y > 0:
        person_y -= 3
    if keys[pygame.K_DOWN] and person_y < SCREEN_HEIGHT - person_size[1]:
        person_y += 3

    # Draw city background (scaled to fill the screen)
    screen.blit(pygame.transform.scale(city_image, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))

    # Draw hospital and animal
    screen.blit(pygame.transform.scale(hospital_image, hospital_size), (hospital_x, hospital_y))
    screen.blit(pygame.transform.scale(animal_image, animal_size), (animal_health_x, animal_health_y))

    # Draw person (scaled down)
    screen.blit(pygame.transform.scale(person_image, person_size), (person_x, person_y))

    # Draw health bar for the animal
    pygame.draw.rect(screen, RED, (animal_health_x, animal_health_y - 20, int(animal_health), 10))

    # Check if the animal's health has depleted
    if animal_health <= 0:
        pygame.draw.rect(screen, BLACK, (animal_health_x, animal_health_y - 20, 100, 10))  # Draw depleted health bar
        display_text("Animal has died! Game Over.", pygame.font.Font(None, 36), BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.flip()
        pygame.time.delay(1000)  # Delay for 1 second before quitting
        running = False

    # Check if person has reached the hospital
    distance_to_hospital = ((person_x - hospital_x) ** 2 + (person_y - hospital_y) ** 2) ** 0.5
    if distance_to_hospital < 50:
        display_text("You have reached the hospital! You saved the animal.", pygame.font.Font(None, 36), BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.flip()
        pygame.time.delay(1000)  # Delay for 1 second before quitting
        running = False

    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Control frame rate

# Quit Pygame
pygame.quit()
sys.exit()
