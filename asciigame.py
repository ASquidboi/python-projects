import numpy as np
import os
import keyboard
#import keyboard


rows, cols = 11, 11
#grid = np.zeros((rows, cols), dtype=str) # Create a grid of zeros with integer type
grid = np.full((rows, cols), ' ')
#print(grid)
# Output:
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]

xpos = 5
ypos = 5

# Accessing and modifying elements:
while True:
  os.system("cls")
  grid[ypos, xpos] = "X"
  print(grid)
  print(xpos)
  print(ypos)
  

  #x = input("How would you like to move?")
  while True:
	  if keyboard.is_pressed("w"):
	  	grid[ypos, xpos] = " "
	  	ypos -= 1
	  	if ypos < 0:
	  		ypos = 0
	  	break
	  elif keyboard.is_pressed("s"):
	  	grid[ypos, xpos] = " "
	  	ypos += 1
	  	if ypos >= rows:
	  		ypos = rows - 1
	  	break
	  elif keyboard.is_pressed("a"):
	  	grid[ypos, xpos] = " "
	  	xpos -= 1
	  	if xpos < 0:
	  		xpos = 0
	  	break
	  elif keyboard.is_pressed("d"):
	  	grid[ypos, xpos] = " "
	  	xpos += 1
	  	if xpos >= cols:
	  		xpos = cols - 1
	  	break

  
