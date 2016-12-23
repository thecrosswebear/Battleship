# coding=utf-8

from random import randint 

HORIZONTAL = 0
VERTICAL = 1
GRIDSIZE = 10

class Boat(object):
	def __init__(self, pointDeVie, x, y, orientation, kind):
		self.pointDeVie = pointDeVie
		self.x = x
		self.y = y
		self.orientation = orientation
		self.kind = kind

# 2 holes
class Destroyer(Boat):
	def __init__(self, x, y, orientation):
		super(Destroyer, self).__init__(2, x, y, orientation, "Destroyer")
# 3 holes	
class Submarine(Boat):
	def __init__(self):
		super(Submarine,self).__init__(3, x, y, orientation, "Submarine")
# 3 holes
class Cruiser(Boat):
	def __init__(self):
		super(Cruiser, self).__init__(3,x, y, orientation, "Cruiser")
# 4 holes
class Battleship(Boat):
	def __init__(self):
		super(Battleship, self).__init__(4, x, y, orientation, "Battleship")
# 5 holes
class Carrier(Boat):
		def __init__(self):
			super(Carrier, self).__init__(5, x, y, orientation, "Carrier")
	
class Grid(object):
	
	board = []
	def __init__(self, x, y):
		self.x = x
		self.y = y
		#self.board = []

	#def setBoard(self):
	for i in range(GRIDSIZE):
	#board.append(['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'])
		board.append(['O'] * GRIDSIZE)

	def drawGrid(self):
		for row in self.board:
			print " ".join(row)

	def verifyBoat(self, boat):
		orientation = randint(0,1)
		if orientation == HORIZONTAL:
			xCoord = randint(0, GRIDSIZE -1 - boat.pointDeVie)
			yCoord = randint(0, GRIDSIZE-1)
			for i in range(0, boat.pointDeVie):
				if self.board[xCoord + i][yCoord] != 'O':
					print 'On ne peut place le bateau a cet endroit'
					return False
				else:
					print 'bateau ok!!!'
					for i in range(0, boat.pointDeVie):						 
						self.board[xCoord + i][yCoord] = 'b'
						print self.board[xCoord + i][yCoord]
					return True
		#Vertical
		else:
			xCoord = randint(0, GRIDSIZE -1)
			yCoord = randint(0, GRIDSIZE-1 - boat.pointDeVie)
			for i in range(0, boat.pointDeVie):
				if self.board[xCoord][yCoord + i] != 'O':
					print 'On ne peut place le bateau a cet endroit'
					return False
				else:
					print 'bateau ok!!!'
					for i in range(0, boat.pointDeVie):
						self.board[xCoord][yCoord + i] = 'b'
						print self.board[xCoord][yCoord + i]
					return True
	
	
class Player(object):
	pass
class Game(object):
	
	def __init__(self):
		pass
	
	def stuff(self):
		print "les x:%d et les y:%d" % x,y
	
def main():
	print "\n**********Battleship***********\n"
	
	'''
	while True:
		global x
		global y
		x = raw_input("Entrez la largeur de la grille (x): ")
		y = raw_input("Entrez la hauteur de la grille (y): ")
		resultatX = x.isdigit()
		resultatY = y.isdigit()
		if resultatX and resultatY:
			x = int(x)
			y = int(y)
			if x >0 and x <=20 and y > 0 and y <=20:
				break
			else:
				print ("Vous devez entrer des valeurs entre 1 et 20!")
	'''
	grid = Grid(GRIDSIZE, GRIDSIZE)
	
	grid.drawGrid()

	destroyer = Destroyer(2,2,VERTICAL)
	submarine = Submarine(2,2,VERTICAL)
	cruiser = Cruiser(2,2,VERTICAL)
	battleship = Battleship(2,3, VERTICAL)
	carrier = Carrier(2,3, VERTICAL)
	
	grid.verifyBoat(destroyer)
	for n in range(0,10):
		grid.verifyBoat(Destroyer(2,2,VERTICAL))

	grid.drawGrid()


	print "random x y: " , randint(1,10) ## random.randrange(1, 10)

	#guess_row = int(raw_input("Guess Row: "))
	#guess_col = int(raw_input("Guess Col: "))
	
	''' Number of boat selection
	while True:
		nbBateaux = raw_input("Combien de bateaux voulez vous?")
		resultat = nbBateaux.isdigit()
		if resultat:
			nbBateaux = int(nbBateaux)
			if nbBateaux >1 and nbBateaux < 6: 
				break
			else:
				print "Vous devez choisir un chiffre entre 2 et 5"
		else:
			print "Svp entrez un numéro entre 2 et 5!"
	#Game.stuff()	
	'''

if __name__ == "__main__":
	main()
		
			
