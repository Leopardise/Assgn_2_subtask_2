import tkinter as tk
from tkinter import messagebox
import random

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
root.geometry("400x300")

lbl_heading = tk.Label(root, text="Welcome to Pet Rescue Quest!")
lbl_heading.pack(pady=10)

lbl_info = tk.Label(root, text="Choose an animal to interact with:")
lbl_info.pack()

for idx, animal in enumerate(shelter.animals):
    btn_animal = tk.Button(root, text=animal.species, command=lambda a=animal: interact_with_animal(a))
    btn_animal.pack()

root.mainloop()
