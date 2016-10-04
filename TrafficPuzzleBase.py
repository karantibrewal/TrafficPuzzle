### This serves as the base script for solving the Traffic Puzzle problem. 
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

	# CONSTRUCTOR
	# @param boardConfig the initial board condiguration for this TrafficBoard
	def __init__(self, boardConfig):
		self.board = boardConfig

	# returns string representation of the board
	def __str__(self):
		string = '\n'.join(['\t'.join(x) for x in [[str(a) for a in b] for b in self.board]])		
		return string


## REMOVE 
## TESTING TRAFFIC PUZZLE 
# TrafficBoard.n = 4
# TrafficBoard.numCars = 0
# board = [[0 for x in range(4)] for y in range(4)]
# board = TrafficBoard(board)
# print board




