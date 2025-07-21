#main.py
import time
import copy

# make board
def printArr(arr):
  for arr2 in arr:
    for el in arr2:
      print(el, end = "")
    print()

arr = []
for i in range(30):
  arr2 = []
  for j in range(40):
    arr2.append("-")
  arr.append(arr2)

# make starting shape
def drawShape(fileName, arr):
  f = open(fileName, "r")
  lines = f.readlines()
  l = [line.split() for line in lines]
  for i in range(30):
    for j in range(40):
      correct = False
      for coords in l:
        if int(coords[0]) == i and int(coords[1]) == j:
          correct = True
      if correct:
        arr[i][j] = "O"
    
drawShape("f-pentomino.in", arr)

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


print("Welcome to Conway's Game of Life. We start with a 30x55 \ngrid of cells, either alive or dead. Here are the rules:")
print("\t1) Any live cell with fewer than two live \n\tneighbors dies, as if by underpopulation.")
print("\t2) Any live cell with two or three live neighbors \tlives on to the next generation.")
print("\t3) Any live cell with more than three live \n\tneighbors dies, as if by underpopulation.")
print("\t4) Any dead cell with exactly three live \n\tneighbors becomes a live cell, as if by \n\treproduction.")
start = input("Press Enter to continue: ")
printArr(arr)

# game
while True:
  arr2 = copy.deepcopy(arr)
  for i in range(30):
    for j in range(40):
      aliveNeighbors = neighborCheck(arr, i, j)
      if (arr[i][j] == "O"):
        if (aliveNeighbors < 2 or aliveNeighbors > 3):
          arr2[i][j] = "-"
      else:
        if (aliveNeighbors == 3):
          arr2[i][j] = "O"
  arr = arr2
  time.sleep(0.2)
  printArr(arr)
  print("\n\n\n\n\n")