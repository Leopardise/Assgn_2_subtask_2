import pygame
import subprocess

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Load images
injured_animal_image = pygame.image.load("injured_animal.png")  # Replace with your image path
back_button_image = pygame.image.load("back_button.png")
next_button_image = pygame.image.load("next_button.png")

# Helper function for button clicks
def is_button_clicked(rect, pos):
    """Checks if a given position is within a rectangular button area"""
    return rect.collidepoint(pos)

# Function to display injured animal window
def display_injured_animal_window():
    injured_window_width, injured_window_height = 798, 702
    injured_window = pygame.display.set_mode((injured_window_width, injured_window_height))
    pygame.display.set_caption("Injured Animal")

    # Scale the injured animal image
    scaled_injured_animal_image = pygame.transform.scale(injured_animal_image, (
        int(injured_animal_image.get_width() * 0.6),
        int(injured_animal_image.get_height() * 0.6)
    ))

    # Center the injured animal image
    injured_window.blit(scaled_injured_animal_image, (
        (injured_window_width - scaled_injured_animal_image.get_width()) // 2,
        (injured_window_height - scaled_injured_animal_image.get_height()) // 2
    ))

    # Load and scale buttons
    button_size = min(injured_window_width, injured_window_height) // 10

    back_button_image_scaled = pygame.transform.scale(back_button_image, (button_size, button_size))
    back_button_mask = pygame.Surface((button_size, button_size), pygame.SRCALPHA)
    pygame.draw.circle(back_button_mask, (255, 255, 255, 255), (button_size // 2, button_size // 2), button_size // 2)
    back_button_image_scaled.blit(back_button_mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    injured_window.blit(back_button_image_scaled, (20, 20))

    next_button_image_scaled = pygame.transform.scale(next_button_image, (button_size, button_size))
    # ... (Do the same masking for next_button_image_scaled) ...
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
                    subprocess.Popen(["python", "main4.py"])  # Transition to main4.py
                    return
                elif is_button_clicked(pygame.Rect(
                    injured_window_width - button_size - 20,
                    injured_window_height - button_size - 20,
                    button_size, button_size), pygame.mouse.get_pos()):
                    subprocess.Popen(["python", "main3.py"])  # Transition to main2.py
                    return

# Main function (add more setup if needed)
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # ... (Any initial setup) ...

    display_injured_animal_window()

if __name__ == "__main__":
    main()
