from turtle import Screen, Turtle
import turtle 
import time
import sys
from collections import deque

# class to create wall
class Wall(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

# class to create the start icon of the maze
class Start(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("classic")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.speed(0)

# class for the finish icon of the maze
class End(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

# show the pathway of the maze
class Pathlh(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.color("skyblue")
        self.penup()
        self.speed(0)

# ----------------------------generate maze by using the above classes------------------------------------------
def generateMaze(file):                          
    global s_x, s_y, e_x, e_y      # set up global variables for start and end locations for bfs
    for y in range(len(file)):                 # read in the file line by line
        for x in range(len(file[y])):          # read each cell in the line
            character = file[y][x]             # assign the variable "character" the x and y location of the file
            x_screen = -600 + (x * 24)          # move to the x location on the screen starting at -600
            y_screen = 270 - (y * 24)          # move to the y location of the screen starting at 270

            if character == "X":
                wall.goto(x_screen, y_screen)         # move pen to the x and y location wall
                wall.stamp()                          # stamp a copy of the maze on the screen
                walls.append((x_screen, y_screen))    # add coordinate to walls list
                mazemap.append((x_screen, y_screen)) # add coordinate to mazemap list

            if character == ".":
                pathlh.goto(x_screen, y_screen) #move pen to the x and y location maze's path
                pathlh.stamp() # stamp a copy of the maze's path on the screen
                plh.append((x_screen, y_screen)) #add coodinate to the plh list lefthand
                mazemap.append((x_screen, y_screen)) # add coordinate to mazemap list

            if character == "." or character == "e":
                path.append((x_screen, y_screen))     # add . and e to path list bfs

            if character == "e":
                # end.color("purple")
                end.goto(x_screen, y_screen)       # send end sprite to screen location
                e_x, e_y = x_screen,y_screen     # assign end locations variables to e_x and e_y
                end.stamp() #stamp a copy of the end
                finish.append((x_screen, y_screen))# add coordinate to finish list
                mazemap.append((x_screen, y_screen)) # add coordinate to mazemap list

            if character == "s":
                s_x, s_y = x_screen, y_screen  # assign start locations variables to s_x and s_y for bfs
                start.goto(x_screen, y_screen) #move pen to start
                start.stamp() #stamp a copy of the start
                starts.append((x_screen, y_screen)) #for tab function
                bfs.goto(x_screen, y_screen) #when bfs is called go to start
                lefthand.goto(x_screen, y_screen) #when lefthand is called go to start
                mazemap.append((x_screen, y_screen)) # add coordinate to mazemap list

# ------------------------------------------left hand algo-------------------------------------------------

class Lefthand(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.shape("turtle")
        self.color("blue") #turtle colour
        self.setheading(90) #turtle facing up
        self.penup()
        self.speed("fastest")
        self.counter = 0 #to count the steps
        
        self.window = Screen()
        self.window.title("PIZZA RUNNERS: Left Hand Alogrithm(0)") #initial title
        self.window.bgcolor("gray") #background colour of screen

        self.header = Turtle()
        self.header.penup()
        self.header.color("white")
        self.header.setpos(-530, 290)
        self.header.write("PIZZA RUNNERS: Done By Emily Lim Xiang Qin, DIT/FT/2B/13", font = ("Calibiri", 14, "normal")) # to be displayed above map
        self.header.hideturtle()

    def trail(self):
        self.dot("blue") #trail in the form of dot in blue colour
        self.window.title(f'PIZZA RUNNERS: Left Hand Alogrithm({1+lefthand.counter})') #count the steps

    def terminate(self): #reached end of maze, allows user to click screen to exit
        self.window.exitonclick()
        sys.exit()

    def moveUp(self):                                                      
            if (self.heading() == 90):                                    
                x = round(lefthand.xcor(), 0)   #x coordinate for current position      
                y = round(lefthand.ycor(), 0)   #y coordinate for current position
                if (x, y) in finish:
                    print("Congrats on finishing the maze using left hand algo!")
                    self.terminate()           #reached end of maze                        
                elif (x - 24, y) in walls:                    #check if left side got wall
                    if (x, y + 24) not in walls:           #front got no wall                     
                        if y == max([item[1] for item in mazemap]):# checks if the current y coordinate is the maximum y coordinate of the maze
                            self.right(90)                                    
                        else:
                            if y + 24 <= max([item[1] for item in mazemap]):# checks if the y coordinate of the path above is less than or equal to the maximum y coordinate of the maze
                                self.forward(24)                           
                                self.trail()                                  
                                self.counter += 1                             
                            else:                                    
                                self.right(90)                      
                    else: #front got wall             
                        self.right(90)                                 
                else:                              #left side no wall                            
                    if x == min([item[0] for item in mazemap]):         
                        if (x, y + 24) not in walls:                
                            if y == max([item[1] for item in mazemap]):  # checks if the current y coordinate is the maximum y coordinate of the maze      
                                self.right(90)                            
                            else:                                              
                                if y + 24 <= max([item[1] for item in mazemap]):  # checks if the y coordinate of the path above is less than or equal to the maximum y coordinate of the maze
                                    self.forward(24)                          
                                    self.trail()                            
                                    self.counter += 1                
                                else:                                           
                                    self.right(90)                            
                        else:                                                 
                            self.right(90)                                    
                    elif x > min([item[0] for item in mazemap]):     # current x coordinate is more than the minimum x coordinate of the maze          
                        if (x, y + 24) in walls: #front got wall
                            if (x - 24, y - 24) in walls: #btm left edge got wall
                                self.left(90)
                                self.forward(24)
                                self.trail()
                                self.counter += 1
                            else:
                                self.right(90)
                        else: #front no wall
                            self.left(90)                                   
                            self.forward(24)                                        
                            self.trail()                                       
                            self.counter += 1                                    
                    else:                                                     
                        self.right(90)                                  

    def moveDown(self):
        if (self.heading() == 270):
            x = round(lefthand.xcor(), 0)
            y = round(lefthand.ycor(), 0)
            if (x, y) in finish:
                print("Congrats on finishing the maze using left hand algo!")
                self.terminate()                               #reached end of maze              
            elif (x + 24, y) in walls:                                      
                if (x, y - 24) not in walls:                          
                    if y == min([item[1] for item in mazemap]):  # checks if the current y coordinate is the minimum y coordinate of the maze               
                        self.right(90)                           
                    else:      
                        if y - 24 >= min([item[1] for item in mazemap]): 
                            self.forward(24)                      
                            self.trail()                              
                            self.counter += 1                 
                        else:      
                            self.right(90)                     
                else:                                            
                    self.right(90)             
            else:                                                       
                if x == max([item[0] for item in mazemap]):                
                    if (x, y - 24) not in walls:                           
                        if y == min([item[1] for item in mazemap]):       
                            self.right(90)                              
                        else:                                         
                            if y - 24 >= min([item[1] for item in mazemap]):  
                                self.forward(24)                           
                                self.trail()                             
                                self.counter += 1                           # adds a step to the counter
                            else:                                           # y coordinate of the path below is less than the minimum y coordinate of the maze
                                self.right(90)                              # turn 90 degrees to the right
                    else:                                                   # the path below is not clear
                        self.right(90)                                           # turn 90 degrees to the right
                elif x < max([item[0] for item in mazemap]):                  # current x coordinate is less than the maximum x coordinate of the maze
                    if (x, y - 24) in walls:
                        if (x + 24, y + 24) in walls:
                            self.left(90)
                            self.forward(24)
                            self.trail()
                            self.counter += 1
                        else:
                            self.right(90)
                    else:
                        self.left(90)                                           # turn 90 degrees to the left
                        self.forward(24)                                        # move forward by 1 square (24 pixels)
                        self.trail()                                            # leaves a trail behind
                        self.counter += 1                                       # adds a step to the counter
                else:                                                       # current x coordinate is more than the maximum x coordinate of the maze
                    self.right(90)                                  
                
    def moveLeft(self):                                              
        if (self.heading() == 180):                                        
            x = round(lefthand.xcor(), 0)                                 
            y = round(lefthand.ycor(), 0)                                    
            if (x, y) in finish:                       
                print("Congrats on finishing the maze using left hand algo!")                 
                self.terminate()                        #reached end of maze                 
            elif (x, y - 24) in walls:                                     
                if (x - 24, y) not in walls:                              
                    if x == min([item[0] for item in mazemap]): # checks if current x coordinate is the minimum x coordinate of the maze      
                        self.right(90)                                    
                    else:                                              
                        if x - 24 >= min([item[0] for item in mazemap]):  # checks if the x coordinate of the path on the left is more than or equal to the minimum x coordinate of the maze
                            self.forward(24)                               
                            self.trail()                            
                            self.counter += 1                            
                        else:                                              
                            self.right(90)                                
                else:                                                  
                    self.right(90)                      
            else:                                                           
                if y == min([item[1] for item in mazemap]): # checks if the current y coordinate is the minimum y coordinate of the maze      
                    if (x - 24, y) not in walls:                            
                        if x == min([item[0] for item in mazemap]): # checks if the current x coordinate is the minimum x coordinate of the maze         
                            self.right(90)                           
                        else:                                               
                            if x - 24 >= min([item[0] for item in mazemap]): # checks if the x coordinate of the path on the left is more than or equal to the minimum x coordinate of the maze 
                                self.forward(24)                          
                                self.trail()                          
                                self.counter += 1                       
                            else:                                          
                                self.right(90)                            
                    else:                                           
                        self.right(90)                      
                elif y > min([item[1] for item in mazemap]): # current y coordinate is more than the minimum y coordinate of the maze            
                    if (x - 24, y) in walls: #front got wall
                        if (x + 24, y - 24) in walls:
                            self.left(90)
                            self.forward(24)
                            self.trail()
                            self.counter += 1
                        else:
                            self.right(90)
                    else: #front no wall
                        self.left(90)                                  
                        self.forward(24)                                       
                        self.trail()                              
                        self.counter += 1                                    
                else:                                                   
                    self.right(90)                                      

    def moveRight(self):                                                   
        if (self.heading() == 0):                                           
            x = round(lefthand.xcor(), 0)                                    
            y = round(lefthand.ycor(), 0)                                  
            if (x, y) in finish:                 
                print("Congrats on finishing the maze using left hand algo!")                          
                self.terminate()                      #reached end of maze               
            elif (x, y + 24) in walls:  #left got wall                   
                if (x + 24, y) not in walls:  #front no wall                             
                    if x == max([item[0] for item in mazemap]):    # checks if the current x coordinate is the maximum x coordinate of the maze      
                        self.right(90)                                
                    else:                                                   
                        if x + 24 <= max([item[0] for item in mazemap]):   # checks if the x coordinate of the path on the right is less than or equal to the maximum x coordinate of the maze 
                            self.forward(24)                              
                            self.trail()                              
                            self.counter += 1                         
                        else:                                               
                            self.right(90)                              
                else:   #front got wall                                                  
                    self.right(90)                                       
            else:   #left no wall                                                      
                if y == max([item[1] for item in mazemap]):   # checks if the current y coordinate is the maximum y coordinate of the maze                
                    if (x + 24, y) not in walls:  #right side no wall                          
                        if x == max([item[0] for item in mazemap]): # checks if the current x coordinate is the maximum x coordinate of the maze         
                            self.right(90)                          
                        else:                                           
                            if x + 24 <= max([item[0] for item in mazemap]): # checks if the x coordinate of the path on the right is less than or equal to the minimum x coordinate of the maze
                                self.forward(24)                          
                                self.trail()                              
                                self.counter += 1                           
                            else:                                       
                                self.right(90)                             
                    else:                                                 
                        self.right(90)                                   
                elif y < max([item[1] for item in mazemap]): # current y coordinate is less than the maximum y coordinate of the maze
                    if (x + 24, y) in walls: #front got wall
                        if (x - 24, y + 24) in walls:
                            self.left(90)
                            self.forward(24)
                            self.trail()
                            self.counter += 1
                        else:
                            self.right(90)
                    else: #front no wall
                        self.left(90)                                  
                        self.forward(24)                           
                        self.trail()                                  
                        self.counter += 1                                  
                else:                                                  
                    self.right(90)                                      

    def noloop(self):
        while True:
            if (round(lefthand.xcor(), 0), round(lefthand.ycor(), 0)+24) not in plh or (round(lefthand.xcor(), 0),round(lefthand.ycor(), 0)-24) not in plh or (round(lefthand.xcor(), 0)-24,round(lefthand.ycor(), 0)) not in plh or (round(lefthand.xcor(), 0)+24,round(lefthand.ycor(), 0)) not in plh or (round(lefthand.xcor(), 0)-24,round(lefthand.ycor(), 0)+24) not in plh or (round(lefthand.xcor(), 0)+24,round(lefthand.ycor(), 0)+24) not in plh or (round(lefthand.xcor(), 0)-24,round(lefthand.ycor(), 0)-24) not in plh or (round(lefthand.xcor(), 0)+24,round(lefthand.ycor(), 0)-24) not in plh: #condition which will allow moving icon to check for walls and use left hand
                self.moveUp()
                self.moveDown()
                self.moveLeft()
                self.moveRight()
            else: # use this to find wall
                self.setheading(90)
                self.forward(24)
                self.trail()
                self.counter += 1
                self.setheading(0)

#---------------------------------------breadth first search algo-----------------------------------------------

class Bfs(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.shape("turtle")
        self.color("magenta") #turtle colour
        self.setheading(90) #turtle facing up
        self.penup()
        self.speed("fastest")
        self.counter = 0 #to count the steps

        self.window = Screen()
        self.window.title("PIZZA RUNNERS: Breadth-first search Alogrithm(0)") #initial title
        self.window.bgcolor("gray") #background colour of screen

        self.header = Turtle()
        self.header.penup()
        self.header.color("white")
        self.header.setpos(-530, 290)
        self.header.write("PIZZA RUNNERS: Done By Emily Lim Xiang Qin, DIT/FT/2B/13", font = ("Calibiri", 14, "normal")) #to be displayed above the map
        self.header.hideturtle()

    def trail(self):
        self.dot("magenta") #trail in the form of dot in magenta colour
        self.window.title(f'PIZZA RUNNERS: Breadth-first search Alogrithm({1+bfs.counter})') #count the steps

    def terminate(self):  #reached end of maze, allows the user to click on screen and exit
        self.window.exitonclick()
        sys.exit()

    def up(self):
        if (self.heading() == 90):
            x = round(bfs.xcor(), 0)  #x coordinate for current position
            y = round(bfs.ycor(), 0)  #y coordinate for current position
            if (x, y) in finish:
                print("Congrats on finishing the maze using breadth-first search algo!")
                self.terminate() #reached end of maze
                
            elif (x, y + 24) not in shortestpath: #front not in shortest path
                if (x - 24, y) not in shortestpath: #left not in shortest path
                    self.setheading(0)
                    self.forward(24)
                    self.trail()
                    self.counter += 1
                if (x + 24, y) not in shortestpath: #right not in shortest path
                    self.setheading(180)
                    self.forward(24)
                    self.trail()
                    self.counter += 1
            else: # if path in front is the shortest path
                self.forward(24)
                self.trail()
                self.counter += 1

    def down(self):
        if (self.heading() == 270):
            x = round(bfs.xcor(), 0)
            y = round(bfs.ycor(), 0)
            if (x, y) in finish:
                print("Congrats on finishing the maze using breadth-first search algo!")
                self.terminate()  #reached end of maze
            elif (x, y - 24) not in shortestpath:
                if (x - 24, y) not in shortestpath: #right not in shortest path
                    self.setheading(0)
                    self.forward(24)
                    self.trail()
                    self.counter += 1
                if (x + 24, y) not in shortestpath: #left not in shortest path
                    self.setheading(180)
                    self.forward(24)
                    self.trail()
                    self.counter += 1
            else: # if path in front is the shortest path
                self.forward(24)
                self.trail()
                self.counter += 1

    def left(self):
        if (self.heading() == 180):
            x = round(bfs.xcor(), 0)
            y = round(bfs.ycor(), 0)
            if (x, y) in finish:
                print("Congrats on finishing the maze using breadth-first search algo!")
                self.terminate() #reached end of maze
            elif (x - 24, y) not in shortestpath: #front not in shortest path
                if (x, y - 24) not in shortestpath: #left not in shortest path
                    self.setheading(90)
                    self.forward(24)
                    self.trail()
                    self.counter += 1
                if (x, y + 24) not in shortestpath: #right not in shortest path
                    self.setheading(270)
                    self.forward(24)
                    self.trail()
                    self.counter += 1
            else: # if path in front is the shortest path
                self.forward(24)
                self.trail()
                self.counter += 1

    def right(self):
        if (self.heading() == 0):
            x = round(bfs.xcor(), 0)
            y = round(bfs.ycor(), 0)
            if (x, y) in finish:
                print("Congrats on finishing the maze using breadth-first search algo!")
                self.terminate() #reached end of maze
            elif (x + 24, y) not in shortestpath: #front not in shortest path
                if (x, y - 24) not in shortestpath: #right not in shortest path
                    self.setheading(90)
                    self.forward(24)
                    self.trail()
                    self.counter += 1
                if (x, y + 24) not in shortestpath: #left not in shortest path
                    self.setheading(270)
                    self.forward(24)
                    self.trail()
                    self.counter += 1
            else: # if path in front is the shortest path
                self.forward(24)
                self.trail()
                self.counter += 1

    def search(self, x,y): #search the path
        frontier.append((x, y))
        solution[x,y] = x,y

        while len(frontier) > 0:          # exit while loop when frontier queue equals zero
            time.sleep(0)
            x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

            if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left has not been walked
                cell = (x - 24, y)
                solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
                frontier.append(cell)   # add cell to frontier list
                visited.add((x-24, y))  # add cell to visited list

            if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down has not been walked
                cell = (x, y - 24)
                solution[cell] = x, y
                frontier.append(cell)
                visited.add((x, y - 24)) 

            if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the right has not been walked
                cell = (x + 24, y)
                solution[cell] = x, y
                frontier.append(cell)
                visited.add((x +24, y))

            if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up has not been walked
                cell = (x, y + 24)
                solution[cell] = x, y
                frontier.append(cell)
                visited.add((x, y + 24))

    def backRoute(self, x, y): #have the shortest path route
        shortestpath.append((x, y))
        while (x, y) != (s_x, s_y):    # stop loop when current cells == start cell
            shortestpath.append((x, y))
            x, y = solution[x, y]             
        shortestpath.append((x, y))

# --------------------------------------- tab switch for each algo --------------------------------------------
settab = False #at the start when tab is not used
class tabswitch():
    def lhs_tab(self):
        while True: #call the lefthand algo
            lefthand.moveUp()
            lefthand.moveDown()
            lefthand.moveLeft()
            lefthand.moveRight()
            lefthand.noloop()

    def bfs_tab(self):
        while True: #call the bfs algo
            bfs.up()
            bfs.down()
            bfs.left()
            bfs.right()

    def tab(self):
        global settab
        settab = not settab #changes when user press 'tab' key
        if settab == True:
            bfs.hideturtle() #hide to prevent 2 turtles from showing
            lefthand.showturtle() #show as lefthand is ongoing
            bfs.goto(starts[0][0],starts[0][1]) #go to the start s
            bfs.clear()
            bfs.counter = 0 #reset the number of steps
            tabswitch.lhs_tab() #call the above function
        else:
            lefthand.hideturtle() #hide to prevent 2 turtles from showing
            bfs.showturtle() #show as bfs is ongoing
            lefthand.goto(starts[0][0],starts[0][1]) #go to the start s
            lefthand.clear()
            lefthand.counter = 0 #reset the number of steps
            bfs.search(s_x,s_y)
            bfs.backRoute(e_x, e_y)
            tabswitch.bfs_tab() #call the above function

    def endprog(self):
        scr.exitonclick() #when user press the screen, allows user to exit

setreset = False
class mazereset():
    def lhs_reset(self): #reset the lefthand algo 
        while True:
            lefthand.moveUp()
            lefthand.moveDown()
            lefthand.moveLeft()
            lefthand.moveRight()
            lefthand.noloop()
    def bfs_reset(self): #reset bfs algo
        while True:
            bfs.up()
            bfs.down()
            bfs.left()
            bfs.right()   

    def reset(self):
        global setreset
        if setreset == False:
            if lefthand.isvisible() == True:
                lefthand.clear()
                bfs.hideturtle() #hide to prevent 2 turtles from showing
                lefthand.goto(starts[0][0],starts[0][1]) #go to the start s
                lefthand.counter = 0
                lefthand.showturtle() #show as lefthand is ongoing
                mazereset.lhs_reset()
            elif bfs.isvisible() == True:
                bfs.clear()
                lefthand.hideturtle() #hide to prevent 2 turtles from showing
                bfs.goto(starts[0][0],starts[0][1]) #go to the start s
                bfs.counter = 0
                bfs.showturtle() #show as lefthand is ongoing
                mazereset.bfs_reset()
     
    def endprog(self):
        scr.exitonclick() #when user press the screen, allows user to exit

# -------------------------------------------------- pause function --------------------------------------------------

def pause():
    time.sleep(2) #when user press 'space' key, moving icon will stop moving for 2 seconds


        
# Open and read file as file
file = open("C:/Users/emily/Documents/DSAA/ca1/maze9.txt", "r")
file = file.readlines()
print(file)

# set up classes
wall = Wall()
pathlh = Pathlh() #show the pathway for map
start = Start()
end = End()
lefthand = Lefthand()
bfs = Bfs()
tabswitch = tabswitch()
mazereset = mazereset()

# setup lists
walls = []
path = [] #pathway for bfs
plh = [] # pathway for lefthand
shortestpath = [] #for bfs
finish = [] #store the coordinates of the ending
starts = [] #store the coordinates of the starting
mazemap = [] # coordinates of the whole maze


visited = set() #path walked already
frontier = deque()
solution = {} # solution dictionary

# main program 

scr = turtle.Screen()
# Window dimension (go for fullscreen window)
scr.setup(width=1.0, height=1.0) 

generateMaze(file)

scr.listen()
scr.onkey(tabswitch.tab, 'Tab')
scr.onkey(mazereset.reset, 'r')
scr.onkey(pause, 'p')

# --------------------- user click on screen when program not running and is able to exit ---------------------
tabswitch.endprog()
mazereset.endprog()
scr.exitonclick()




