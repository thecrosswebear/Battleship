from random import randint

grid = []

myNumber = int(raw_input ('Entrez un chiffre svp:'))

for i in range(0,myNumber):
	grid.append(['O'] * myNumber)

for i in range(1,myNumber):
	print "*",
print ('\n')
print 'Random thing: ' ,randint(0,myNumber)

def printGrid():
	for row in grid:
		print (" ").join(row)
	print ('\n')

printGrid()

grid[randint(0,myNumber)-1][randint(0,myNumber)-1] = 'X'

printGrid()