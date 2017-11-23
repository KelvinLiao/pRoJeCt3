"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 3
HEIGHT = 3

# This sets the margin between each cell
MARGIN = 2

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(120):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(160):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 0

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [802,602]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Grid Map")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

count = 0
while(count < 8):
    xrand = random.randint(0, 159)
    yrand = random.randint(0, 119)
    print( "xrand: ", xrand, ", yrand: ", yrand)
    probability = 0

    xTopLeftCorner = 0
    yTopLeftCorner = 0
        
    if xrand >= 15 and yrand >= 15:
        xTopLeftCorner = xrand - 15
        yTopLeftCorner = yrand - 15

    elif xrand >= 15 and yrand < 15:
        xTopLeftCorner = xrand - 15

    elif yrand >= 15 and xrand < 15:
        yTopLeftCorner = yrand - 15

    else:
        xTopLeftCorner = 0
        yTopLeftCorner = 0


    xBottomRightCorner = xrand + 15
    yBottomRightCorner = yrand + 15

    if xrand <= 144 and yrand <= 104:
        xBottomRightCorner = xrand + 15
        yBottomRightCorner = yrand + 15
        
    elif xrand <= 144 and yrand > 104:
        yBottomRightCorner = 119

    elif yrand <= 104 and xrand > 144:
        xBottomRightCorner = 159

    else:
        xBottomRightCorner = 159
        yBottomRightCorner = 119

    for x in range(xTopLeftCorner, xBottomRightCorner + 1):
        for y in range(yTopLeftCorner, yBottomRightCorner + 1):
            probability = random.uniform(0,1)
            if probability > 0.5:
                print( "coordinates ", x , " + ", y)
                grid[y][x] = 1
        
    count += 1

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        """ elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)  """

    # Set the screen background
    screen.fill(BLACK)

    """count = 0
    while(count < 8):
        xrand = random.randint(0, 159)
        yrand = random.randint(0, 119)
        print "xrand: ", xrand, ", yrand: ", yrand
        probability = 0

        xTopLeftCorner = 0
        yTopLeftCorner = 0
        
        if xrand >= 15 and yrand >= 15:
            xTopLeftCorner = xrand - 15
            yTopLeftCorner = yrand - 15

        elif xrand >= 15 and yrand < 15:
            xTopLeftCorner = xrand - 15

        elif yrand >= 15 and xrand < 15:
            yTopLeftCorner = yrand - 15

        else:
            xTopLeftCorner = 0
            yTopLeftCorner = 0


        xBottomRightCorner = xrand + 15
        yBottomRightCorner = yrand + 15

        if xrand <= 144 and yrand <= 104:
            xBottomRightCorner = xrand + 15
            yBottomRightCorner = yrand + 15
        
        elif xrand <= 144 and yrand > 104:
            yBottomRightCorner = 119

        elif yrand <= 104 and xrand > 144:
            xBottomRightCorner = 159

        else:
            xBottomRightCorner = 159
            yBottomRightCorner = 119

        for x in range(xTopLeftCorner, xBottomRightCorner + 1):
            for y in range(yTopLeftCorner, yBottomRightCorner + 1):
                probability = random.uniform(0,1)
                if probability > 0.5:
                    print "coordinates ", x , " + ", y
                    grid[y][x] = 1
        
        count += 1"""

    # Draw the grid
    for row in range(120):
        for column in range(160):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()


