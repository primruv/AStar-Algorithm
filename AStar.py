from ev3dev.ev3 import *
import heapq as h
from time import sleep

rightMotor = ev3.LargeMotor('outB') #setting a motor in portB
leftMotor = ev3.LargeMotor('outC') #setting a motor in portC

BOUNDARY_Y,BOUNDARY_X = 5,5
start =(0, 3)
goal = (3, 4)
#This is a priorityQueue implemented with heaps
# define PriorityQueue to store class objects if we override Priority Queue functions particularly  __cmp__()
#because it stores tuples
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        h.heappush(self.elements, (priority, item))
    
    def get(self):
        return h.heappop(self.elements)[1]
    
    def heapify(self,list):
        return h.heapify(list)

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

def findNeighbours(point, BOUNDARY_X, BOUNDARY_Y):
    # eight directions
    x = point[0]
    y=point[1]
    eastPoint,northPoint,southPoint,westPoint,northEastPoint,northWestPoint,southEastPoint,southWestPoint= (x,y+1),(x-1,y),(x+1,y),\
    (x,y-1),(x-1,y+1),(x-1,y-1),(x+1,y+1),(x+1,y-1)
 
    if eastPoint[0]<= BOUNDARY_X  and eastPoint[1]<= BOUNDARY_Y and eastPoint[0] >= 0 and eastPoint[1] >= 0:
        east = eastPoint
        
    else :
        east = None 
    if(southPoint[0]<= BOUNDARY_X  and southPoint[1]<= BOUNDARY_Y and southPoint[0] >= 0 and southPoint[1] >= 0):
        south = southPoint
    else :
        south = None         
    if(westPoint[0]<= BOUNDARY_X  and westPoint[1]<= BOUNDARY_Y and westPoint[0] >= 0 and westPoint[1] >= 0):
        west = westPoint
    else :
        west = None 
    if(northPoint[0]<= BOUNDARY_X  and northPoint[1]<= BOUNDARY_Y and northPoint[0] >= 0 and northPoint[1] >= 0):
        north = northPoint
    else :
        north = None
    if(northEastPoint[0]<= BOUNDARY_X  and northEastPoint[1]<= BOUNDARY_Y and northEastPoint[0] >= 0 and northEastPoint[1] >= 0):
        northEast = northEastPoint
    else :
        northEast = None
    if(northWestPoint[0]<= BOUNDARY_X  and northWestPoint[1]<= BOUNDARY_Y and northWestPoint[0] >= 0 and northWestPoint[1] >= 0):
        northWest = northWestPoint
    else :
        northWest = None
    if(southEastPoint[0]<= BOUNDARY_X  and southEastPoint[1]<= BOUNDARY_Y and southEastPoint[0] >= 0 and southEastPoint[1] >= 0):
        southEast = southEastPoint
    else :
        southEast = None

    if(southWestPoint[0]<= BOUNDARY_X  and southWestPoint[1]<= BOUNDARY_Y and southWestPoint[0] >= 0 and southWestPoint[1] >= 0):
        southWest = southWestPoint
    else :
        southWest = None
        
    return east, south, west, north,northEast,northWest,southEast,southWest

#finding the next cell in a map using the findNeighbour function on a map
###################################
def traversingNeighbour(world_arr, currentCell):
    queue = []
    east,north,south,west,northEast,northWest,southEast,southWest = findNeighbours(currentCell, len(world_arr)-1, len(world_arr)-1)
    if east != None and world_arr[east[0]][east[1]] ==0:
       world_arr[east[0]][east[1]] = world_arr[currentCell[0]][currentCell[1]] + 1
       queue.append(east)

    if south != None and world_arr[south[0]][south[1]] ==0:
        world_arr[south[0]][south[1]] = world_arr[currentCell[0]][currentCell[1]] + 1
        queue.append(south)

    if west != None and world_arr[west[0]][west[1]] == 0:
        world_arr[west[0]][west[1]] = world_arr[currentCell[0]][currentCell[1]] + 1
        queue.append(west)
        
    if north != None and world_arr[north[0]][north[1]] == 0:
        world_arr[north[0]][north[1]] = world_arr[currentCell[0]][currentCell[1]] + 1
        queue.append(north)

    if northEast != None and world_arr[northEast[0]][northEast[1]] ==0:
        world_arr[northEast[0]][northEast[1]] = world_arr[currentCell[0]][currentCell[1]] + 1
        queue.append(northEast)

    if northWest != None and world_arr[northWest[0]][northWest[1]] ==0:
        world_arr[northWest[0]][northWest[1]] = world_arr[currentCell[0]][currentCell[1]] + 1
        queue.append(northWest)

    if southEast != None and world_arr[southEast[0]][southEast[1]] == 0:
        world_arr[southEast[0]][southEast[1]] = world_arr[currentCell[0]][currentCell[1]] + 1
        queue.append(southEast)
        
    if southWest != None and world_arr[southWest[0]][southWest[1]] == 0:
        world_arr[southWest[0]][southWest[1]] = world_arr[currentCell[0]][currentCell[1]] + 1
        queue.append(southWest)

    return queue



#using diagonal Distance
#h = the estimated movement cost to move from that given square on the currentGrid to the final destination. 
def findHeuristic(currentPoint, goalPoint):
    h = max (abs(currentPoint[0] - goalPoint[0]), abs(currentPoint[1] - goalPoint[1]))
    return h
 
#g = the movement cost to move from the starting point to a given square on the currentGrid, following the path generated to get there.   
def findG(currentCell,nextCell):
   
    movingStraight,movingDiagonal = 2,30 #cost of moving straight and diagonal distance
    #northdirection

    ########################if value in cell is 0:
    if(world_map[nextCell[0]][nextCell[1]] == 0): #visit only grid with value 0
        #northdirection
        if(currentCell[0] == nextCell[0]-1) and (currentCell[1] == nextCell[1]):
            return  movingStraight
        #eastdirection
        elif(currentCell[0] == nextCell[0]) and (currentCell[1] == nextCell[1] +1):
            return movingStraight
        #south direction
        elif(currentCell[0] == nextCell[0]+1) and (currentCell[1] == nextCell[1]):
            return movingStraight
        #west direction
        elif(currentCell[0] == nextCell[0]) and (currentCell[1] == nextCell[1] -1):
            return movingStraight
        #northEast
        elif(currentCell[0] == nextCell[0]-1) and (currentCell[1] == nextCell[1]+ 1):
            return  movingDiagonal
        #SouthEast
        elif(currentCell[0] == nextCell[0]+1) and (currentCell[1] == nextCell[1]+ 1):
            return  movingDiagonal
        #SouthWest
        elif(currentCell[0] == nextCell[0]+1) and (currentCell[1] == nextCell[1]- 1):
            return  movingDiagonal
        #NorthWest
        elif(currentCell[0] == nextCell[0]-1) and (currentCell[1] == nextCell[1]- 1):
            return  movingDiagonal
        
    #if the value is 1 of a cell return a big number so that it doesn't even consider it.
    else:
       return 100
 
#a priority queue, an element with high priority is served before an element with low priority.
#If two elements have the same priority, they are served according to their order in the queue
came_from = {} 
def astarTotalCost(wmap, start, goal):
    priorityQ = PriorityQueue()
    priorityQ.put(start, 0)
    global came_from
    came_from[start] = None
    cost_so_far = {} 
    cost_so_far[start] = 0
    

    while not priorityQ.empty():
       currentCell = priorityQ.get()

       if currentCell == goal:
          break
       
       for successor in traversingNeighbour(wmap, currentCell):
          currentCost = cost_so_far[currentCell] + findG(currentCell, successor)
          if successor not in cost_so_far or currentCost < cost_so_far[successor]:
             cost_so_far[successor] = currentCost
             totalCost = currentCost + findHeuristic(successor, goal)
             priorityQ.put(successor, totalCost)
             came_from[successor] = currentCell
    
    
    
    #return came_from,cost_so_far
    return came_from,cost_so_far
  

def reconstruct_path(start, goal):
    global came_from
    cell = goal
    path = []
    while cell != start:
        path.append(cell)
        cell = came_from[cell]
    path.append(start) 
    path.reverse()
    return path
    

#problem not passing all came_from elements make it global
def findPath():
    global came_from
    shortpath = []
    astarTotalCost(world_map, start, goal) # strange line
    print("path is :")
    shortpath = reconstruct_path(start, goal)
    return(shortpath)

print(findPath())
def relDirections(point):
    print(point)
    east, south, west, north,northEast,northWest,southEast,southWest = findNeighbours(point, BOUNDARY_X, BOUNDARY_Y)
    if east:
        orientation = 7
        return orientation
    elif south:
        orientation = 5
        return orientation
    elif west:
        orientation = 3
        return orientation
    elif north:
        orientation = 1
        return orientation
        
    elif northEast:
        orientation = 8
        return orientation
    elif northWest:
        orientation = 2
        return orientation
    elif southEast:
        orientation = 6
        return orientation
    
    elif southWest:
        orientation = 4
        return orientation
        
def relDirection(pos1, pos2):
    (x1, y1) = pos1
    (x2, y2) = pos2
    if x2==x1 and y2==y1+1:
        dir = 0
    elif x2==x1+1 and y2==y1:
        dir = 1
    elif x2==x1 and y2==y1-1:
        dir = 2
    elif x2==x1-1 and y2==y1:
        dir = 3
    elif x2==x1+1 and y2==y1+1:
        dir = 4
    elif x2==x1+1 and y2==y1-1:
        dir = 5
    elif x2==x1-1 and y2==y1-1:
        dir = 6
    elif x2==x1-1 and y2==y1+1:
        dir = 7
    else:
        raise ValueError(str(pos1)+" and " + str(pos2) + " are not neighbors,"\
                         +"so cannot compute relative direction between them.")
    return dir
    
startPosition = start
path = findPath()
path.pop(0)
startOrientation = 0 #east

def followPath(startPosition, startOrientation, path):
    curPos = startPosition
    curDir = startOrientation
    # Names of cardinal directions corresponding to the integers 0, 1, 2, and 3
    directions = ['east','south','west','north', 'southeast',  'southwest', 'northwest', 'northeast']

    for i in range(len(path)):
        nextPos = path[i]
        if curPos == goal:
          return
        relDir = relDirection(curPos, nextPos)
        print("At pos " + str(curPos) + " facing direction " + str(curDir)
              + " (" + directions[curDir] + ")")
        print("Next pos is " + str(nextPos)
              + ", whose direction relative to the current pos is "
              + str(relDir) + " (" + directions[relDir] + ")")
        print()
        
        # For the curDir == 0-----------------------------------------------
        if directions[curDir] == 'east' and directions[relDir] == 'east':
            straight_line(70,150)
        elif directions[curDir] == 'east' and directions[relDir] == 'south':
            spinRight(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'east' and directions[relDir] == 'north':
            spinLeft(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'east' and directions[relDir] == 'west':
            spinRight(180,100) 
            straight_line(70,150)
        elif directions[curDir] == 'east' and directions[relDir] == 'northeast':
            spinLeft(45,100) 
            straight_line(70,150)
        elif directions[curDir] == 'east' and directions[relDir] == 'southeast':
            spinRight(45,100)
            straight_line(70,150)
        elif directions[curDir] == 'east' and directions[relDir] == 'northwest':
            spinLeft(135,100)
            straight_line(70,150)
        elif directions[curDir] == 'east' and directions[relDir] == 'southwest':
            spinRight(135,100) 
            straight_line(70,150)

        # For the curDir == 1-----------------------------------------------
        if directions[curDir] == 'south' and directions[relDir] == 'south':
            straight_line(70,150)
        elif directions[curDir] == 'south' and directions[relDir] == 'west':
            spinRight(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'south' and directions[relDir] == 'north':
            spinL(180,100)
            straight(70,150)
        elif directions[curDir] == 'south' and directions[relDir] == 'east':
            spinLeft(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'south' and directions[relDir] == 'southeast':
            spinLeft(45,100)
            straight_line(70,150)
        elif directions[curDir] == 'south' and directions[relDir] == 'southwest':
            spinRight(45,100)
            straight_line(70,150) 
        elif directions[curDir] == 'south' and directions[relDir] == 'northwest':
            spinRight(135,100)
            straight_line(70,150)
        elif directions[curDir] == 'south' and directions[relDir] == 'east':
            spinLeft(135,100)
            straight_line(70,150)
            
        # For the curDir == 2-----------------------------------------------
        if directions[curDir] == 'west' and directions[relDir] == 'west':
            straight_line(70,150)
        elif directions[curDir] == 'west' and directions[relDir] == 'north':
            spinRight(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'west' and directions[relDir] == 'east':
            spinLeft(180,100)
            straight_line(70,150)
        elif directions[curDir] == 'west' and directions[relDir] == 'south':
            spinLeft(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'west' and directions[relDir] == 'northwest':
            spinRight(45,100)
            straight_line(70,150)
        elif directions[curDir] == 'west' and directions[relDir] == 'northeast':
            spinRight(135,100)
            straight_line(70,150)
        elif directions[curDir] == 'west' and directions[relDir] == 'southeast':
            spinLeft(135,100)
            straight_line(70,150)
        elif directions[curDir] == 'west' and directions[relDir] == 'southwest':
            spinLeft(45,100)
            straight_line(70,150)

        
        # For the curDir == 3-----------------------------------------------
        if directions[curDir] == 'north' and directions[relDir] == 'north':
            straight_line(70,150)
        elif directions[curDir] == 'north' and directions[relDir] == 'east':
            spinRight(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'north' and directions[relDir] == 'south':
            spinLeft(180,100)
            straight_line(70,150)
        elif directions[curDir] == 'north' and directions[relDir] == 'west':
            spinLeft(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'north' and directions[relDir] == 'northwest':
            spinLeft(45,100)
            straight_line(70,150)
        elif directions[curDir] == 'north' and directions[relDir] == 'northeast':
            spinRight(45,100)
            straight_line(70,150)
        elif directions[curDir] == 'north' and directions[relDir] == 'southeast':
            spinRight(135,100)
            straight_line(70,150)
        elif directions[curDir] == 'north' and directions[relDir] == 'southwest':
            spinLeft(135,100)
            straight_line(70,150)
          # For the curDir == 4-----------------------------------------------
        if directions[curDir] == 'southeast' and directions[relDir] == 'east':
            spinLeft(45,100)
            straight_line(70,150)
        elif directions[curDir] == 'southeast' and directions[relDir] == 'south':
            spinRight(45,100)
            straight_line(70,150)
        elif directions[curDir] == 'southeast' and directions[relDir] == 'north':
            spinLeft(135,100)
            straight_line(70,150)
        elif directions[curDir] == 'southeast' and directions[relDir] == 'west':
            spinRight(135,100) 
            straight_line(70,150)
        elif directions[curDir] == 'southeast' and directions[relDir] == 'northeast':
            spinLeft(90,100) 
            straight_line(70,150)
        elif directions[curDir] == 'southeast' and directions[relDir] == 'southeast':
            straight_line(70,150)
        elif directions[curDir] == 'southeast' and directions[relDir] == 'northwest':
            spinLeft(180,100)
            straight_line(70,150)
        elif directions[curDir] == 'southeast' and directions[relDir] == 'southwest':
            spinRight(90,100) 
            straight_line(70,150)  
            

        # For the curDir == 5-----------------------------------------------
        if directions[curDir] == 'southwest' and directions[relDir] == 'south':
            spinLeft(45,100)
            straight_line(70,150)
        elif directions[curDir] == 'southwest' and directions[relDir] == 'west':
            spinRight(45,100)
            straight_line(70,150) 
        elif directions[curDir] == 'southwest' and directions[relDir] == 'north':
            spinRight(135,100)
            straight_line(70,150)
        elif directions[curDir] == 'southwest' and directions[relDir] == 'east':
            spinLeft(135,100)
            straight_line(70,150)
        elif directions[curDir] == 'southwest' and directions[relDir] == 'southeast':
            spinLeft(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'southwest' and directions[relDir] == 'southwest':
            straight_line(70,150)
        elif directions[curDir] == 'southwest' and directions[relDir] == 'northwest':
            spinRight(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'southwest' and directions[relDir] == 'northeast':
            spinRight(180,100)
            straight_line(70,150)
        
        # For the curDir == 6-----------------------------------------------
        if directions[curDir] == 'northwest' and directions[relDir] == 'west':
            spinLeft(45,100)
            straight_line(50,150)
        elif directions[curDir] == 'northwest' and directions[relDir] == 'north':
            spinR(45,100)
            straight_line(50,150)
        elif directions[curDir] == 'northwest' and directions[relDir] == 'east':
            spinR(135,100)
            straight_line(50,150)
        elif directions[curDir] == 'northwest' and directions[relDir] == 'south':
            spinLeft(135,100)
            straight_line(50,150)
        elif directions[curDir] == 'northwest' and directions[relDir] == 'northwest':
            straight_line(50,150)
        elif directions[curDir] == 'northwest' and directions[relDir] == 'northeast':
            spinR(90,100)
            straight_line(50,150)
        elif directions[curDir] == ' northwest' and directions[relDir] == 'southeast':
            spinLeft(180,100)
            straight_line(50,150)
        elif directions[curDir] == 'northwest' and directions[relDir] == 'southwest':
            spinLeft(90,100)
            straight_line(70,150)

        
        # For the curDir == 7-----------------------------------------------
        if directions[curDir] == 'northeast' and directions[relDir] == 'northeast' :
            straight_line(70,150)
        elif directions[curDir] == 'northeast'  and directions[relDir] == 'east':
            spinRight(45,100)
            straight_line(70,150)
        elif directions[curDir] == 'northeast'  and directions[relDir] == 'south':
            spinRight(135,100)
            straight_line(70,150)
        elif directions[curDir] == 'northeast'  and directions[relDir] == 'west':
            spinLeft(135,100)
            straight_line(70,150)
        elif directions[curDir] == 'northeast'  and directions[relDir] == 'northwest':
            spinLeft(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'northeast'  and directions[relDir] == 'north':
            spinLeft(45,100)
            straight_line(70,150)
        elif directions[curDir] == 'northeast'  and directions[relDir] == 'southeast':
            spinRight(90,100)
            straight_line(70,150)
        elif directions[curDir] == 'northeast'  and directions[relDir] == 'southwest':
            spinRight(180,100)
            straight_line(70,150)


        # Update the current position and orientation
        curPos = nextPos
        curDir = relDir


         
followPath(startPosition, startOrientation, path)

#print(findNeighbours(point, 5,5))
#currentPoint = (1,2)


#print(findPath())
#(findG(start,nextCell))
#print(findNeighbours(start, 7,7))
#print(traversingNeighbour(world_map, start))
#print(astarTotalCost(world_map,start,goal))
#
#print('compare came from and this')
#astarTotalCost(world_map,start,goal)


#print(orientation(start))
#print(findNeighbours(start, 5,5))
#print("given point ", start, " my neighbours are: ",findNeighbours(start, 5,5))
#print(traversingNeighbour(world_map, start))

#h = findHeuristic(currentPoint, goalPoint)
#print(findHeuristic(current, goal))
#print(findG(current,goal))
    


