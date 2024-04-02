import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Animal:
    def __init__(self, species, health=100):
        self.species = species
        self.health = health

    def feed(self):
        self.health += 10

    def treat(self):
        self.health += 10

    def play(self):
        self.health += 10

class Shelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

# Initialize shelter and animals
shelter = Shelter()
shelter.add_animal(Animal("Animal"))
shelter.add_animal(Animal("Bird"))

# Initialize main window
root = tk.Tk()
root.title("Pet Rescue Quest")
root.geometry("600x600")

# Load and resize images
# gif_frames = []
# for i in range(36):
#     img = Image.open(f"{i}.gif").resize((100, 100), Image.LANCZOS)
#     gif_frames.append(ImageTk.PhotoImage(img))

# Create canvas for displaying GIF matrix

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()


# Initial player position
player_position = (0, 0)

# Function to update player position
def move(direction):
    global player_position
    x, y = player_position
    if direction == "left":
        if x > 0:
            x -= 1
            print(x,y)
    elif direction == "right":
        if x < 5:
            x += 1
            print(x,y)
    elif direction == "up":
        if y > 0:
            y -= 1
            print(x,y)
    elif direction == "down":
        if y < 5:
            y += 1
            print(x,y)
    player_position = (x, y)
    

    update_board()

# Function to check win or lose
def check_status():
    global player_position
    if player_position == (5, 5):  # Assuming the sanctuary is at position (5, 5)
        messagebox.showinfo("Congratulations", "You reached the sanctuary! You win!")
        root.destroy()
    elif shelter.animals[0].health <= 0:
        messagebox.showinfo("Game Over", "Your pet's health reached 0. You lose!")
        root.destroy()

# Function to update the board
# def update_board():
#     canvas.delete("all")
#     cell_size = 100
#     for i in range(6):
#         for j in range(6):
#             idx = i * 6 + j + 30
#             if idx == 9 or idx == 23:
#                 canvas.create_rectangle(i * cell_size, j * cell_size, (i + 1) * 100, (j + 1) * 100, fill="red")
#             elif idx == 3 or idx == 13 or idx == 18 or idx == 27 or idx == 33:
#                 canvas.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill="blue")
#             elif idx == 0 or idx == 6:
#                 canvas.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill="green")
#             else:
#                 canvas.create_image(j * 100 + 50, i * 100 + 50, image=gif_frames[idx])
#     # Draw player
#     player_x, player_y = player_position
#     canvas.create_image((player_x * 100) + 50, (player_y * 100) + 50, image=gif_frames[0])  # Assuming player image index is 0
#     check_status()






# def update_board():
#     canvas.delete("all")
#     cell_size = 100
#     for i in range(6):
#         for j in range(6):
#             color = "white"
#             if (i, j) == player_position:
#                 color = "blue"  # Player's position
#             canvas.create_rectangle(i * cell_size, j * cell_size, (i + 1) * cell_size, (j + 1) * cell_size, fill=color)

# # Create canvas for the game board
# canvas = tk.Canvas(root, width=600, height=600, bg="white")
# canvas.pack()

# Load and resize images for each block
gif_frames = []
for i in range(36):
    img = Image.open(f"{i}.gif").resize((screen_width, screen_height), Image.LANCZOS)
    gif_frames.append(ImageTk.PhotoImage(img))

# Function to update the board
def update_board():
    canvas.delete("all")
    cell_size = 100
    for i in range(6):
        for j in range(6):
            idx = i * 6 + j
            if (i, j) == player_position:
                # colour = "blue"
                canvas.create_image(i * cell_size + cell_size / 2, j * cell_size + cell_size / 2, image=gif_frames[idx])
                check_status()
            



# Bind arrow key presses to movement
root.bind("<Left>", lambda event: move("left"))
root.bind("<Right>", lambda event: move("right"))
root.bind("<Up>", lambda event: move("up"))
root.bind("<Down>", lambda event: move("down"))

# Initial board setup
update_board()

root.mainloop()
