# coding=utf-8

class Battleship(object):
	pass
class Boat(object):
	pass
class Destroyer(Boat):
	pass
class Submarine(Boat):
	pass
class Carrier(Boat):
	pass
class Cruiser(Boat):
	pass
	
class Grid(object):
		
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def drawGrid(self):
		for j in range (0, self.y):
			for i in range(0, self.x):
				print '-',
			print "\n"
class Player(object):
	pass
class Game(object):
	
	def __init__(self):
		pass
	
	def stuff(self):
		print "les x:%d et les y:%d" % x,y
	
	def main():
		print "\n********Hello Battleship***********\n"
		
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
		
		grid = Grid(x,y)
		
		grid.drawGrid()
		
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
		Game.stuff()	
	
	if __name__ == "__main__":
		main()
		
			
