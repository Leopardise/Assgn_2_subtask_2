import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import pygame
from pygame.locals import *
import os


class Animal:
    def __init__(self, species, health=100):
        self.species = species
        self.health = health

    def feed(self):
        self.health += random.randint(5, 15)

    def treat(self):
        self.health += random.randint(10, 20)

    def play(self):
        self.health += random.randint(5, 10)

class Shelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

# Initialize shelter and animals
shelter = Shelter()
shelter.add_animal(Animal("Dog"))
shelter.add_animal(Animal("Cat"))
shelter.add_animal(Animal("Bird"))

def interact_with_animal(animal):
    def feed():
        animal.feed()
        messagebox.showinfo("Interaction", f"You fed the {animal.species}. Health increased to {animal.health}.")

    def treat():
        animal.treat()
        messagebox.showinfo("Interaction", f"You treated the {animal.species}. Health increased to {animal.health}.")

    def play():
        animal.play()
        messagebox.showinfo("Interaction", f"You played with the {animal.species}. Health increased to {animal.health}.")

    window = tk.Toplevel(root)
    window.title(animal.species)
    window.geometry("300x200")

    lbl_animal = tk.Label(window, text=f"{animal.species} - Health: {animal.health}")
    lbl_animal.pack(pady=10)

    btn_feed = tk.Button(window, text="Feed", command=feed)
    btn_feed.pack()

    btn_treat = tk.Button(window, text="Treat", command=treat)
    btn_treat.pack()

    btn_play = tk.Button(window, text="Play", command=play)
    btn_play.pack()

# Initialize main window
root = tk.Tk()
root.title("Pet Rescue Quest")
root.geometry("800x600")

lbl_heading = tk.Label(root, text="Welcome to Pet Rescue Quest!")
lbl_heading.pack(pady=10)

# Load GIF frames
gif_frames = []
gif = Image.open("forest2.gif")
try:
    while True:
        
        frame = gif.copy()
        frame.thumbnail((root.winfo_screenwidth(), root.winfo_screenheight()))
        frame = frame.resize((root.winfo_width(), root.winfo_height()), Image.LANCZOS)  # Resize to fit window
        
        # gif_frames.append(ImageTk.PhotoImage(gif.copy()))
        gif_frames.append(ImageTk.PhotoImage(gif.copy()))
        gif.seek(len(gif_frames))  # Go to the next frame
except EOFError:
    pass

# Display GIF frames
gif_index = 0
background_label = tk.Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def update_gif():
    global gif_index
    root.after(100, update_gif)  # Adjust the speed of the GIF here
    background_label.config(image=gif_frames[gif_index])
    background_label.image = gif_frames[gif_index]
    gif_index = (gif_index + 1) % len(gif_frames)

update_gif()

# Load and resize images
dog_img = Image.open("dog.jpg").resize((200, 200), Image.LANCZOS)
dog_photo = ImageTk.PhotoImage(dog_img)

cat_img = Image.open("cat.jpg").resize((200, 200), Image.LANCZOS)
cat_photo = ImageTk.PhotoImage(cat_img)

bird_img = Image.open("bird.jpg").resize((200, 200), Image.LANCZOS)
bird_photo = ImageTk.PhotoImage(bird_img)

button_width = 200
button_height = 200

centre_x = (root.winfo_screenwidth()) / 2
centre_y = (root.winfo_screenheight()) / 4

start_x = centre_x - button_width / 2
start_y = centre_y - button_height / 2

# Display buttons with resized images
animal_buttons = []
for idx, animal in enumerate(shelter.animals):
    if animal.species == "Dog":
        btn_animal = tk.Button(root, text=animal.species, image=dog_photo, compound="left", command=lambda a=animal: interact_with_animal(a))
    elif animal.species == "Cat":
        btn_animal = tk.Button(root, text=animal.species, image=cat_photo, compound="left", command=lambda a=animal: interact_with_animal(a))
    elif animal.species == "Bird":
        btn_animal = tk.Button(root, text=animal.species, image=bird_photo, compound="left", command=lambda a=animal: interact_with_animal(a))
    animal_buttons.append(btn_animal)

# Calculate vertical center
# vertical_center = (600 - len(animal_buttons) * 220) / 2

# Place animal buttons
for idx, btn_animal in enumerate(animal_buttons):
    btn_animal.place(x=start_x, y=start_y + idx * (button_height + 20))

root.mainloop()
