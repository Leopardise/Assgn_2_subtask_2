import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

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
root.geometry("800x600")

# Load and resize images
gif_frames = []
# Load and resize images
gif_frames = []
for i in range(36):
    img = Image.open(f"{i}.gif").resize((100, 100), Image.LANCZOS)
    gif_frames.append(ImageTk.PhotoImage(img))


# Create canvas for displaying GIF matrix
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Initialize player position
player_position = 30

# Function to update player position
def move(direction):
    global player_position
    if direction == "left":
        if player_position % 6 != 0:
            player_position -= 1
    elif direction == "right":
        if (player_position + 1) % 6 != 0:
            player_position += 1
    elif direction == "forward":
        if player_position >= 6:
            player_position -= 6
    elif direction == "backward":
        if player_position < 30:
            player_position += 6

    update_board()

# Function to check win or lose
def check_status():
    global player_position
    if player_position == 5:
        messagebox.showinfo("Congratulations", "You reached the sanctuary! You win!")
        root.destroy()
    elif shelter.animals[0].health <= 0:
        messagebox.showinfo("Game Over", "Your pet's health reached 0. You lose!")
        root.destroy()

# Function to update the board
def update_board():
    canvas.delete("all")
    for i in range(6):
        for j in range(6):
            idx = i * 6 + j + 30
            if idx == 9 or idx == 23:
                canvas.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill="red")
            elif idx == 3 or idx == 13 or idx == 18 or idx == 27 or idx == 33:
                canvas.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill="blue")
            elif idx == 0 or idx == 6:
                canvas.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill="green")
            else:
                canvas.create_image(j * 100 + 50, i * 100 + 50, image=gif_frames[idx])
    canvas.create_image((player_position % 6) * 100 + 50, (player_position // 6) * 100 + 50, image=gif_frames[shelter.animals[0].health])

    check_status()

# Bind arrow key presses to movement
root.bind("<Left>", lambda event: move("left"))
root.bind("<Right>", lambda event: move("right"))
root.bind("<Up>", lambda event: move("forward"))
root.bind("<Down>", lambda event: move("backward"))

# Initial board setup
update_board()

root.mainloop()
