import pygame
import pygame_gui
import sys

# Initialize Pygame and Pygame GUI
pygame.init()
pygame.display.set_caption('Complex Maze Game')

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
manager = pygame_gui.UIManager(window_size)
background_image = pygame.image.load('city.jpg').convert()
background = pygame.transform.scale(background_image, (800, 600))
player_image = pygame.image.load('person.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (30, 30))
hospital_image = pygame.image.load('hospital.jpg').convert()
hospital = pygame.transform.scale(hospital_image, (50, 50))

# Game configurations
player_pos = [50, 50]
destination_pos = [700, 500]
player_speed = 5
levels = [
    [
        (0, 0, 10, 600), (0, 0, 800, 10), (790, 0, 10, 600), (0, 590, 800, 10),
        (100, 50, 10, 500), (100, 50, 500, 10), (300, 100, 10, 500), (200, 500, 500, 10), (700, 50, 10, 450), (400, 250, 280, 10)
    ],
    [
        (0, 0, 10, 600), (0, 0, 800, 10), (790, 0, 10, 600), (0, 590, 800, 10),
        (50, 100, 700, 10), (150, 0, 10, 500), (750, 100, 10, 500), (150, 500, 600, 10), (350, 0, 10, 300), (250, 300, 500, 10)
    ],
    [
        (0, 0, 10, 600), (0, 0, 800, 10), (790, 0, 10, 600), (0, 590, 800, 10),
        (100, 0, 10, 550), (700, 50, 10, 550), (200, 50, 600, 10), (200, 540, 600, 10), (400, 50, 10, 490), (300, 270, 200, 10)
    ]
]
current_level = 0
walls = levels[current_level]

# Game functions
def draw_walls():
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(wall))

def check_collision(player_rect):
    for wall in walls:
        if player_rect.colliderect(pygame.Rect(wall)):
            return True
    return False

def show_dialog(text, buttons):
    dialog_rect = pygame.Rect((200, 200), (400, 200))
    return pygame_gui.windows.UIConfirmationDialog(rect=dialog_rect,
                                                   manager=manager,
                                                   window_title="Level Complete",
                                                   action_long_desc=text,
                                                   button_text={"ok": buttons[0], "cancel": buttons[1]})

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        manager.process_events(event)

        if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
            if event.ui_element.ok_pressed:
                if event.ui_object_id == "#confirmation_dialog.ok_button":
                    if event.text == "Next Level":
                        current_level = (current_level + 1) % len(levels)
                        walls = levels[current_level]
                        player_pos = [50, 50]
                    elif event.text == "Replay":
                        player_pos = [50, 50]
                    elif event.text == "Quit Game":
                        is_running = False
            elif event.ui_element.cancel_pressed:
                is_running = False

    keys = pygame.key.get_pressed()
    new_pos = player_pos[:]
    if keys[pygame.K_LEFT]:
        new_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        new_pos[0] += player_speed
    if keys[pygame.K_UP]:
        new_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        new_pos[1] += player_speed

    player_rect = pygame.Rect(new_pos[0], new_pos[1], 30, 30)
    if not check_collision(player_rect):
        player_pos = new_pos

    if pygame.Rect(player_pos[0], player_pos[1], 30, 30).colliderect(pygame.Rect(destination_pos[0], destination_pos[1], 50, 50)):
        options = ["Replay", "Next Level"] if current_level < 2 else ["Replay", "Quit Game"]
        show_dialog(f"Level {current_level + 1} Complete!", options)

    screen.blit(background, (0, 0))
    draw_walls()
    screen.blit(hospital, destination_pos)
    screen.blit(player_image, player_pos)
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.update()

pygame.quit()
sys.exit()
