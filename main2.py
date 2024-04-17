import pygame
import sys
import time
import subprocess
import tkinter as tk
from tkinter import messagebox

# Initialize Pygame
pygame.init()

pygame.mixer.init()  # Initialize the mixer
pygame.mixer.music.load('background_music.mp3')  # Load your background music file

pygame.mixer.music.play(-1)  # Play the music on loop (-1 means infinite loop)

pygame.mixer.music.set_volume(.7)  # Set the volume to 50%


# Resolution & Display
WINDOW_WIDTH = 798
WINDOW_HEIGHT = 702

SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption('Animal Rescue Quest')

# Grid Settings
BLOCK_WIDTH = 266
BLOCK_HEIGHT = 266

# RGB Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (250, 250, 250)

game_state = "tile_game_1"
health = 100
my_font = pygame.font.SysFont('Algerian', 20)

def restart_game():
  subprocess.Popen(['python3', 'main1.py'])
  pygame.quit()
  sys.exit()
  
def display_health():
    # Render health information
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"HEALTH: {health}", True, WHITE)
    text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, 50))
    SCREEN.blit(text_surface, text_rect)
  
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
  load_and_scale_image("player4.jpg"),
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
    load_and_scale_image("20.jpg"),
    load_and_scale_image("player4.jpg"),
    load_and_scale_image("1.jpg"),
    load_and_scale_image("19.jpg"),
    load_and_scale_image("3.jpg"),
    load_and_scale_image("11.jpg")
]

# Load Images for the second window
images_3 = [
    load_and_scale_image("3.jpg"),
    load_and_scale_image("11.jpg"),
    load_and_scale_image("5.jpg"),
    load_and_scale_image("6.jpg"),
    load_and_scale_image("player4.jpg"),
    load_and_scale_image("8.jpg"),
    load_and_scale_image("hunter15.jpg"),
    load_and_scale_image("16.jpg"),
    load_and_scale_image("hunter17.jpg")
]

# Load Images for the second window
images_4 = [
    load_and_scale_image("20.jpg"),
    load_and_scale_image("0.jpg"),
    load_and_scale_image("1.jpg"),
    load_and_scale_image("19.jpg"),
    load_and_scale_image("player4.jpg"),
    load_and_scale_image("11.jpg"),
    load_and_scale_image("wolf18.jpg"),
    load_and_scale_image("6.jpg"),
    load_and_scale_image("7.jpg")
]

# Load Images for the second window
images_5 = [
    load_and_scale_image("1.jpg"),
    load_and_scale_image("2.jpg"),
    load_and_scale_image("21.jpg"),
    load_and_scale_image("11.jpg"),
    load_and_scale_image("player4.jpg"),
    load_and_scale_image("22.jpg"),
    load_and_scale_image("7.jpg"),
    load_and_scale_image("8.jpg"),
    load_and_scale_image("23.jpg")
]

# Load Images for the second window
images_6 = [
    load_and_scale_image("9.jpg"),
    load_and_scale_image("13.jpg"),
    load_and_scale_image("14.jpg"),
    load_and_scale_image("1.jpg"),
    load_and_scale_image("player4.jpg"),
    load_and_scale_image("21.jpg"),
    load_and_scale_image("11.jpg"),
    load_and_scale_image("5.jpg"),
    load_and_scale_image("22.jpg")
]

# Load Images
images_7 = [
  load_and_scale_image("12.jpg"),
  load_and_scale_image("9.jpg"),
  load_and_scale_image("13.jpg"),
  load_and_scale_image("0.jpg"),
  load_and_scale_image("player4.jpg"),
  load_and_scale_image("2.jpg"),
  load_and_scale_image("3.jpg"),
  load_and_scale_image("11.jpg"),
  load_and_scale_image("5.jpg")
]

# Load Images
images_1 = [
  load_and_scale_image("50.jpg"),
  load_and_scale_image("51.jpg"),
  load_and_scale_image("52.jpg"),
  load_and_scale_image("53.jpg"),
  load_and_scale_image("hunter15.jpg"),
  load_and_scale_image("54.jpg"),
  load_and_scale_image("55.jpg"),
  load_and_scale_image("56.jpg"),
  load_and_scale_image("57.jpg")
]

# Load Images for the second window
images_8 = [
    load_and_scale_image("24.jpg"),
    load_and_scale_image("10.jpg"),
    load_and_scale_image("12.jpg"),
    load_and_scale_image("u.jpg"),
    load_and_scale_image("player4.jpg"),
    load_and_scale_image("0.jpg"),
    load_and_scale_image("25.jpg"),
    load_and_scale_image("19.jpg"),
    load_and_scale_image("3.jpg")
]

# Load Images for the second window
images_9 = [
    load_and_scale_image("u.jpg"),
    load_and_scale_image("26.jpg"),
    load_and_scale_image("27.jpg"),
    load_and_scale_image("24.jpg"),
    load_and_scale_image("player4.jpg"),
    load_and_scale_image("12.jpg"),
    load_and_scale_image("u.jpg"),
    load_and_scale_image("20.jpg"),
    load_and_scale_image("0.jpg")
]

# Load Images
images_10 = [
  load_and_scale_image("26.jpg"),
  load_and_scale_image("27.jpg"),
  load_and_scale_image("m.jpg"),
  load_and_scale_image("10.jpg"),
  load_and_scale_image("player4.jpg"),
  load_and_scale_image("9.jpg"),
  load_and_scale_image("20.jpg"),
  load_and_scale_image("0.jpg"),
  load_and_scale_image("1.jpg")
]

# Load Images
images_11 = [
  load_and_scale_image("27.jpg"),
  load_and_scale_image("m.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("12.jpg"),
  load_and_scale_image("player4.jpg"),
  load_and_scale_image("13.jpg"),
  load_and_scale_image("0.jpg"),
  load_and_scale_image("1.jpg"),
  load_and_scale_image("2.jpg")
]

# Load Images
images_12 = [
  load_and_scale_image("u.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("13.jpg"),
  load_and_scale_image("player4.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("2.jpg"),
  load_and_scale_image("21.jpg"),
  load_and_scale_image("u.jpg")
]

# Load Images
images_13 = [
  load_and_scale_image("13.jpg"),
  load_and_scale_image("14.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("2.jpg"),
  load_and_scale_image("player4.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("3.jpg"),
  load_and_scale_image("22.jpg"),
  load_and_scale_image("u.jpg")
]

# Load Images
images_14 = [
  load_and_scale_image("2.jpg"),
  load_and_scale_image("21.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("5.jpg"),
  load_and_scale_image("player4.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("8.jpg"),
  load_and_scale_image("23.jpg"),
  load_and_scale_image("u.jpg")
]

# Load Images
images_15 = [
  load_and_scale_image("19.jpg"),
  load_and_scale_image("3.jpg"),
  load_and_scale_image("11.jpg"),
  load_and_scale_image("wolf18.jpg"),
  load_and_scale_image("player4.jpg"),
  load_and_scale_image("7.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("hunter15.jpg"),
  load_and_scale_image("u.jpg")
]

# Load Images
images_16 = [
  load_and_scale_image("5.jpg"),
  load_and_scale_image("22.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("8.jpg"),
  load_and_scale_image("player4.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("hunter17.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("u.jpg")
]

# Load Images
images_17 = [
  load_and_scale_image("u.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("20.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("player4.jpg"),
  load_and_scale_image("19.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("u.jpg"),
  load_and_scale_image("wolf18.jpg")
]


def draw_grid(images):
  for x in range(0, WINDOW_WIDTH, int(BLOCK_WIDTH)):
    for y in range(0, WINDOW_HEIGHT, int(BLOCK_HEIGHT)):
      rect = pygame.Rect(x, y, int(BLOCK_WIDTH), int(BLOCK_HEIGHT))
      pygame.draw.rect(SCREEN, WHITE, rect, 1)

      # Calculate image index based on tile position
      image_index = (y // BLOCK_HEIGHT) * 3 + (x // BLOCK_WIDTH)
      SCREEN.blit(images[image_index], (x, y)) # Display the image

      if image_index == 4:
        original_font_size = 20
        new_font_size = int(original_font_size * 1.71)
        scaled_font = pygame.font.SysFont(None, new_font_size)
        health_text = scaled_font.render(f"HEALTH: {health}", True, WHITE)
        
        text_rect = health_text.get_rect(center=(x+BLOCK_WIDTH//2, y+BLOCK_HEIGHT//2))
        SCREEN.blit(health_text, text_rect)

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
      # if image_index == 0 and game_state == "tile_game_3":  # Clicked on 0.jpg
      #   game_state = "tile_game_1"
      print(game_state)
      if (image_index == 0 and game_state == "tile_game_1") or (image_index == 3 and game_state == "tile_game_8") or (image_index == 1 and game_state == "tile_game_5") or (image_index == 6 and game_state == "tile_game_12") or (image_index == 8 and game_state == "tile_game_10") or (image_index == 5 and game_state == "tile_game_9"):  # Clicked on 0.jpg
        game_state = "tile_game_2"
      elif (image_index == 7 and game_state == "tile_game_1") or (image_index == 8 and game_state == "tile_game_5") or (image_index == 6 and game_state == "tile_game_6") or (image_index == 5 and game_state == "tile_game_3") or (image_index == 3 and game_state == "tile_game_18"):  # Clicked on 0.jpg
        game_state = "tile_game_4"
      elif (image_index == 3 and game_state == "tile_game_1") or (image_index == 7 and game_state == "tile_game_2") or (image_index == 6 and game_state == "tile_game_8") or (image_index == 1 and game_state == "tile_game_3") or (image_index == 0 and game_state == "tile_game_4") or (image_index == 1 and game_state == "tile_game_18") or (image_index == 8 and game_state == "tile_game_9") or (image_index == 2 and game_state == "tile_game_16"):  # Clicked on 0.jpg
        game_state = "tile_game_5"
      elif (image_index == 5 and game_state == "tile_game_1") or (image_index == 8 and game_state == "tile_game_8") or (image_index == 7 and game_state == "tile_game_7") or (image_index == 2 and game_state == "tile_game_4") or (image_index == 6 and game_state == "tile_game_14") or (image_index == 0 and game_state == "tile_game_17") or (image_index == 3 and game_state == "tile_game_15"):  # Clicked on 0.jpg
        game_state = "tile_game_6"
      elif (image_index == 2 and game_state == "tile_game_1") or (image_index == 5 and game_state == "tile_game_8") or (image_index == 1 and game_state == "tile_game_6") or (image_index == 6 and game_state == "tile_game_13") or (image_index == 3 and game_state == "tile_game_14") or (image_index == 0 and game_state == "tile_game_15") or (image_index == 8 and game_state == "tile_game_12"):  # Clicked on 0.jpg
        game_state = "tile_game_7"
      elif (image_index == 1 and game_state == "tile_game_1") or (image_index == 5 and game_state == "tile_game_2") or (image_index == 3 and game_state == "tile_game_7") or (image_index == 2 and game_state == "tile_game_5") or (image_index == 0 and game_state == "tile_game_6") or (image_index == 7 and game_state == "tile_game_12"):  # Clicked on 0.jpg
        game_state = "tile_game_8"
      elif (image_index == 6 and game_state == "tile_game_1") or (image_index == 7 and game_state == "tile_game_5") or (image_index == 3 and game_state == "tile_game_4") or (image_index == 5 and game_state == "tile_game_16"):
        game_state = "tile_game_3"
      elif (image_index == 8 and game_state == "tile_game_1") or (image_index == 7 and game_state == "tile_game_6") or (image_index == 5 and game_state == "tile_game_4") or (image_index == 3 and game_state == "tile_game_17") or (image_index == 6 and game_state == "tile_game_15"):
        game_state = "tile_game_18"
      elif (image_index == 3 and game_state == "tile_game_2") or (image_index == 0 and game_state == "tile_game_5") or (image_index == 7 and game_state == "tile_game_10"):  # Clicked on 0.jpg
        game_state = "tile_game_9"
      elif (image_index == 0 and game_state == "tile_game_2") or (image_index == 1 and game_state == "tile_game_9"):  # Clicked on 0.jpg
        game_state = "tile_game_10"
      elif (image_index == 1 and game_state == "tile_game_2") or (image_index == 0 and game_state == "tile_game_8") or (image_index == 2 and game_state == "tile_game_9"):  # Clicked on 0.jpg
        game_state = "tile_game_11"
      elif (image_index == 2 and game_state == "tile_game_2") or (image_index == 1 and game_state == "tile_game_8") or (image_index == 0 and game_state == "tile_game_7") or (image_index == 5 and game_state == "tile_game_5"):  # Clicked on 0.jpg
        game_state = "tile_game_12"
      elif (image_index == 8 and game_state == "tile_game_2") or (image_index == 7 and game_state == "tile_game_8") or (image_index == 6 and game_state == "tile_game_7") or (image_index == 3 and game_state == "tile_game_6") or (image_index == 2 and game_state == "tile_game_3") or (image_index == 1 and game_state == "tile_game_4") or (image_index == 0 and game_state == "tile_game_18"):  # Clicked on 0.jpg
        game_state = "tile_game_1"
      elif (image_index == 2 and game_state == "tile_game_7") or (image_index == 1 and game_state == "tile_game_14"):  # Clicked on 0.jpg
        game_state = "tile_game_13"
      elif (image_index == 5 and game_state == "tile_game_7") or (image_index == 2 and game_state == "tile_game_6") or (image_index == 7 and game_state == "tile_game_13") or (image_index == 1 and game_state == "tile_game_15"):  # Clicked on 0.jpg
        game_state = "tile_game_14"
      elif (image_index == 8 and game_state == "tile_game_7") or (image_index == 5 and game_state == "tile_game_6") or (image_index == 2 and game_state == "tile_game_18") or (image_index == 7 and game_state == "tile_game_14") or (image_index == 1 and game_state == "tile_game_17"):  # Clicked on 0.jpg
        game_state = "tile_game_15"
      elif (image_index == 6 and game_state == "tile_game_5") or (image_index == 3 and game_state == "tile_game_3"):  # Clicked on 0.jpg
        game_state = "tile_game_16"
      elif (image_index == 8 and game_state == "tile_game_6") or (image_index == 5 and game_state == "tile_game_18") or (image_index == 7 and game_state == "tile_game_15"):  # Clicked on 0.jpg
        game_state = "tile_game_17"
      elif (image_index == 6 and game_state == "tile_game_9") or (image_index == 0 and game_state == "tile_game_16"):
        game_state = "tile_game_19"

      #update health
      health = health - 10
      if health <= 0:
        root = tk.Tk()
        root.withdraw()
        result = 0
        result = messagebox.askquestion("You lose", "Play Again?")
        while result is None:
            pygame.time.wait(100)
        # print("result = ", result)
        if result == "yes":
          restart_game()
        elif result == "no":
          pygame.quit()
          sys.exit()
      
        
          
          
          
      

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False

  SCREEN.fill(BACKGROUND_COLOR)


  if game_state == "tile_game_1":
        draw_grid(images)
  elif game_state == "tile_game_2":
        draw_grid(images_2)
  elif game_state == "tile_game_3":
        draw_grid(images_1)
  elif game_state == "tile_game_18":
        draw_grid(images_1)
  elif game_state == "tile_game_4":
        draw_grid(images_3)
  elif game_state == "tile_game_5":
        draw_grid(images_4)
  elif game_state == "tile_game_6":
        draw_grid(images_5)
  elif game_state == "tile_game_7":
        draw_grid(images_6)
  elif game_state == "tile_game_8":
        draw_grid(images_7)
  elif game_state == "tile_game_9":
        draw_grid(images_8)
  elif game_state == "tile_game_10":
        draw_grid(images_9)
  elif game_state == "tile_game_11":
        draw_grid(images_10)
  elif game_state == "tile_game_12":
        draw_grid(images_11)
  elif game_state == "tile_game_13":
        draw_grid(images_12)
  elif game_state == "tile_game_14":
        draw_grid(images_13)
  elif game_state == "tile_game_15":
        draw_grid(images_14)
        
  elif game_state == "tile_game_16":
        draw_grid(images_15)
  elif game_state == "tile_game_17":
        draw_grid(images_16)
  elif game_state == "tile_game_19":
        draw_grid(images_17)
        
  elif game_state == "not_allowed":
        root = tk.Tk()
        root.withdraw()
        result = messagebox.showinfo("", "Not allowed")
        while result is None:
          pygame.time.wait(100)
        root.destroy()  

  pygame.display.flip()

pygame.quit()
sys.exit()
