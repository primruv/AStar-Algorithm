import time
from maze import*
openList = []
closedList = []
def findNeighbours(point, boundaryX, boundaryY):
    # eight directions
    x,y = point
    eastPoint,northPoint,southPoint,westPoint,northEastPoint,northWestPoint,southEastPoint,southWestPoint= (x,y+1),(x-1,y),(x+1,y),\
    (x,y-1),(x-1,y+1),(x-1,y-1),(x+1,y+1),(x+1,y-1)
 
    if eastPoint[0]<= boundaryX  and eastPoint[1]<= boundaryY and eastPoint[0] >= 0 and eastPoint[1] >= 0:
        east = eastPoint
    else :
        east = None 
    if(southPoint[0]<= boundaryX  and southPoint[1]<= boundaryY and southPoint[0] >= 0 and southPoint[1] >= 0):
        south = southPoint
    else :
        south = None         
    if(westPoint[0]<= boundaryX  and westPoint[1]<= boundaryY and westPoint[0] >= 0 and westPoint[1] >= 0):
        west = westPoint
    else :
        west = None 
    if(northPoint[0]<= boundaryX  and northPoint[1]<= boundaryY and northPoint[0] >= 0 and northPoint[1] >= 0):
        north = northPoint
    else :
        north = None
    if(northEastPoint[0]<= boundaryX  and northEastPoint[1]<= boundaryY and northEastPoint[0] >= 0 and northEastPoint[1] >= 0):
        northEast = northEastPoint
    else :
        northEast = None
    if(northWestPoint[0]<= boundaryX  and northWestPoint[1]<= boundaryY and northWestPoint[0] >= 0 and northWestPoint[1] >= 0):
        northWest = northWestPoint
    else :
        northWest = None
    if(southEastPoint[0]<= boundaryX  and southEastPoint[1]<= boundaryY and southEastPoint[0] >= 0 and southEastPoint[1] >= 0):
        southEast = southEastPoint
    else :
        southEast = None

    if(southWestPoint[0]<= boundaryX  and southWestPoint[1]<= boundaryY and southWestPoint[0] >= 0 and southWestPoint[1] >= 0):
        southWest = southWestPoint
    else :
        southWest = None
        
    return east, south, west, north,northEast,northWest,southEast,southWest
#def orientation():
    

#using diagonal Distance
#h = the estimated movement cost to move from that given square on the currentGrid to the final destination. 
def findHeuristic(currentPoint, goalPoint):
    h = max (abs(currentPoint[0] - goalPoint[0]), abs(currentPoint[1] - goalPoint[1]))
    return h
 
#g = the movement cost to move from the starting point to a given square on the currentGrid, following the path generated to get there.   
def findG(currentGrid,nextGrid):
   
    movingStraight,movingDiagonal = 2,4 #cost of moving straight and diagonal distance
    #northdirection

    ########################if value in cell is 0:
    if(world_map[nextGrid[0]][nextGrid[1]] == 0): #visit only grid with value 0
        if(currentGrid[0] == nextGrid[0]-1) and (currentGrid[1] == nextGrid[1]):
            return  movingStraight
        #eastdirection
        elif(currentGrid[0] == nextGrid[0]) and (currentGrid[1] == nextGrid[1] +1):
            return movingStraight
        #south direction
        elif(currentGrid[0] == nextGrid[0]+1) and (currentGrid[1] == nextGrid[1]):
            return movingStraight
        #west direction
        elif(currentGrid[0] == nextGrid[0]) and (currentGrid[1] == nextGrid[1] -1):
            return movingStraight
        #northEast
        elif(currentGrid[0] == nextGrid[0]-1) and (currentGrid[1] == nextGrid[1]+ 1):
            return  movingDiagonal
        #SouthEast
        elif(currentGrid[0] == nextGrid[0]+1) and (currentGrid[1] == nextGrid[1]+ 1):
            return  movingDiagonal
        #SouthWest
        elif(currentGrid[0] == nextGrid[0]+1) and (currentGrid[1] == nextGrid[1]- 1):
            return  movingDiagonal
        #NorthWest
        elif(currentGrid[0] == nextGrid[0]-1) and (currentGrid[1] == nextGrid[1]- 1):
            return  movingDiagonal
        else:
            return None

    else:
        return 100
        

    

point = (0,0)
#print(findNeighbours(point, 5,5))
#currentPoint = (1,2)
current = (1,1)
goal = (2,1)
#print(findHeuristic(current, goal))
print(findG(current,goal))
    
