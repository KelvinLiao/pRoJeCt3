
import pygame
import random
import math
from heapdict import heapdict
import timeit

start = timeit.default_timer()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255,165,0)
GRAY = (128,128,128)
GOLD = (255, 215,0)
PINK = (255,105,180)

WIDTH = 3
HEIGHT = 3

MARGIN = 2
grid = []

for row in range(120):
    grid.append([])
    for column in range(160):
        grid[row].append(0) 
        
pygame.init()
windowSize = [802,602]
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Grid Map")
done = False
clock = pygame.time.Clock()



xrands = []
yrands = []
numberHardAreas = 0
while(numberHardAreas < 8):
    xrand = random.randint(0, 159)     #centers
    yrand = random.randint(0, 119)
    xrands.append(xrand)
    yrands.append(yrand)
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
                grid[y][x] = '1'
        
    numberHardAreas += 1

def pickBorderCell():
    
    borderCell = []
    xCoord = 0 #random placeholder values
    yCoord = 0 #random placeholder values
    
    while( (xCoord == 0 and yCoord == 0) or (xCoord == 159 and yCoord == 0) or (xCoord == 0 and yCoord == 119) or (xCoord == 159 and yCoord == 119)):
       
        selection = random.randint(0,559)
        #selection ranges from 0 - 159, x ranges from 0 to 159
        if selection < 160: 
            xCoord = selection
            yCoord = 0
        
        #selection ranges from 160 to 279, y ranges from 0 to 119
        elif selection < 280: 
            xCoord = 159
            yCoord = selection - 160
        
        #selection ranges from 279 to 438, x ranges from 0 to 159
        elif selection < 439: 
            xCoord = selection - 279
            yCoord = 119
        
        #selection ranges from 439 to 558
        else: 
            xCoord = 0
            yCoord = selection - 439
            
    #print ("pickBorderCell generating border coordinate: xCoord: " , xCoord, " yCoord: ", yCoord)
    borderCell.append(xCoord)
    borderCell.append(yCoord)
    return borderCell



finalHighwayGrid = []
for row in range(120):
    finalHighwayGrid.append([])
    for column in range(160):
        finalHighwayGrid[row].append(0)  


highwaysCreated = 0
count = 0

def riverGenerator():
   return
   
    
    
   

  
def createHighwayPath():    
    global highwaysCreated
    global count
    
    #print("highwaysCreated: ", highwaysCreated)
   
    currentHighwayGrid = []
    for row in range(120):
    # Add an empty array that will hold each cell
    # in this row
        currentHighwayGrid.append([])
        for column in range(160):
            currentHighwayGrid[row].append(0)  # Append a cell
    
    
    count = 0
    
    borderCell = pickBorderCell()
    
    #borderCellX = borderCell[0]
    borderCellX = borderCell[0]
    borderCellY = borderCell[1]
    
    currCellX = borderCellX
    currCellY = borderCellY
    
    currentDirection = ''
    
    
    if(borderCellX == 0):
        currentHighwayGrid = lengthenHighway(borderCellX,borderCellY,'right',currentHighwayGrid)
        if(highwaysCreated >= 4):
            return
        currentDirection = 'right'
        
        currCellX = borderCellX + 20
        currCellY = borderCellY
        
        
        
    elif(borderCellX == 159):
        currentHighwayGrid = lengthenHighway(borderCellX,borderCellY,'left',currentHighwayGrid)
        if(highwaysCreated >= 4):
            return
        currentDirection = 'left'
        
        currCellX = borderCellX - 20
        currCellY = borderCellY
        
        
        
    elif(borderCellY == 0):
        currentHighwayGrid = lengthenHighway(borderCellX,borderCellY,'down',currentHighwayGrid)
        if(highwaysCreated >= 4):
            return
        currentDirection = 'down'
        
        currCellX = borderCellX 
        currCellY = borderCellY + 20
        
        
        
    else:
        currentHighwayGrid = lengthenHighway(borderCellX,borderCellY,'up',currentHighwayGrid)
        if(highwaysCreated >= 4):
            return
        currentDirection = 'up'
        
        currCellX = borderCellX 
        currCellY = borderCellY - 20
   
    currentDirection = pickNewDirection(currentDirection)
    
    controlIterations = 0
    while(True):
    
        currentHighwayGrid = lengthenHighway(currCellX, currCellY, currentDirection ,currentHighwayGrid)
        if(highwaysCreated >= 4):
            return 
        currCellCoord = updateCurrCell(currCellX, currCellY, currentDirection)
        currCellX = currCellCoord[0]
        currCellY = currCellCoord[1]
        currentDirection = pickNewDirection(currentDirection)

        controlIterations += 1

    
    
    return currentHighwayGrid


def checkHighwayInBounds(a, b):
    
    if(a >= 0 and b >= 0 and a <= 159 and b <= 119):
        return True
    else:
        return False
    
def updateCurrCell(X, Y, direction):
    
    currCoord = []
    currCellX = X
    currCellY = Y
    
    if(direction == 'right'):
        currCellX = X + 20
        currCellY = Y
        
    elif(direction == 'left'):
        currCellX = X - 20
        currCellY = Y
     
    elif(direction == 'down'):
        currCellX = X 
        currCellY = Y + 20
        
    else:
        currCellX = X 
        currCellY = Y - 20
    
    currCoord.append(currCellX)
    currCoord.append(currCellY)
    return currCoord
    
    
    
def lengthenHighway(xCoord, yCoord, direction, currentHighwayGrid):
    global highwaysCreated
    global count
    global finalHighwayGrid
    
    if(direction == 'up'):
        for i in range(20):
            if(checkHighwayInBounds(xCoord,yCoord-i)):
                if(not finalHighwayGrid[yCoord-i][xCoord] == '2' and not finalHighwayGrid[yCoord-i][xCoord] == '3' and not currentHighwayGrid[yCoord-i][xCoord] == '2' and not currentHighwayGrid[yCoord-i][xCoord] == '3' ):
                    if(grid[yCoord-i][xCoord]=='1'):
                        currentHighwayGrid[yCoord-i][xCoord] = '3'
                        count += 1
                    else:
                        currentHighwayGrid[yCoord-i][xCoord] = '2'
                        count += 1
                else:
                    createHighwayPath()
                    if(highwaysCreated >= 4):
                        return
                    
            else:
                if(count >= 100):
                    for row in range(120):
                        for column in range(160):
                            if(currentHighwayGrid[row][column] == '2'):
                                #print("row: " , row, " column: ", column)
                                finalHighwayGrid[row][column] = '2'
                            elif(currentHighwayGrid[row][column] == '3'):
                                #print("row: " , row, " column: ", column)
                                finalHighwayGrid[row][column] = '3'
                    highwaysCreated += 1
                    #print("DONE")
                    #print("Finished at xCoord: ", xCoord, " yCoord: ", yCoord-i)
                    if(highwaysCreated >= 4):
                        return
                    else:
                        createHighwayPath()
                        if(highwaysCreated >= 4):
                            return
                else:
                    createHighwayPath()
                    if(highwaysCreated >= 4):
                        return
                    
      
        
    elif(direction == 'down'):
        for i in range(20):
            if(checkHighwayInBounds(xCoord,yCoord+i)):
                if(not finalHighwayGrid[yCoord+i][xCoord] == '2' and not finalHighwayGrid[yCoord+i][xCoord] == '3' and not currentHighwayGrid[yCoord+i][xCoord] == '2' and not currentHighwayGrid[yCoord+i][xCoord] == '3' ):
                    if(grid[yCoord+i][xCoord]=='1'):
                        currentHighwayGrid[yCoord+i][xCoord] = '3'
                        count += 1
                    else:
                        currentHighwayGrid[yCoord+i][xCoord] = '2'
                        count += 1
                else:
                    createHighwayPath()
                    if(highwaysCreated >= 4):
                        return
            else:
                if(count >= 100):
                    for row in range(120):
                        for column in range(160):
                            if(currentHighwayGrid[row][column] == '2'):
                                #print("row: " , row, " column: ", column)
                                finalHighwayGrid[row][column] = '2'
                            elif(currentHighwayGrid[row][column] == '3'):
                                #print("row: " , row, " column: ", column)
                                finalHighwayGrid[row][column] = '3'
                    highwaysCreated += 1
                    #print("DONE")
                    #print("Finished at xCoord: ", xCoord, " yCoord: ", yCoord+i)
                    if(highwaysCreated >= 4):
                        return
                    else:
                        createHighwayPath()
                        if(highwaysCreated >= 4):
                            return
                else:
                    createHighwayPath()
                    if(highwaysCreated >= 4):
                        return
            

    
    elif(direction == 'left'):
        for i in range(20):
            if(checkHighwayInBounds(xCoord-i,yCoord)):
                if(not finalHighwayGrid[yCoord][xCoord-i] == '2' and not finalHighwayGrid[yCoord][xCoord-i] == '3' and not currentHighwayGrid[yCoord][xCoord-i] == '2' and not currentHighwayGrid[yCoord][xCoord-i] == '3' ):
                    if(grid[yCoord][xCoord-i]=='1'):
                        currentHighwayGrid[yCoord][xCoord-i] = '3'
                        count += 1
                    else:
                        currentHighwayGrid[yCoord][xCoord-i] = '2'
                        count += 1
                else:
                    createHighwayPath()
                    if(highwaysCreated >= 4):
                        return
            else:
                if(count >= 100):
                    for row in range(120):
                        for column in range(160):
                            if(currentHighwayGrid[row][column] == '2'):
                                #print("row: " , row, " column: ", column)
                                finalHighwayGrid[row][column] = '2'
                            elif(currentHighwayGrid[row][column] == '3'):
                                #print("row: " , row, " column: ", column)
                                finalHighwayGrid[row][column] = '3'
                    highwaysCreated += 1
                    #print("DONE")
                    #print("Finished at xCoord: ", xCoord-i, " yCoord: ", yCoord)
                    if(highwaysCreated >= 4):
                        return
                    else:
                        createHighwayPath()
                        if(highwaysCreated >= 4):
                            return
                else:
                    createHighwayPath()
                    if(highwaysCreated >= 4):
                        return
             
                
                
    else:
        for i in range(20):
            if(checkHighwayInBounds(xCoord+i,yCoord)):
                if(not finalHighwayGrid[yCoord][xCoord+i] == '2' and not finalHighwayGrid[yCoord][xCoord+i] == '3' and not currentHighwayGrid[yCoord][xCoord+i] == '2' and not currentHighwayGrid[yCoord][xCoord+i] == '3' ):
                    if(grid[yCoord][xCoord+i]=='1'):
                        currentHighwayGrid[yCoord][xCoord+i] = '3'
                        count += 1
                    else:
                        currentHighwayGrid[yCoord][xCoord+i] = '2'
                        count += 1
                else:
                    createHighwayPath()
                    if(highwaysCreated >= 4):
                        return
            else:
                if(count >= 100):
                    for row in range(120):
                        for column in range(160):
                            if(currentHighwayGrid[row][column] == '2'):
                                #print("row: " , row, " column: ", column)
                                finalHighwayGrid[row][column] = '2'
                            elif(currentHighwayGrid[row][column] == '3'):
                                #print("row: " , row, " column: ", column)
                                finalHighwayGrid[row][column] = '3'
                    highwaysCreated += 1
                    #print("DONE")
                    #print("Finished at xCoord: ", xCoord+i, " yCoord: ", yCoord-i)
                    if(highwaysCreated >= 4):
                        return
                    else:
                        createHighwayPath()
                        if(highwaysCreated >= 4):
                            return
                else:
                    createHighwayPath()  
                    if(highwaysCreated >= 4):
                        return
             
    return currentHighwayGrid
             





def pickNewDirection(direction):
    
    probability = random.uniform(0,1)
    
    if(direction == 'up'):
        if(probability <= 0.6):
            return 'up'
        elif(probability >0.6 and probability <= 0.8):
            return 'left'
        else:
            return 'right'
    
    elif(direction == 'down'):
        if(probability <= 0.6):
            return 'down'
        elif(probability >0.6 and probability <= 0.8):
            return 'left'
        else:
            return 'right'
        
    elif(direction == 'left'):
        if(probability <= 0.6):
            return 'left'
        elif(probability >0.6 and probability <= 0.8):
            return 'up'
        else:
            return 'down'
        
    else:
        if(probability <= 0.6):
            return 'right'
        elif(probability >0.6 and probability <= 0.8):
            return 'up'
        else:
            return 'down'
    return 

            
createHighwayPath()
highways = finalHighwayGrid


for row in range(120):
    for column in range(160):
        if(highways[row][column] == '2'): #2 is for highways over regular cells
            #print("row: " , row, " column: ", column)
            grid[row][column] = '2'
        elif(highways[row][column] == '3'): #3 is for highways over hard to traverse cells
            grid[row][column] = '3'
        else:
            continue
        

def blockedCells():
    tempCount = 0
    tempX = 0
    tempY = 0
    
    while(tempCount < 3840):
        tempX = random.randint(0,159)
        tempY = random.randint(0,119)
        
        if(not grid[tempY][tempX] == '2' and not grid[tempY][tempX] == '3'):
            grid[tempY][tempX] = '4'
            tempCount += 1
        else:
            continue 
            
blockedCells()

startCoordinate = []
def selectStart():
    global startCoordinate
    
    probabilityX = random.random()
    probabilityY = random.random()
    startX = 0
    startY = 0
    
    while(not grid[startY][startX] == '4'):
        startX = random.randint(0,159)
        startY = random.randint(0,119)
    
    while(grid[startY][startX] == '4'):
        if(probabilityX < 0.5 and probabilityY < 0.5):
            startX = random.randint(0,20)
            startY = random.randint(0,19)
        
        elif(probabilityX > 0.5 and probabilityY < 0.5):
            startX = random.randint(140,159)
            startY = random.randint(0,19)
        
        elif(probabilityX < 0.5 and probabilityY > 0.5):
            startX = random.randint(0,20)
            startY = random.randint(100,119)
        
        else:
            startX = random.randint(140,159)
            startY = random.randint(100,119)
        
        probabilityX = random.random()
        probabilityY = random.random()
        
    grid[startY][startX] = '5'
    startCoordinate.append(startY)
    startCoordinate.append(startX)
    print("SELECTED START AT xCoord: ", startX, " yCoord: " , startY)
    
selectStart()

goalCoordinate = []
def selectGoal():
    global goalCoordinate
    global startCoordinate
    
    startX = startCoordinate[1]
    startY = startCoordinate[0]
    probabilityX = random.random()
    probabilityY = random.random()
    goalX = 0
    goalY = 0
    
    while(not grid[goalY][goalX] == '4'):
        goalX = random.randint(0,159)
        goalY = random.randint(0,119)
    
    distanceFromStart = 0
    
    while(grid[goalY][goalX] == '4' or distanceFromStart < 100):
        if(probabilityX < 0.5 and probabilityY < 0.5):
            goalX = random.randint(0,20)
            goalY = random.randint(0,19)
            distanceFromStart = abs(startX - goalX) + abs(startY - goalY)
        
        elif(probabilityX > 0.5 and probabilityY < 0.5):
            goalX = random.randint(140,159)
            goalY = random.randint(0,19)
            distanceFromStart = abs(startX - goalX) + abs(startY - goalY)
        
        elif(probabilityX < 0.5 and probabilityY > 0.5):
            goalX = random.randint(0,20)
            goalY = random.randint(100,119)
            distanceFromStart = abs(startX - goalX) + abs(startY - goalY)
        
        else:
            goalX = random.randint(140,159)
            goalY = random.randint(100,119)
            distanceFromStart = abs(startX - goalX) + abs(startY - goalY)
      
        probabilityX = random.random()
        probabilityY = random.random()
        
    goalCoordinate.append(goalY)
    goalCoordinate.append(goalX)
    grid[goalY][goalX] = '6'
    
    print("SELECTED GOAL AT xCoord: ", goalX, " yCoord: " , goalY)
    
selectGoal()
print("DONE GENERATING MAP")
#BEGIN DANS CODE
def returnFile():
    global goalCoordinate
    global startCoordinate
    workfile = open('info.txt', 'w')
    workfile.write('Start coordinates: (' + str(startCoordinate[1]) + ', '+ str(startCoordinate[0]) + ') \n')
    workfile.write('Goal coordinates: (' + str(goalCoordinate[1]) + ', '+ str(goalCoordinate[0]) + ') \n')
    for i in range(len(xrands)):
        workfile.write('Center of hard to traverse region ' + str(i) + ': (' + str(xrands[i]) + ', ' + str(yrands[i]) + ') \n')
    row = 0 
    for line in grid:
        next_line = ''
        for val in line:
            if val == '4':
                next_line += '0'
            elif val == '1':	
                next_line += '2'
            elif val == '2':	
                next_line += 'a'
            elif val == '3':	
                next_line += 'b'
            else:
                next_line += '1'
        workfile.write(next_line + '\n')	

  
print("FILE RETURNED")
def readFile():
    global goalCoordinate
    global startCoordinate
    
    #data_file = sys.argv[1]
    #data_file = 'info.txt'
    for_grid = open('info.txt', 'r')
    count = 0
    grid2 = []
    for line in for_grid:
        line = line.strip('\n') 
        if count <= 9:
            if count == 0:
                start = line.find( '(' )
                end = line.find( ')' )
                if start != -1 and end != -1:
                    result = line[start+1:end]
                x, y = result.split(',')
                #print x, y
                startCoordinate[0] = int(y.strip(' '))
                startCoordinate[1] = int(x)
                print(startCoordinate)
                print(count)
                count += 1

            elif count == 1:
                print("LOL IN THE LOOP")
                start = line.find( '(' )
                end = line.find( ')' )
                if start != -1 and end != -1:
                    result = line[start+1:end]
                x, y = result.split(',')
                print(x, y)
                goalCoordinate[0] = int(y.strip(' '))
                goalCoordinate[1] = int(x)
                print(goalCoordinate)
                count += 1
            
            else:
                count += 1
            

        else:
            holder = []
            col = 0
            row = 0

            for val in line:
                if str(val) == '0':
                    holder.append('4')
                elif str(val) == '2':
                    holder.append('1')
                elif str(val) == 'a':
                    holder.append('2')
                elif str(val) == 'b':
                    holder.append('3')
                else:
                    holder.append('0')	
                col = col + 1
            grid2.append(holder)
            row = row + 1
    grid2[goalCoordinate[0]][goalCoordinate[1]] = '6'	
    grid2[startCoordinate[0]][startCoordinate[1]] = '5'	
    return grid2				


#if len(sys.argv) > 1:

#END DANS CODE





#currentCell is the item popped off from the fringe, exists in form(f, xCoord, yCoord)
def findSucc(currentCell):
    global closedList
    
    successors = []
    
    #start by checking the cell to the upper left of x, y
    xTemp = currentCell[0][0] - 1
    yTemp = currentCell[0][1] - 1
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4' and not successorCoordinate in closedList):
        successors.append((xTemp,yTemp))

    
    #check cell above x, y
    xTemp = currentCell[0][0] 
    yTemp = currentCell[0][1] - 1 
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4' and not successorCoordinate in closedList):
        successors.append((xTemp,yTemp))
    

    #check cell upper right of x, y
    xTemp = currentCell[0][0] + 1
    yTemp = currentCell[0][1] - 1 
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4' and not successorCoordinate in closedList):
       successors.append((xTemp,yTemp))
    
    
    #check cell right of x, y
    xTemp = currentCell[0][0] + 1
    yTemp = currentCell[0][1]  
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4' and not successorCoordinate in closedList):
        successors.append((xTemp,yTemp))
    
    
    #check cell bottom right of x, y
    xTemp = currentCell[0][0] + 1
    yTemp = currentCell[0][1] + 1  
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4' and not successorCoordinate in closedList):
        successors.append((xTemp,yTemp))
    
    
    #check cell below x, y
    xTemp = currentCell[0][0] 
    yTemp = currentCell[0][1] + 1 
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4' and not successorCoordinate in closedList):
        successors.append((xTemp,yTemp))
    
    
    #check cell bottom left of x, y
    xTemp = currentCell[0][0] - 1
    yTemp = currentCell[0][1] + 1 
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4' and not successorCoordinate in closedList):
        successors.append((xTemp,yTemp))
    
    
    #check cell left of x, y
    xTemp = currentCell[0][0]  - 1
    yTemp = currentCell[0][1]  
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4' and not successorCoordinate in closedList):
        successors.append((xTemp,yTemp))
    
    
    return successors
    

fringe = heapdict()
#s is the item popped off from the fringe, exists in the form (f, xCoord, yCoord)    
def inFringe(s):
    global fringe
    
    tempX = s[0][0]
    tempY = s[0][1]
    
    for triplet in fringe:
        if(triplet[0] == tempX and triplet[1] == tempY):
            return True
    return False

def calculateCost(sx, sy, sprimex, sprimey):
    
    #should never be blocked or out of bounds
    
    grid[sy][sx]
    #character
    #no character: regular cell
        #== ''
    #1: hard to traverse
    #2: highway over regular
    #3: highway over hard to traverse 
    #4: blocked
    #5: start(regular)
    #6: goal(regular)
    
    #for current cell-------------------
    
    currentCellType=''
    
    #partially blocked
    if(grid[sy][sx]=='1'):
        currentCellType='p'
    #highway over regular
    elif(grid[sy][sx]=='2'):
        currentCellType='hr'
    #highway over partially blocked
    elif(grid[sy][sx]=='3'):
        currentCellType='hp'
    #regular
    else:
        currentCellType='r'
    
    #print("currentCellType="+currentCellType)
    
    #for successor cell
    
    successorCellType=''
    
    #partially blocked
    if(grid[sprimey][sprimex]=='1'):
        successorCellType='p'
    #highway over regular
    elif(grid[sprimey][sprimex]=='2'):
        successorCellType='hr'
    #highway over partially blocked
    elif(grid[sprimey][sprimex]=='3'):
        successorCellType='hp'
    #regular
    else:
        successorCellType='r'
        
    #print("successorCellType="+successorCellType)
        
    #is it a horizontal or diagonal move:
    typeMove =''
    
    #it's a horizontal move
    if(sy==sprimey or sx==sprimex):
        typeMove='h'
    else:
        typeMove='d'
        
    
    if(currentCellType=='r'):
        if(successorCellType=='r' or successorCellType=='hr'):
            if(typeMove=='h'):
                #horizontal regular to regular
                #horizontal regular to hregular
                return 1
            elif(typeMove=='d'):
                #diagonal regular to regular
                #diagonal regular to hregular
                return 2**(.5)
        elif(successorCellType=='p'or successorCellType=='hp'):
            if(typeMove=='h'):
                #horizontal regular to partially
                #horizontal regular to hpartially
                return 1.5
            elif(typeMove=='d'):
                #diagonal regular to partially
                #diagonal regular to hpartially
                return (2**(.5)+8**(.5))/2   
    elif(currentCellType=='p'):
        if(successorCellType=='r'or successorCellType=='hr'):
            if(typeMove=='h'):
                #horizontal partially to regular
                #horizontal partially to hregular
                return 1.5
            elif(typeMove=='d'):
                #diagonal partially to regular
                #diagonal partially to hregular
                return (2**(.5)+8**(.5))/2   
        elif(successorCellType=='p' or successorCellType=='hp'):
            if(typeMove=='h'):
                #horizontal partially to partially
                #horizontal partially to hpartially
                return 2
            elif(typeMove=='d'):
                #diagonal partially to partially
                #diagonal partially to hpartially
                return 8**(.5)
    elif(currentCellType=='hr'):
        if(successorCellType=='r'):
            if(typeMove=='h'):
                #horizontal hregular to regular
                return 1
            elif(typeMove=='d'):
                #diagonal hregular to regular
                return 2**(.5)
        elif(successorCellType=='p'):
            if(typeMove=='h'):
                #horizontal hregular to partially
                return 1.5
            elif(typeMove=='d'):
                #diagonal hregular to partially
                return (2**(.5)+8**(.5))/2  
        elif(successorCellType=='hr'):
            #hregular to hregular
            return .25
        elif(successorCellType=='hp'):
            #hregular to hpartially
            return .375
    elif(currentCellType=='hp'):
        if(successorCellType=='r'):
            if(typeMove=='h'):
                #horizontal hpartially to regular
                return 1.5
            elif(typeMove=='d'):
                #diagonal hpartially to regular
                return (2**(.5)+8**(.5))/2   
        elif(successorCellType=='p'):
            if(typeMove=='h'):
                #horizontal hpartially to partially
                return 2
            elif(typeMove=='d'):
                #diagonal hpartially to partially
                return 8**(.5)
        elif(successorCellType=='hr'):
            #hpartially to hregular
            return .375
        elif(successorCellType=='hp'):
            #hpartially to hpartially
            return .5
        

 

#We are going to use Euclidean distance/10 as our main admissible/consistent heuristic
#It calculates the straight line distance between our current point and the goal point 
#Even though it ignores the type of cells in the way and the way you can move on the grid(diagonally/horizontally/vertically) 
#it does a great job telling us what direction to go in
#The formula is sqrt((cellX-goalX)^2+(cellY-goalY)^2)
def euclidianDist(cellX,cellY, goalX, goalY):
    x=cellX-goalX
    y=cellY-goalY
    return math.hypot(x,y)/10.0

#Manhattan distance, like Euclidean distance ignores the type of cells in the way but actually takes into account 
#the way you move on the grid. It ignores diagonal moves, but it does calculate the number of horizontal/vertical
#moves you need to get to the goal. It also tells us what direction to go in to get to the goal, just not in a diagonal way
#The formula is abs(cellX-goalX)+abs(cellY-goalY)
def manhattanDist(cellX,cellY,goalX,goalY):
    x=abs(cellX-goalX)
    y=abs(cellY-goalY)
    return x+y

#Chebychev distance is like Manhattan distance but does actually take into account the diagonal movement. 
#Like Manhattan distance and Euclidean distance it does ignore the types of cells on the way
#The formula is max(abs(cellX-goalX),abs(cellY-goalY))
def chebychevDist(cellX,cellY,goalX,goalY):
    x=abs(cellX-goalX)
    y=abs(cellY-goalY)
    return max(x,y)

#To make a heuristic that does take into account the type of cells on the way to the goal, we make a simple heuristic 
#that discourages the path from going close to hard to traverse areas since those areas make the costs higher
#The idea is that if the current cell is really close to the closest center, the heuristic should be higher
#If the current cell is not so close to the closest center, the heurisitc should be lower
#The formula is the distance to the closest center
def avoidHardToTraverseCenters(cellX,cellY,goalX,goalY):
    global xrands
    global yrands
    
    minimumDistanceToCenter = 10000
    for centerN in range(len(xrands)):
        x=xrands[centerN]
        y=yrands[centerN]
        if(math.hypot(x-cellX,y-cellY) < minimumDistanceToCenter):
            minimumDistanceToCenter=math.hypot(x-cellX,y-cellY)
    
    if(minimumDistanceToCenter == 0):
        minimumDistanceToCenter = 1
    #the larger that distance, the smaller the heursitic
    #the smaller the distance, the bigger the heuristic
    return 1/minimumDistanceToCenter

#Another heuristic we came up with but didn't actually implement was to take into account the types of cells as follows: 
#we give a higher heuristic value to cells who have more neighbors which are either regular cells or highways
#def goTowardsRegularNeighbors(cellX,cellY,goalX,goalY):
    
#Combining direction, movement and a knowledge of cell types: we get a combination of chebychev distance and avoiding hard to traverse centers
#The formula is chebychevDist()+weight * avoidHardToTraverseCenters()
def chebychevAndAvoidHardToTraverse(cellX,cellY,goalX,goalY):
    #this weight seems pretty good since we direction is more important than avoiding hard to traverse centers. 
    #Avoiding these might really lead you down a bad path
    weight = 2
    return chebychevDist(cellX,cellY,goalX,goalY) + weight * avoidHardToTraverseCenters(cellX,cellY,goalX,goalY)



def h(choice, sX, sY, sPX, sPY):
    
    if(choice == 1):
        #print("1 ",euclidianDist(sX, sY, sPX, sPY))
        return euclidianDist(sX, sY, sPX, sPY)
        
    elif(choice == 2):
        #print( manhattanDist(sX, sY, sPX, sPY))
        return manhattanDist(sX, sY, sPX, sPY)
        
    elif(choice == 3):
        #print( chebychevDist(sX, sY, sPX, sPY))
        return chebychevDist(sX, sY, sPX, sPY)
        
    elif(choice == 4):
        #print( avoidHardToTraverseCenters(sX, sY, sPX, sPY))
        return avoidHardToTraverseCenters(sX, sY, sPX, sPY)
        
    else:
        #print( avoidHardToTraverseCenters(sX, sY, sPX, sPY))
        return chebychevAndAvoidHardToTraverse(sX, sY, sPX, sPY)
        
#s and sPrime exist as (f, x, y) triplets
def UpdateVertex(s, sPrime, w, hChoice):
    global startCoordinate
    global goalCoordinate
    global gVals
    global parentsTable
    
    goalX = goalCoordinate[1]
    goalY = goalCoordinate[0]
    
    sX = s[0][0]
    sY = s[0][1]
    sCoord = [sX,sY]
    
    #NEED TO FIGURE OUT HOW TO STORE SPRIME RIGHT NOW IT'S A TUPLE WITH (x,y) NOT (f,x,y)
    sPrimeX = sPrime[0]
    sPrimeY = sPrime[1]
    
    
    
    c = calculateCost(sX, sY, sPrimeX, sPrimeY)
    #f = g + h, so to get g use g = f - h, f is stored as s[0] and h is calculated 
    gS = gVals[sY][sX]
    gSPrime = gVals[sPrimeY][sPrimeX]
    #print("gSPrime ", gSPrime)
    hSPrime = h(hChoice, sPrimeX, sPrimeY, goalX, goalY)
    
    if(gS + c < gSPrime):
        #print("IM IN IF")
        gSPrime = gS + c
        gVals[sPrimeY][sPrimeX] = gSPrime
        
        parentsTable[sPrimeY][sPrimeX] = sCoord
       
        fringe[(sPrimeX, sPrimeY)] = gSPrime + hSPrime * w
        
    
closedList = []
gVals = []
parentsTable = [] 
nodesExpanded = 0   
def aStar(w, hChoice):
    global startCoordinate
    global goalCoordinate
    global closedList
    global gVals
    global parentsTable
    global nodesExpanded

    #Create 120x160 table for g values
    for row in range(120):
        gVals.append([])
        for column in range(160):
            gVals[row].append(0)  
    #Initialize all values to infinity
    for row in range(120):
        for column in range(160):
            gVals[row][column] = 999999999
            
    #Create 120x160 table to link each coordiante's parent
    for row in range(120):
        parentsTable.append([])
        for column in range(160):
            parentsTable[row].append(0)  # Append a cell
    #Initialize all values to null
    for row in range(120):
        for column in range(160):
            parentsTable[row][column] = []
            
    
    startX = startCoordinate[1]
    startY = startCoordinate[0]
    
    #g for start cell is 0 
    gVals[startY][startX] = 0
    goalX = goalCoordinate[1]
    goalY = goalCoordinate[0]
    
    
    closedList = []
    
    parentsTable[startY][startX] = [startX, startY]
    heur = h(hChoice,startX, startY, goalX, goalY) * w
    f = gVals[startY][startX] + heur
    
    
    fringe[(startX, startY)] = f
    
    
   
    
    finished = False
    while(not finished):
        try:
            
            s = fringe.popitem()
            nodesExpanded += 1
            if(s[0][0] == goalX and s[0][1] == goalY):
                print("PATH FOUND")
                return
            
          
            sForClosedList = (s[0][0],s[0][1])
            closedList.append(sForClosedList)
            #print("CLOSED LIST ", closedList)
            #print("S ", s)
            successors = findSucc(s)
            #print("SUCCESSORS ", successors)
            
            for sPrimes in successors:
                UpdateVertex(s,sPrimes,w,hChoice)
        
        except: 
            print("EXCEPT BLOCK")
            finished = True
            
pathCost = 0
def paintPath(paintChoice):
    global startCoordinate
    global goalCoordinate
    global parentsTable
    global pathCost
    
    goalX = goalCoordinate[1]
    goalY = goalCoordinate[0]
    
    startX = startCoordinate[1]
    startY = startCoordinate[0]
    
    tempX = goalX
    tempY = goalY
    tempParent = [goalX, goalY]
    
    if(paintChoice == 0):
        while(not(tempX == startX and tempY == startY)):
            tempParent = parentsTable[tempY][tempX]
            #print(tempParent)
            pathCost += calculateCost(tempX, tempY, tempParent[0], tempParent[1])
            tempY = tempParent[1]
            tempX = tempParent[0]
            
    else:
        while(not(tempX == startX and tempY == startY)):
            tempParent = parentsTable[tempY][tempX]
            pathCost += calculateCost(tempX, tempY, tempParent[0], tempParent[1])
            grid[tempY][tempX] = '7'
            tempY = tempParent[1]
            tempX = tempParent[0]
        
#aStar(w, hchoice), w= 0 is uniform cost search
"""
aStar(0,5)
paintPath(0) 
optimalPathCost = pathCost
print("Optimal path cost ", optimalPathCost)

nodesExpanded= 0
pathCost = 0
aStar(10,1)
paintPath(1)

stop = timeit.default_timer()
print("Path cost ", pathCost)
print("Path cost as function of optimal ", optimalPathCost/pathCost)
print("Nodes expanded ", nodesExpanded)
print("Time ", stop-start,"seconds")


"""

OPEN = []
CLOSED = []
GVALS = []
PARENTSTABLE = []


#currentCell is the item popped off from the fringe, exists in form((xCoord,yCoord),key)
def findSucc2(currentCell):
    global closedList
    
    successors = []
    
    #start by checking the cell to the upper left of x, y
    xTemp = currentCell[0][0] - 1
    yTemp = currentCell[0][1] - 1
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4'):
        successors.append((xTemp,yTemp))

    
    #check cell above x, y
    xTemp = currentCell[0][0] 
    yTemp = currentCell[0][1] - 1 
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4'):
        successors.append((xTemp,yTemp))
    

    #check cell upper right of x, y
    xTemp = currentCell[0][0] + 1
    yTemp = currentCell[0][1] - 1 
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4'):
       successors.append((xTemp,yTemp))
    
    
    #check cell right of x, y
    xTemp = currentCell[0][0] + 1
    yTemp = currentCell[0][1]  
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4'):
        successors.append((xTemp,yTemp))
    
    
    #check cell bottom right of x, y
    xTemp = currentCell[0][0] + 1
    yTemp = currentCell[0][1] + 1  
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4'):
        successors.append((xTemp,yTemp))
    
    
    #check cell below x, y
    xTemp = currentCell[0][0] 
    yTemp = currentCell[0][1] + 1 
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4'):
        successors.append((xTemp,yTemp))
    
    
    #check cell bottom left of x, y
    xTemp = currentCell[0][0] - 1
    yTemp = currentCell[0][1] + 1 
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4'):
        successors.append((xTemp,yTemp))
    
    
    #check cell left of x, y
    xTemp = currentCell[0][0]  - 1
    yTemp = currentCell[0][1]  
    successorCoordinate = [xTemp,yTemp]
    
    if(checkHighwayInBounds(xTemp, yTemp) and not grid[yTemp][xTemp] == '4'):
        successors.append((xTemp,yTemp))
    
    
    return successors


def Key(x,y,i):
    global GVALS
    global w1
    global w2
    global goalCoordinate
    
    goalX = goalCoordinate[1]
    goalY = goalCoordinate[0]
    
    g = GVALS[i][y][x]
    heur = h(i+1,x,y,goalX,goalY)
    
    return g + w1*heur
    

def ExpandStates(x,y,i):
    
    successors = findSucc2(((x,y),0))
    
    for sPrimes in successors:
        if(not sPrimes in OPEN[i] and not sPrimes in CLOSED[i]):
          
            GVALS[i][sPrimes[1]][sPrimes[0]] = 999999999
            PARENTSTABLE[i][sPrimes[1]][sPrimes[0]] = []
            
        if(GVALS[i][sPrimes[1]][sPrimes[0]] > GVALS[i][y][x] + calculateCost(x,y,sPrimes[0],sPrimes[1])):
            
            GVALS[i][sPrimes[1]][sPrimes[0]] = GVALS[i][y][x] + calculateCost(x,y,sPrimes[0],sPrimes[1])
            PARENTSTABLE[i][sPrimes[1]][sPrimes[0]] = [x,y]
            
            if(not sPrimes in CLOSED[i]):
                
                OPEN[i][(sPrimes[0],sPrimes[1])] = Key(sPrimes[0],sPrimes[1],i)

def seqAStar(n):
    global startCoordinate
    global goalCoordinate
    global OPEN
    global CLOSED
    global GVALS
    global PARENTSTABLE
    global w1
    global w2
    global nodesExpanded
    
    for i in range(0,n):
        
        
        fringe = heapdict()
        OPEN.append(fringe)
        
        CLOSED.append([])
        
        gVals = []
        #Create 120x160 table for g values
        for row in range(120):
             gVals.append([])
             for column in range(160):
                 gVals[row].append(0)  
        #Initialize all values to infinity
        for row in range(120):
            for column in range(160):
                gVals[row][column] = 999999999
                
                
        startX = startCoordinate[1]
        startY = startCoordinate[0]
    
        #g for start cell is 0 
        gVals[startY][startX] = 0
        
        goalX = goalCoordinate[1]
        goalY = goalCoordinate[0]
        
        gVals[goalY][goalX] = 999999999
        GVALS.append(gVals)
        
        
        parentsTable = []
         #Create 120x160 table to link each coordiante's parent
        for row in range(120):
            parentsTable.append([])
            for column in range(160):
                parentsTable[row].append(0)  # Append a cell
                #Initialize all values to null
        for row in range(120):
            for column in range(160):
                parentsTable[row][column] = []
                
        PARENTSTABLE.append(parentsTable)
        
        OPEN[i][(startX, startY)] = Key(startX, startY, i)
    
    while(OPEN[0].peekitem()[1] < 999999999):
        for i in range(1,n):
            if(OPEN[i].peekitem()[1] <= w2 * OPEN[0].peekitem()[1]):
                if(GVALS[i][goalY][goalX] <= OPEN[i].peekitem()[1]):
                    if(GVALS[i][goalY][goalX] < 999999999):
                        print("PATH FOUND")
                        return i
                    
                else:
                    s = OPEN[i].popitem()
                    nodesExpanded += 1
                    ExpandStates(s[0][0],s[0][1],i)
                    if(not (s[0][0],s[0][1]) in CLOSED[i]):
                        CLOSED[i].append((s[0][0],s[0][1]))
                    
            else:
                if( GVALS[0][goalY][goalX] <= OPEN[0].peekitem()[1]):
                    if(GVALS[0][goalY][goalX] <999999999 ):
                        print("PATH FOUND")
                        return 0
                else:
                    s = OPEN[0].popitem()
                    nodesExpanded += 1
                    ExpandStates(s[0][0],s[0][1],0)
                    if(not (s[0][0],s[0][1]) in CLOSED[0]):
                        CLOSED[0].append((s[0][0],s[0][1]))
     

def paintPath2(paintChoice, ay):
    global startCoordinate
    global goalCoordinate
    global PARENTSTABLE
    global pathCost
    
    goalX = goalCoordinate[1]
    goalY = goalCoordinate[0]
    
    startX = startCoordinate[1]
    startY = startCoordinate[0]
    
    tempX = goalX
    tempY = goalY
    tempParent = [goalX, goalY]
    
    if(paintChoice == 0):
        while(not(tempX == startX and tempY == startY)):
            tempParent = PARENTSTABLE[ay][tempY][tempX]
            pathCost += calculateCost(tempX, tempY, tempParent[0], tempParent[1])
            tempY = tempParent[1]
            tempX = tempParent[0]
            
    else:
        while(not(tempX == startX and tempY == startY)):
            tempParent = PARENTSTABLE[ay][tempY][tempX]
            pathCost += calculateCost(tempX, tempY, tempParent[0], tempParent[1])
            grid[tempY][tempX] = '7'
            tempY = tempParent[1]
            tempX = tempParent[0]





#COMMENT IN OR OUT IF YOU WOULD LIKE TO READ GRID INTO A FILE
#returnFile() 


#COMMENT IN OR OUT IF YOU WOULD LIKE TO READ IN A GRID
grid = readFile()  
            




#COMMENT THE ORANGE IN OR OUT IF YOU WOULD LIKE TO RUN A*
#aStar(weight, heuristicChoice)
            
#heuristic 1: euclidian distance
#heuristic 2: manhattan distance
#heuristic 3: chebychev1 distance
#heuristic 4: avoid hard to traverse centers
#heuristic 5: chebychev and avoid hard to traverse centers
            

WEIGHT = 1000        #set weight here for A*
HEURISTICCHOICE = 4  #set heuristic choice here for A*
runASTAR = False




runASTAR = True
aStar(0,1)
paintPath(0) 
optimalPathCost = pathCost
print("Optimal path cost ", optimalPathCost)


nodesExpanded= 0
pathCost = 0
aStar(WEIGHT,HEURISTICCHOICE)
paintPath(1)

stop = timeit.default_timer()
print("Path cost ", pathCost)
print("Path cost as function of optimal ", optimalPathCost/pathCost)
print("Nodes expanded ", nodesExpanded)
print("Time ", stop-start,"seconds")

            
            
            
            
            
            
#COMMENT THE ORANGE IN OR OUT IF YOU WOULD LIKE TO RUN SEQUENTIAL A*
#aStar(weight, heuristicChoice) 
w1 = 7.5            #set w1 here for sequential A*
w2 = 5           #set w2 here for sequential A*


"""      
aStar(0,1)  
paintPath(0)
optimalPathCost = pathCost
print("Optimal path cost ", optimalPathCost)      
            
pathCost = 0            
nodesExpanded = 0
            
ay = seqAStar(5)           
paintPath2(1,ay)
stop = timeit.default_timer()

print("Path cost ", pathCost)
print("Path cost as function of optimal ", optimalPathCost/pathCost)
print("Nodes expanded ", nodesExpanded)
print("Time ", stop-start,"seconds")
"""
      
                








while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
            
    
    screen.fill(BLACK)

    
    
    for row in range(120):
        for column in range(160):
            color = WHITE
            if grid[row][column] == '7': #7 is for the path
                color = RED
            if grid[row][column] == '6': #6 is for goal cell
                color = PINK
            if grid[row][column] == '5': #5 is for start cell
                color = GRAY
            if grid[row][column] == '4': #4 is for blocked cells
                color = BLUE
            if grid[row][column] == '3': #3 is for highways over hard to traverse cells
                color = GREEN
            if grid[row][column] == '2': #2 is for highways over regular cells
                color = BLACK
            if grid[row][column] == '1': #1 is for hard to traverse cells 
                color = ORANGE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    
    
    
    
    clock.tick(40)

    
    pygame.display.flip()
    
    if(runASTAR):
        X = int(input("Input X coordinate of cell to investigate"))
        Y = int(input("Input Y coordinate of cell to investigate"))
        
        
        goalX = goalCoordinate[1]
        goalY = goalCoordinate[0]
        
        
        g = gVals[Y][X]
        heur = h(HEURISTICCHOICE,X,Y,goalX, goalY)
        f = g + WEIGHT * heur
        
        print("g: ", g, " h: ", heur, " f: ", f)

pygame.quit()


