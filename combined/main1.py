import pygame
import sys
from moviepy.editor import VideoFileClip
from moviepy.editor import TextClip
import subprocess
from moviepy.editor import VideoFileClip
import numpy as np

# import main2

pygame.init()

pygame.mixer.init()  # Initialize the mixer
pygame.mixer.music.load('background_music.mp3')  # Load your background music file

pygame.mixer.music.play(-1)  # Play the music on loop (-1 means infinite loop)

pygame.mixer.music.set_volume(.7)  # Set the volume to 50%



# Set up the display
WINDOW_WIDTH, WINDOW_HEIGHT = 798, 702
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Animal Rescue Quest")

# Load images
background_image = pygame.image.load("background.gif")
play_button_image = pygame.image.load("play_button.png")
animal_button_image = pygame.image.load("animal_button.gif")
bird_button_image = pygame.image.load("bird_button.gif")
back_button_image = pygame.image.load("back_button.png")  # Load back button image

# Scale the play button to fit a smaller portion of the screen
play_button_size = min(WINDOW_WIDTH, WINDOW_HEIGHT) // 5
play_button_image = pygame.transform.scale(play_button_image, (play_button_size, play_button_size))

# Create circular mask for play button
play_button_mask = pygame.Surface((play_button_size, play_button_size), pygame.SRCALPHA)
pygame.draw.circle(play_button_mask, (255, 255, 255, 255), (play_button_size // 2, play_button_size // 2), play_button_size // 2)

# Apply mask to play_button_image
play_button_image.blit(play_button_mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

# Scale animal, bird, and back buttons
button_size = min(WINDOW_WIDTH, WINDOW_HEIGHT) // 5
animal_button_image = pygame.transform.scale(animal_button_image, (button_size, button_size))
bird_button_image = pygame.transform.scale(bird_button_image, (button_size, button_size))
back_button_image = pygame.transform.scale(back_button_image, (button_size * 3 // 4, button_size * 3 // 4))  # Scale back button image to 75%
injured_animal_image = pygame.image.load("injured_animal.png")  # Load injured animal image
injured_bird_image = pygame.image.load("injured_bird.png")  # Load injured animal image
# Create circular mask for back button
back_button_mask = pygame.Surface((button_size * 3 // 4, button_size * 3 // 4), pygame.SRCALPHA)
pygame.draw.circle(back_button_mask, (255, 255, 255, 255), (button_size * 3 // 8, button_size * 3 // 8), button_size * 3 // 8)

# Apply mask to back_button_image
back_button_image.blit(back_button_mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

# Fonts
font = pygame.font.SysFont("Algerian", 64)

# Function to display text
def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to draw buttons
def draw_button(image, x, y):
    screen.blit(image, (x, y))

# Function to check if a button is clicked
def is_button_clicked(button_rect, pos):
    x, y = pos
    if button_rect.collidepoint(x, y):
        return True
    return False

# Main menu
def main_menu():
    pygame.init()
    blink = False
    blink_timer = pygame.time.get_ticks()
    while True:
        screen.blit(background_image, (0, 0))
        # Position the play button at approximately 65% down the screen
        draw_button(play_button_image, (WINDOW_WIDTH - play_button_size) // 2, int(WINDOW_HEIGHT * 0.65) - play_button_size // 2)

        # Calculate the y-coordinate for the caption at approximately 35% from the top
        caption_y = int(0.35 * WINDOW_HEIGHT)

        # Blinking caption "Animal Rescue Quest"
        if pygame.time.get_ticks() - blink_timer > 250:
            blink = not blink
            blink_timer = pygame.time.get_ticks()
        if blink:
            display_text("Animal Rescue Quest", font, (255, 255, 255), WINDOW_WIDTH // 2, caption_y)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_button_clicked(pygame.Rect((WINDOW_WIDTH - play_button_size) // 2, int(WINDOW_HEIGHT * 0.65) - play_button_size // 2, play_button_size, play_button_size), pygame.mouse.get_pos()):
                    health = 100
                    gameplay(health)


def gameplay(health):
    show_injured_animal = False

    while True:
        screen.blit(background_image, (0, 0))

        # Display health at the top of the screen
        chalkboard_font = pygame.font.SysFont("Algerian", 32)
        display_text("Animal or bird? Pick your favorite!", chalkboard_font, (255, 255, 255), WINDOW_WIDTH // 2, 100)

        # Position the back button at approximately 10% down the screen
        draw_button(back_button_image, 20, 20)

        # Position the animal button at approximately 15% down the screen
        draw_button(animal_button_image, (WINDOW_WIDTH - button_size) // 2, int(WINDOW_HEIGHT * 0.45) - button_size // 2)

        # Position the bird button at approximately 55% down the screen
        draw_button(bird_button_image, (WINDOW_WIDTH - button_size) // 2, int(WINDOW_HEIGHT * 0.80) - button_size // 2)
        # Load and scale watch video button
        watch_video_button_image = pygame.image.load("watch_video.png")
        watch_video_button_size = int(min(WINDOW_WIDTH, WINDOW_HEIGHT) // 8 * 1.5)  # Increase size by 20%
        watch_video_button_image = pygame.transform.scale(watch_video_button_image, (watch_video_button_size, watch_video_button_size))
        # Position the watch video button at the bottom right corner
        watch_video_button_x = WINDOW_WIDTH - watch_video_button_size - 20
        watch_video_button_y = WINDOW_HEIGHT - watch_video_button_size - 20
        draw_button(watch_video_button_image, watch_video_button_x, watch_video_button_y)

        # Display caption "watch video" below the watch video button
        watch_video_caption_font = pygame.font.SysFont("Algerian", 16)
        watch_video_caption_color = (255, 255, 255)
        watch_video_caption_text = "Watch Video"
        watch_video_caption_text_surface = watch_video_caption_font.render(watch_video_caption_text, True, watch_video_caption_color)
        watch_video_caption_text_rect = watch_video_caption_text_surface.get_rect()
        watch_video_caption_text_rect.midtop = (watch_video_button_x + watch_video_button_size // 2, watch_video_button_y + watch_video_button_size + 5)
        screen.blit(watch_video_caption_text_surface, watch_video_caption_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_button_clicked(pygame.Rect(20, 20, button_size * 3 // 4, button_size * 3 // 4), pygame.mouse.get_pos()):
                    return  # Return to main menu

                elif is_button_clicked(pygame.Rect((WINDOW_WIDTH - button_size) // 2, int(WINDOW_HEIGHT * 0.45) - button_size // 2, button_size, button_size), pygame.mouse.get_pos()):
                    subprocess.Popen(["python3", "main4.py"])  # Reset flag after displaying injured animal
                        # subprocess.Popen(["python3", "main2.py"])
                    pygame.quit()


                elif is_button_clicked(pygame.Rect((WINDOW_WIDTH - button_size) // 2, int(WINDOW_HEIGHT * 0.80) - button_size // 2, button_size, button_size), pygame.mouse.get_pos()):
                    # print("Bird button clicked. Transition to main2.py.")
                    subprocess.Popen(["python3", "main5.py"])
                    pygame.quit()

                elif is_button_clicked(pygame.Rect(WINDOW_WIDTH - watch_video_button_size - 20, WINDOW_HEIGHT - watch_video_button_size - 20, watch_video_button_size, watch_video_button_size), pygame.mouse.get_pos()):
                     # Handle click action for watch video button
                     # Usage
                     play_video_pygame('The_Bitter_Bond.mp4', screen, back_button_image)




def play_video_pygame(video_path, screen, back_button_image):
    # Load video
    pygame.mixer.music.pause()
    clip = VideoFileClip(video_path)
    video = clip.resize(newsize=(screen.get_width(), screen.get_height()))  # Resize video to screen size
    
    # Prepare the back button
    back_button_rect = back_button_image.get_rect(topleft=(20, 20))
    
    # Load and play background music
    pygame.mixer.init()
    background_music = pygame.mixer.Sound("The_Bitter_Bond.wav")
    background_music.play(-1)  # Play background music on loop
    # fp = clip.fps
    # print("fps  = ",fp)
    # print("fps of audio", background_music.fps)
    try:
        # Video playback
        for frame in video.iter_frames(fps=clip.fps*16, dtype='uint8'):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button_rect.collidepoint(event.pos):
                        background_music.stop()
                        pygame.mixer.music.unpause()
                        return  # Exit video playback early

            # Convert the video frame to a Pygame surface
            frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            screen.blit(frame_surface, (0, 0))
            screen.blit(back_button_image, back_button_rect.topleft)
            pygame.display.flip()

    finally:
        # Clean up: Stop background music and close video clip
        background_music.stop()
        clip.close()

    # Ensure background music resumes after video playback
    pygame.mixer.music.unpause()
        

# Run the game
if __name__ == "__main__":
    main_menu()
