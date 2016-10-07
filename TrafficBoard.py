### Karan Tibrewal, Williams College
### (c) 2016
### karan.tibrewal@williams.edu


## This class represents a board, describing the number of positions, cars
## and their positions. 
class TrafficBoard: 
	# number of rows/columns
	n = 0

	# number of cars
	numCars = 0

	# number of trucks
	numTrucks = 0
	# coordinates of end gate
	endGate = (0,0)

	# CONSTRUCTOR
	# @param boardConfig the initial board condiguration for this TrafficBoard
	def __init__(self, boardConfig, cars, trucks):
		self.board = boardConfig
		self.vehicles = cars + trucks

	# returns string representation of the board
	def __str__(self):
		string = '\n'.join(['\t'.join(x) for x in [[str(a) for a in b] for b in self.board]])		
		return string

	# creates an empty board of all zeros
	# @param n dimension of square board
	# @return empty board (all zeros)
	@staticmethod
	def createEmptyMatrix(n):

		return [[0 for x in range(n)] for y in range(n)]