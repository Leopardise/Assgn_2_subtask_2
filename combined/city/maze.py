import pygame
import sys
import random
import os

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CELL_SIZE = 40  # Size of each cell in the maze



# Calculate the number of rows and columns based on screen size and cell size
NUM_COLS = SCREEN_WIDTH // CELL_SIZE
NUM_ROWS = SCREEN_HEIGHT // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
# Load images directly from the current directory
hospital_img = pygame.image.load('hospital.jpg')
person_img = pygame.image.load('person.png')

# Resize images to match the cell size
hospital_img = pygame.transform.scale(hospital_img, (CELL_SIZE, CELL_SIZE))
person_img = pygame.transform.scale(person_img, (CELL_SIZE, CELL_SIZE))

# Load background image
background_img = pygame.image.load('city.jpg')
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Maze representation (0 = wall, 1 = path, 2 = player, 3 = destination)
maze = [[0 for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

# Disjoint Set (Union-Find) data structure for Kruskal's algorithm
class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        
        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def generate_maze():
    global maze, player_pos, dest_pos, health
    
    # Reset the maze to its initial state
    maze = [[0 for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]  # All cells are walls initially

    walls = []  # List to hold all walls in the maze
    disjoint_set = DisjointSet()

    # Initialize disjoint set for each cell and collect all walls
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            cell = (row, col)
            disjoint_set.parent[cell] = cell
            disjoint_set.rank[cell] = 0
            
            # Add walls around each cell (not in the last row or column)
            if row < NUM_ROWS - 1:
                walls.append((cell, (row + 1, col)))  # Wall below the current cell
            if col < NUM_COLS - 1:
                walls.append((cell, (row, col + 1)))  # Wall to the right of the current cell

    random.shuffle(walls)  # Randomize the order of walls

    # Kruskal's algorithm to generate the maze
    for wall in walls:
        cell1, cell2 = wall
        root1 = disjoint_set.find(cell1)
        root2 = disjoint_set.find(cell2)
        
        if root1 != root2:
            # Remove the wall between two cells
            row1, col1 = cell1
            row2, col2 = cell2
            if row1 == row2:  # Cells are in the same row
                maze[row1][min(col1, col2)] = 1  # Remove vertical wall
            elif col1 == col2:  # Cells are in the same column
                maze[min(row1, row2)][col1] = 1  # Remove horizontal wall
            
            disjoint_set.union(root1, root2)

    # Place player and destination
    player_pos = (0, 0)  # Starting position of the player
    dest_pos = (NUM_ROWS - 1, NUM_COLS - 1)  # Destination position
    maze[player_pos[0]][player_pos[1]] = 2  # Place player at start
    maze[dest_pos[0]][dest_pos[1]] = 3  # Place destination
    health = 100  # Reset health

def draw_maze(screen, font):
    # Draw the background image first
    screen.blit(background_img, (0, 0))
    global health

    # Draw maze cells
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if maze[row][col] == 0:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[row][col] == 2:
                screen.blit(person_img, (col * CELL_SIZE, row * CELL_SIZE))
            elif maze[row][col] == 3:
                screen.blit(hospital_img, (col * CELL_SIZE, row * CELL_SIZE))
     # Draw health value on the screen corner
    
    health_text = font.render(f"Health: {health}", True, RED)
    screen.blit(health_text, (10, 10))  # Display health at (10, 10) on the screen
    

def move_player(dx, dy):
    global player_pos, health
    
    
    new_row = player_pos[0] + dy
    new_col = player_pos[1] + dx

    if 0 <= new_row < NUM_ROWS and 0 <= new_col < NUM_COLS and maze[new_row][new_col] != 0:
        # Move player to the new position
        maze[player_pos[0]][player_pos[1]] = 1  # Clear current player position
        player_pos = (new_row, new_col)
        health -= 3.5
        maze[player_pos[0]][player_pos[1]] = 2  # Place player in the new position

def display_message(screen, font, message):
    text_surface = font.render(message, True, BLACK)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text_surface, text_rect)

def main():
    global player_pos, health
    # health = 100

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Maze Game")

    # Load font for displaying text
    font = pygame.font.Font(None, 36)

    generate_maze()  # Generate the maze using Kruskal's algorithm

    clock = pygame.time.Clock()
    game_running = True
    game_over = False
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_player(0, -1)
                elif event.key == pygame.K_DOWN:
                    move_player(0, 1)
                elif event.key == pygame.K_LEFT:
                    move_player(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    move_player(1, 0)

        # Check if player reaches the destination
        if player_pos == dest_pos:
            screen.fill(WHITE)
            display_message(screen, font, "You won!")
            pygame.display.flip()
            pygame.time.wait(2000)  # Display the message for 2 seconds
            player_pos = (0, 0)  # Reset player position
            health = 100
            screen.fill(WHITE)
            display_message(screen, font, "Press 'N' to next or 'Q' to quit")
            pygame.display.flip()

            replay_or_quit = False
            while not replay_or_quit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_n:
                            # Replay the game
                            player_pos = (0, 0)
                            health = 100
                            generate_maze()
                            game_over = False
                            replay_or_quit = True
                        elif event.key == pygame.K_q:
                            # Quit the game
                            pygame.quit()
                            sys.exit()
                            
            generate_maze()  # Regenerate maze for a new game
# Check if health is depleted
        if health <= 0 and not game_over:
            game_over = True
            # Display "You lose" message
            screen.fill(WHITE)
            display_message(screen, font, "You lose, the player died")
            pygame.display.flip()
            pygame.time.wait(2000)  # Display the message for 2 seconds

        if game_over:
            # Ask player to replay or quit
            screen.fill(WHITE)
            display_message(screen, font, "Press 'R' to replay or 'Q' to quit")
            pygame.display.flip()

            replay_or_quit = False
            while not replay_or_quit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            # Replay the game
                            player_pos = (0, 0)
                            health = 100
                            generate_maze()
                            game_over = False
                            replay_or_quit = True
                        elif event.key == pygame.K_q:
                            # Quit the game
                            pygame.quit()
                            sys.exit()

        # Draw the maze, player, and destination
        draw_maze(screen, font)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(10)  # Limit to 10 frames per second

if __name__ == "__main__":
    main()
