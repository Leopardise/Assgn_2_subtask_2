import pygame
import subprocess

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 798
SCREEN_HEIGHT = 702

pygame.mixer.init()  # Initialize the mixer
pygame.mixer.music.load('background_music.mp3')  # Load your background music file

pygame.mixer.music.play(-1)  # Play the music on loop (-1 means infinite loop)

pygame.mixer.music.set_volume(.7)  # Set the volume to 50%

# Load images
injured_bird_image = pygame.image.load("injured_bird.png")  # Replace with your image path
back_button_image = pygame.image.load("back_button.png")
next_button_image = pygame.image.load("next_button.png")

# Helper function for button clicks
def is_button_clicked(rect, pos):
    """Checks if a given position is within a rectangular button area"""
    return rect.collidepoint(pos)

# Function to display injured bird window
def display_injured_bird_window():
    injured_window_width, injured_window_height = 798, 702
    injured_window = pygame.display.set_mode((injured_window_width, injured_window_height))
    pygame.display.set_caption("Animal Rescue Quest")

    # Scale the injured bird image
    scaled_injured_bird_image = pygame.transform.scale(injured_bird_image, (
        int(injured_bird_image.get_width() * 0.6),
        int(injured_bird_image.get_height() * 0.6)
    ))

    # Center the injured bird image
    injured_window.blit(scaled_injured_bird_image, (
        (injured_window_width - scaled_injured_bird_image.get_width()) // 2,
        (injured_window_height - scaled_injured_bird_image.get_height()) // 2
    ))

    # Load and scale buttons
    button_size = min(injured_window_width, injured_window_height) // 10

    back_button_image_scaled = pygame.transform.scale(back_button_image, (button_size, button_size))
    back_button_mask = pygame.Surface((button_size, button_size), pygame.SRCALPHA)
    pygame.draw.circle(back_button_mask, (255, 255, 255, 255), (button_size // 2, button_size // 2), button_size // 2)
    back_button_image_scaled.blit(back_button_mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    injured_window.blit(back_button_image_scaled, (20, 20))

    next_button_image_scaled = pygame.transform.scale(next_button_image, (button_size, button_size))
    # ... (Do the same for next_button_image_scaled) ...
    injured_window.blit(next_button_image_scaled, (
        injured_window_width - button_size - 20,
        injured_window_height - button_size - 20
    ))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_button_clicked(pygame.Rect(20, 20, button_size, button_size), pygame.mouse.get_pos()):
                    subprocess.Popen(["python", "main5.py"])  # Transition to main6.py
                    return
                elif is_button_clicked(pygame.Rect(
                    injured_window_width - button_size - 20,
                    injured_window_height - button_size - 20,
                    button_size, button_size), pygame.mouse.get_pos()):
                    subprocess.Popen(["python", "main9.py"])  # Transition to main3.py
                    return

# Main function (add more setup if needed)
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display_injured_bird_window()

if __name__ == "__main__":
    main()
