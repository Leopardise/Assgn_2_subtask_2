import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk





player_position = (0,0)
gif_frames = []
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
    
    def medicate(self, player_position):
        # global player_position
        # Get the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        canvas = tk.Canvas(root, width=screen_width, height=screen_height)
        canvas.pack()
        
        player_position = (0, 0)
        
       
        for i in range(36):
            img = Image.open(f"{i}.gif").resize((screen_width, screen_height), Image.LANCZOS)
            # img = Image.open(f"{i}.gif").resize((100, 100), Image.LANCZOS)
            gif_frames.append(ImageTk.PhotoImage(img))
            print(i)
        # print("gif_frame == ", len(gif_frames))
        cell_size = 100
        # Bind arrow key presses to movement
        root.bind("<Left>", lambda event: move("left", cell_size, canvas))
        root.bind("<Right>", lambda event: move("right", cell_size, canvas))
        root.bind("<Up>", lambda event: move("up", cell_size, canvas))
        root.bind("<Down>", lambda event: move("down", cell_size, canvas))

        # Initial board setup
        update_board(cell_size, canvas)
        # root.mainloop()
                
        

class Shelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

# Initialize shelter and animals
shelter = Shelter()
shelter.add_animal(Animal("Cat"))
shelter.add_animal(Animal("Bird"))
shelter.add_animal(Animal("Dog"))

# def choose_animal():
#     animal_selection = tk.Toplevel(root)
#     animal_selection.title("Choose Animal")

#     lbl_select = tk.Label(animal_selection, text="Select an animal:")
#     lbl_select.pack()

#     # Function to handle animal selection
#     def select_animal(animal):
#         animal_selection.destroy()
#         interact_with_animal(animal)

#     # Create buttons for each animal
#     for animal in shelter.animals:
#         btn_animal = tk.Button(animal_selection, text=animal.species, command=lambda a=animal: select_animal(a))
#         btn_animal.pack()

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
    def medicate():
        animal.medicate(player_position)
        
        
    interaction_window = tk.Toplevel(root)
    interaction_window.title(animal.species)
    interaction_window.geometry("300x200")

    lbl_animal = tk.Label(interaction_window, text=f"{animal.species} - Health: {animal.health}")
    lbl_animal.pack(pady=10)

    btn_feed = tk.Button(interaction_window, text="Feed", command=feed)
    btn_feed.pack()

    btn_treat = tk.Button(interaction_window, text="Treat", command=treat)
    btn_treat.pack()

    btn_play = tk.Button(interaction_window, text="Play", command=play)
    btn_play.pack()
    
    btn_injured = tk.Button(interaction_window, text="Treat animal", command=medicate)
    btn_injured.pack()

# def start_game():
#     choose_animal()

# Initialize main window
root = tk.Tk()
root.title("Pet Rescue Quest")
root.geometry("600x600")

lbl_heading = tk.Label(root, text="Welcome to Pet Rescue Quest!")
lbl_heading.pack(pady=10)

# Load GIF frames
gif_frames = []
gif = Image.open("forest2.gif")
try:
    while True:
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


# Place animal buttons
for idx, btn_animal in enumerate(animal_buttons):
    btn_animal.place(x=start_x, y=start_y + idx * (button_height + 20))


# Function to update player position
def move(direction, cell_size, canvas):
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
    update_board(cell_size, canvas)


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
def update_board(cell_size, canvas):
    canvas.delete("all")
    for i in range(6):
        for j in range(6):
            idx = i * 6 + j
            if (i, j) == player_position:
                # colour = "blue"
                canvas.create_image(i * cell_size + cell_size / 2, j * cell_size + cell_size / 2, image=gif_frames[idx])
                if (i, j) == (1,1):
                    animal.health += 10
                check_status()
root.mainloop()
