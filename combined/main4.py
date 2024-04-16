import pygame
import subprocess

# Initialize Pygame
pygame.init()


pygame.mixer.init()  # Initialize the mixer
pygame.mixer.music.load('background_music.mp3')  # Load your background music file

pygame.mixer.music.play(-1)  # Play the music on loop (-1 means infinite loop)

pygame.mixer.music.set_volume(.7)  # Set the volume to 50%


# Set up the display
WIDTH, HEIGHT = 798, 702
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animal Rescue Quest")

# Load background image
background = pygame.image.load("back_4.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load button images
quit_button = pygame.image.load("quit.jpg").convert_alpha()
play_button = pygame.image.load("play.jpg").convert_alpha()

# Resize buttons
button_width, button_height = 90, 90
quit_button = pygame.transform.scale(quit_button, (button_width, button_height))
play_button = pygame.transform.scale(play_button, (button_width, button_height))

# Button positions
quit_button_rect = quit_button.get_rect(topleft=(10, HEIGHT - button_height - 10))
play_button_rect = play_button.get_rect(topright=(WIDTH - 10, HEIGHT - button_height - 10))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                if quit_button_rect.collidepoint(mouse_pos):
                    subprocess.Popen(["python", "main1.py"])
                    running = False
                elif play_button_rect.collidepoint(mouse_pos):
                    subprocess.Popen(["python", "main.py"])
                    running = False

    # Draw background and buttons
    screen.blit(background, (0, 0))
    screen.blit(quit_button, quit_button_rect)
    screen.blit(play_button, play_button_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
