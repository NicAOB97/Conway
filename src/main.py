# import dependencies
import pygame 
import numpy as np 
import time

# initialise screen 
pygame.init()

# set width and height 
height, width = 1000, 1000
screen = pygame.display.set_mode((height, width))

# set background colour 
bgc = 25, 25, 25
screen.fill(bgc)

# decide on number of cells (nc) you want to segment your x and y axis into 
ncX, ncY = 30, 30 

# specify size of each cell (given by width of screen divided by number of cells)
dimCWidth = width / ncX
dimCHeight = height / ncY

# specify what colour each cell will be at each moment 
# alive = 1, dead = 0 
# they all start dead so matrix of zeros of amount of cells in x and y 
gameState = np.zeros((ncX, ncY))

# Automate start
# stick automation
gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1
# mobile automation
gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1

# draw a grid
while True :

    newGameState = np.copy(gameState)
    screen.fill(bgc)

    time.sleep(0.2)

    # track mouse clicks to personalise board 
    # if mouse clicked, the cell which is clicked will change state (from 0 to 1)
    ev = pygame.event.get()
    mouseClick = pygame.mouse.get_pressed()

    for event in ev:
        if sum(mouseClick) > 0: 
            posX , posY = pygame.mouse.get_pos()
            celX, celY  = int(np.floor(posX/dimCWidth)), int(np.floor(posX/dimCHeight))
            newGameState[celX,celY] = 1

    for y in range (0, ncX):
        for x in range (0,ncY):

            # calculate number of neighbours per cell 
            # check each of the 8 cells surrounding every cell 
            n_neighbours =  gameState[(x-1) % ncX, (y-1)  % ncY ] + \
                            gameState[(x-1) % ncX, (y)    % ncY ]+ \
                            gameState[(x-1) % ncX, (y+1)  % ncY] + \
                            gameState[(x)   % ncX , (y-1) % ncY] + \
                            gameState[(x)   % ncX , (y+1) % ncY] + \
                            gameState[(x+1) % ncX, (y-1)  % ncY] + \
                            gameState[(x+1) % ncX, (y)    % ncY] + \
                            gameState[(x+1) % ncX, (y+1)  % ncY] 

            # specify the rules 
            # rule 1: if dead with 3 live neighbours -> cell revives
            if gameState[x,y] == 0 and n_neighbours == 3:
                newGameState[x,y] = 1

            # rule 2: if alive and less than 2 or more than 3 neighbours -> cell dies
            elif gameState[x,y] == 1 and (n_neighbours < 2 or n_neighbours > 3):
                 newGameState[x,y] = 0


            # cell coordinates
            poly = [(x     * dimCWidth, y     * dimCHeight), # coordinates of bottom left corner
                    ((x+1) * dimCWidth, y     * dimCHeight), # coordinates of bottom right corner
                    ((x+1) * dimCWidth, (y+1) * dimCHeight), # coordinates of top right corner
                    (x     * dimCWidth, (y+1) * dimCHeight), # coordinates of top left corner
                ]

            # draw polygon on surface (screen), of specific colour, coordinates, width (pixel)
            # colour according newGameState (changing in time) 
                # dead = dark 
                # alive = white

            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128,128,128), poly, 1 )
            else: 
                pygame.draw.polygon(screen, (255,255,255), poly, 0 )

    # update gameState 
    gameState = np.copy(newGameState )

    # display 
    pygame.display.flip()


# run screen
# exit and close window when exit button pressed
while True  :
    pass
"""     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() """