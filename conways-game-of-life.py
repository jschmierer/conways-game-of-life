#main.py
import time
import copy

# you can change this to any of the shape names from the files to see how each one turns out. if you're curious, make a custom shape file yourself!
SHAPE = "glider"

# make this value bigger if you want the simulation to go slower
SPEED = 0.2

# customize the size of the board here (minimums are 30 and 30 or imported shapes will break, recommend 40+ for y though)
BOARDX = 30
BOARDY = 40

# make board
def printArr(arr):
  for arr2 in arr:
    for el in arr2:
      print(el, end = "")
    print()

arr = []
for i in range(BOARDX):
  arr2 = []
  for j in range(BOARDY):
    arr2.append("-")
  arr.append(arr2)

def drawShape(fileName, arr):
  f = open(fileName, "r")
  lines = f.readlines()
  l = [line.split() for line in lines]
  for i in range(BOARDX):
    for j in range(BOARDY):
      correct = False
      for coords in l:
        if int(coords[0]) == i and int(coords[1]) == j:
          correct = True
      if correct:
        arr[i][j] = "O"
    
drawShape(SHAPE + ".in", arr)

# game logic
def neighborCheck(arr, i, j):
  neighborCount = 0
  for k in range(i - 1, i + 2):
    for l in range(j - 1, j + 2):
      if k == i and l == j:
        pass
      elif 0 <= k < len(arr) and 0 <= l < len(arr[0]):
        if arr[k][l] == "O":
          neighborCount += 1
  return neighborCount

printArr(arr)

# game
while True:
  arr2 = copy.deepcopy(arr)
  for i in range(BOARDX):
    for j in range(BOARDY):
      aliveNeighbors = neighborCheck(arr, i, j)
      if (arr[i][j] == "O"):
        if (aliveNeighbors < 2 or aliveNeighbors > 3):
          arr2[i][j] = "-"
      else:
        if (aliveNeighbors == 3):
          arr2[i][j] = "O"
  arr = arr2
  time.sleep(SPEED)
  printArr(arr)
