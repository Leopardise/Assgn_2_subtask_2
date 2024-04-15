import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Resolution & Display
WINDOW_WIDTH = 798
WINDOW_HEIGHT = 600

SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption('Animal Rescue Quest')

# Grid Settings
BLOCK_WIDTH = 266
BLOCK_HEIGHT = 200

# RGB Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (250, 250, 250)

game_state = "tile_game_1"

# Function to load and scale images
def load_and_scale_image(filename):
  image = pygame.image.load(filename).convert_alpha() # Load image
  return pygame.transform.scale(image, (int(BLOCK_WIDTH), int(BLOCK_HEIGHT)))

# Load Images
images = [
  load_and_scale_image("0.jpg"),
  load_and_scale_image("1.jpg"),
  load_and_scale_image("2.jpg"),
  load_and_scale_image("3.jpg"),
  load_and_scale_image("4.jpg"),
  load_and_scale_image("5.jpg"),
  load_and_scale_image("6.jpg"),
  load_and_scale_image("7.jpg"),
  load_and_scale_image("8.jpg")
]

# Load Images for the second window
images_2 = [
    load_and_scale_image("10.jpg"),
    load_and_scale_image("12.jpg"),
    load_and_scale_image("9.jpg"),
    load_and_scale_image("14.jpg"),
    load_and_scale_image("4.jpg"),
    load_and_scale_image("1.jpg"),
    load_and_scale_image("13.jpg"),
    load_and_scale_image("3.jpg"),
    load_and_scale_image("11.jpg")
]

# Load Images for the second window
images_3 = [
    load_and_scale_image("3.jpg"),
    load_and_scale_image("11.jpg"),
    load_and_scale_image("5.jpg"),
    load_and_scale_image("6.jpg"),
    load_and_scale_image("4.jpg"),
    load_and_scale_image("8.jpg"),
    load_and_scale_image("15.jpg"),
    load_and_scale_image("16.jpg"),
    load_and_scale_image("17.jpg")
]

# Load Images for the second window
images_4 = [
    load_and_scale_image("20.jpg"),
    load_and_scale_image("0.jpg"),
    load_and_scale_image("1.jpg"),
    load_and_scale_image("19.jpg"),
    load_and_scale_image("4.jpg"),
    load_and_scale_image("11.jpg"),
    load_and_scale_image("18.jpg"),
    load_and_scale_image("6.jpg"),
    load_and_scale_image("7.jpg")
]

# Load Images for the second window
images_5 = [
    load_and_scale_image("1.jpg"),
    load_and_scale_image("2.jpg"),
    load_and_scale_image("21.jpg"),
    load_and_scale_image("11.jpg"),
    load_and_scale_image("4.jpg"),
    load_and_scale_image("22.jpg"),
    load_and_scale_image("7.jpg"),
    load_and_scale_image("8.jpg"),
    load_and_scale_image("23.jpg")
]

# Load back image and scale it down to 75% of its original size
back_image = pygame.image.load("back_1.jpg").convert()
new_width = int(WINDOW_WIDTH * 0.95)
new_height = int(WINDOW_HEIGHT * 0.95)
back_image = pygame.transform.scale(back_image, (new_width, new_height))

# Calculate the coordinates to blit the image at the center of the screen
back_x = (WINDOW_WIDTH - new_width) // 2
back_y = (WINDOW_HEIGHT - new_height) // 2

def display_caution_screen():
  SCREEN.blit(back_image, (back_x, back_y))
  font = pygame.font.SysFont("Algerian", 50)
  text = font.render('Caution: Danger within 1km', True, WHITE)
  text_rect = text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
  SCREEN.blit(text, text_rect)

  # Load and scale the back button image
  back_button_image = pygame.image.load("back_button.png").convert_alpha()
  back_button_image = pygame.transform.scale(back_button_image, (50, 50))

  # Calculate the position to blit the back button (top left corner)
  button_x = 20
  button_y = 20

  # Blit the back button onto the screen
  SCREEN.blit(back_button_image, (button_x, button_y))

  # Check for mouse click on the back button
  mouse_x, mouse_y = pygame.mouse.get_pos()
  if button_x < mouse_x < button_x + 50 and button_y < mouse_y < button_y + 50:
    if pygame.mouse.get_pressed()[0]: # Check for left mouse button click
      return False # Signal to move back to the tile window

  return True # Continue displaying the caution screen


def draw_grid(images):
  for x in range(0, WINDOW_WIDTH, int(BLOCK_WIDTH)):
    for y in range(0, WINDOW_HEIGHT, int(BLOCK_HEIGHT)):
      rect = pygame.Rect(x, y, int(BLOCK_WIDTH), int(BLOCK_HEIGHT))
      pygame.draw.rect(SCREEN, WHITE, rect, 1)

      # Calculate image index based on tile position
      image_index = (y // BLOCK_HEIGHT) * 3 + (x // BLOCK_WIDTH)
      SCREEN.blit(images[image_index], (x, y)) # Display the image



def mouse_pos():
  # Takes the mouse position and, if over a tile, returns the tile index relative to the board list
  pos = pygame.mouse.get_pos()
  x = pos[0] // BLOCK_WIDTH
  y = pos[1] // BLOCK_HEIGHT

  return x, y

running = True
caution_screen = False
image_index = -1

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONUP:
      if caution_screen:
        continue
      x, y = mouse_pos()
      image_index = y * 3 + x
      if image_index == 0 and game_state == "tile_game_3":  # Clicked on 0.jpg
        game_state = "tile_game_1"
      elif image_index == 0 and game_state == "tile_game_1":  # Clicked on 0.jpg
        game_state = "tile_game_2"
      elif image_index == 7 and game_state == "tile_game_1":  # Clicked on 0.jpg
        game_state = "tile_game_4"
      elif image_index == 3 and game_state == "tile_game_1":  # Clicked on 0.jpg
        game_state = "tile_game_5"
      elif image_index == 5 and game_state == "tile_game_1":  # Clicked on 0.jpg
        game_state = "tile_game_6"
      elif image_index == 6 or image_index == 8 and game_state == "tile_game_1":
        game_state = "tile_game_3"
        caution_screen = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False

  SCREEN.fill(BACKGROUND_COLOR)

  if caution_screen:
    caution_screen = display_caution_screen()
    if not caution_screen:
        caution_screen = False

  elif game_state == "tile_game_1":
        draw_grid(images)
  elif game_state == "tile_game_2":
        draw_grid(images_2)
  elif game_state == "tile_game_4":
        draw_grid(images_3)
  elif game_state == "tile_game_5":
        draw_grid(images_4)
  elif game_state == "tile_game_6":
        draw_grid(images_5)

  pygame.display.flip()

pygame.quit()
sys.exit()
