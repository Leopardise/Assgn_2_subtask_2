import pygame
import sys
from moviepy.editor import VideoFileClip
from moviepy.editor import TextClip

pygame.init()

pygame.mixer.init()  # Initialize the mixer
pygame.mixer.music.load('background_music.mp3')  # Load your background music file

pygame.mixer.music.play(-1)  # Play the music on loop (-1 means infinite loop)

pygame.mixer.music.set_volume(.7)  # Set the volume to 50%


# Set up the display
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pet Rescue Quest")

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
    blink = False
    blink_timer = pygame.time.get_ticks()
    while True:
        screen.blit(background_image, (0, 0))
        # Position the play button at approximately 65% down the screen
        draw_button(play_button_image, (WINDOW_WIDTH - play_button_size) // 2, int(WINDOW_HEIGHT * 0.65) - play_button_size // 2)

        # Calculate the y-coordinate for the caption at approximately 35% from the top
        caption_y = int(0.35 * WINDOW_HEIGHT)

        # Blinking caption "Pet Rescue Quest"
        if pygame.time.get_ticks() - blink_timer > 250:
            blink = not blink
            blink_timer = pygame.time.get_ticks()
        if blink:
            display_text("Pet Rescue Quest", font, (255, 255, 255), WINDOW_WIDTH // 2, caption_y)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_button_clicked(pygame.Rect((WINDOW_WIDTH - play_button_size) // 2, int(WINDOW_HEIGHT * 0.65) - play_button_size // 2, play_button_size, play_button_size), pygame.mouse.get_pos()):
                    health = 100
                    gameplay(health)

# Gameplay screen
def gameplay(health):
    while True:
        screen.blit(background_image, (0, 0))
        chalkboard_font = pygame.font.SysFont("Algerian", 32)
        # Display health at the top of the screen
        display_text(f"Health: {health}%", chalkboard_font, (255, 255, 255), WINDOW_WIDTH // 2, 100)
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
                # Check if back button clicked
                if is_button_clicked(pygame.Rect(20, 20, button_size * 3 // 4, button_size * 3 // 4), pygame.mouse.get_pos()):
                    main_menu()  # Return to main menu
                # Check if animal button clicked
                elif is_button_clicked(pygame.Rect((WINDOW_WIDTH - button_size) // 2, int(WINDOW_HEIGHT * 0.45) - button_size // 2, button_size, button_size), pygame.mouse.get_pos()):
                    # Here, you would transition to main2.py or call its main function
                    print("Animal button clicked. Transition to main2.py.")
                # Check if bird button clicked
                elif is_button_clicked(pygame.Rect((WINDOW_WIDTH - button_size) // 2, int(WINDOW_HEIGHT * 0.80) - button_size // 2, button_size, button_size), pygame.mouse.get_pos()):
                    # Here, you would transition to main2.py or call its main function
                    print("Bird button clicked. Transition to main2.py.")
                # Check if watch video button clicked
                elif is_button_clicked(pygame.Rect(WINDOW_WIDTH - watch_video_button_size - 20, WINDOW_HEIGHT - watch_video_button_size - 20, watch_video_button_size, watch_video_button_size), pygame.mouse.get_pos()):
                    # Handle click action for watch video button
                    play_video()

def play_video():
    # Create a separate display surface for video playback
    video_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pet Rescue Quest")  # Set window title
    clip = VideoFileClip("watch.mp4")


    # # Set the position of the back button
    # back_button_position = (20, 20)
    # # Blit the back button image to the screen at the specified position
    # screen.blit(back_button_image, back_button_position)
    #
    # # Inside the event loop
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         sys.exit()
    #     elif event.type == pygame.MOUSEBUTTONDOWN:
    #         mouse_pos = pygame.mouse.get_pos()
    #         if is_button_clicked(pygame.Rect((WINDOW_WIDTH - play_button_size) // 2, int(WINDOW_HEIGHT * 0.65) - play_button_size // 2, play_button_size, play_button_size), pygame.mouse.get_pos()):
    #             gameplay(100)  # Call the gameplay(100) method when the back button is clicked



    # Fit the video to the window size
    scaled_clip = clip.resize((WINDOW_WIDTH, WINDOW_HEIGHT))
    # Get frames of the video
    frames = scaled_clip.iter_frames(fps=1500)  # Adjusted frame rate (decreased by 20%)
    # Loop through frames and display them on the video screen
    for frame in frames:
        # Convert the frame to a format Pygame can use
        frame_surface = pygame.image.frombuffer(frame, (WINDOW_WIDTH, WINDOW_HEIGHT), 'RGB')
        video_screen.blit(frame_surface, (0, 0))
        # Create a text surface
        # text_content = """
        # In shadows deep, where wild hearts quake,
        # Beneath the weight of mankind's wake,
        # Innocent eyes meet cruel fate's decree,
        # As pain and sorrow grip each plea.
        #
        # Yet in the hearts of those who see,
        # A sanctuary born, a refuge free,
        # For creatures battered, broken, torn,
        # A haven found, where hope is sworn.
        #
        # To those who tend with gentle hand,
        # To creatures of the earth and sand,
        # Reward is due for love untold,
        # True nature's stewards, brave and bold.
        # """
        # text_surface = pygame.font.SysFont("Algerian", 20).render(text_content, True, (255, 255, 255))
        # text_rect = pygame.Rect(
        #     (WINDOW_WIDTH / 2 - text_surface.get_width() / 2),
        #     (WINDOW_HEIGHT / 2 - text_surface.get_height() / 2),
        #     text_surface.get_width(),
        #     text_surface.get_height(),
        # )
        # video_screen.blit(text_surface, text_rect)

        # Update the display
        pygame.display.flip()
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# Run the game
if __name__ == "__main__":
    main_menu()
