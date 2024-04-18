import pygame
import sys
import pygame_gui

# Initialize Pygame and Pygame GUI
pygame.init()
pygame.font.init()
pygame_gui.elements.UIButton

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the display surface
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

# Load images
player_image = pygame.image.load('person.png')
player_image = pygame.transform.scale(player_image, (30, 30))  # Scale player to 30x30
hospital_image = pygame.image.load('hospital.jpg')
hospital = pygame.transform.scale(hospital_image, (50, 50))
background_image = pygame.image.load('city.jpg')
background = pygame.transform.scale(background_image, (screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# FPS controller
clock = pygame.time.Clock()
fps = 30

# UI Manager
manager = pygame_gui.UIManager((screen_width, screen_height))

# Player attributes
player_size = 30
player_pos = [50, 50]
player_speed = 5

# Destination
destination_pos = [700, 500]

# Levels with maze configurations
levels = [
    [  # Level 1
        (0, 0, 10, 600),  # Left wall
        (0, 0, 800, 10),  # Top wall
        (790, 0, 10, 600),  # Right wall
        (0, 590, 800, 10),  # Bottom wall
        (100, 50, 10, 500),  # Vertical wall near left
        (100, 50, 600, 10),  # Horizontal wall near top
        (300, 100, 10, 500),  # Middle vertical wall
        (200, 500, 500, 10),  # Bottom horizontal wall
        (700, 50, 10, 450),  # Right side vertical wall
        (400, 250, 340, 10),  # Middle horizontal wall
    ],
    [  # Level 2
        (0, 0, 10, 600),
        (0, 0, 800, 10),
        (790, 0, 10, 600),
        (0, 590, 800, 10),
        (50, 100, 700, 10),  # Top horizontal wall shifted right
        (150, 0, 10, 500),  # Left side vertical wall lower
        (750, 100, 10, 500),  # Right side vertical wall lower
        (150, 500, 600, 10),  # Bottom horizontal wall shifted right
        (350, 0, 10, 300),  # Middle vertical wall higher
        (250, 300, 500, 10),  # Middle horizontal wall higher
    ],
    [  # Level 3
        (0, 0, 10, 600),
        (0, 0, 800, 10),
        (790, 0, 10, 600),
        (0, 590, 800, 10),
        (100, 0, 10, 550),  # Tall vertical wall near left
        (700, 50, 10, 550),  # Tall vertical wall near right
        (200, 50, 600, 10),  # Top horizontal wall near top
        (200, 540, 600, 10),  # Bottom horizontal wall near bottom
        (400, 50, 10, 490),  # Center vertical wall full height
        (300, 270, 200, 10),  # Short horizontal wall center
    ]
]


def draw_walls(screen, walls):
    for wall in walls:
        pygame.draw.rect(screen, black, pygame.Rect(wall))

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def show_message(level):
    text = f"Level {level} complete!"
    options = ["Replay", "Next Level"] if level < len(levels) else ["Replay", "Quit Game"]
    return show_dialog(text, options)

def show_dialog(text, options):
    dialog_rect = pygame.Rect((250, 200), (300, 200))
    dialog_box = pygame_gui.windows.UIConfirmationDialog(rect=dialog_rect,
                                                         manager=manager,
                                                         window_title="Level Complete",
                                                         action_long_desc=text,
                                                         buttons=options)
    return dialog_box

def next_level(current_level):
    return (current_level + 1) % len(levels)

# Game loop variables
current_level = 0
walls = levels[current_level]
running = True
dialog_open = False
dialog_result = None

# Game loop
while running:
    time_delta = clock.tick(fps)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)
        if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
            dialog_open = False
            if event.ui_element.text == "Next Level":
                current_level = next_level(current_level)
                player_pos = [50, 50]  # Reset player position
            elif event.ui_element.text == "Quit Game":
                running = False
            walls = levels[current_level]

    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Prevent walking through walls
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    for wall in walls:
        wall_rect = pygame.Rect(wall)
        if check_collision(player_rect, wall_rect):
            if keys[pygame.K_LEFT]:
                player_pos[0] += player_speed
            if keys[pygame.K_RIGHT]:
                player_pos[0] -= player_speed
            if keys[pygame.K_UP]:
                player_pos[1] += player_speed
            if keys[pygame.K_DOWN]:
                player_pos[1] -= player_speed

    # Check if reached destination
    destination_rect = pygame.Rect(destination_pos[0], destination_pos[1], 50, 50)
    if player_rect.colliderect(destination_rect) and not dialog_open:
        dialog_open = True
        show_message(current_level + 1)

    # Drawing
    screen.blit(background, (0, 0))  # Draw the background
    draw_walls(screen, walls)
    screen.blit(hospital, destination_pos)
    screen.blit(player_image, player_pos)
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
