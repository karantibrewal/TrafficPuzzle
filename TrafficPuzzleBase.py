### This serves as the base script for solving the Traffic Puzzle problem. 
### Karan Tibrewal, Williams College
### (c) 2016
### karan.tibrewal@williams.edu





## This class represents a node in the search space. 
## It contains informations about:
## board representation of this state
## its parent
## action used to generate it
## its heuristic calculation
class Node: 
	def __init__(self, board, parent, action, pathCost):
		self.board = board
		self.parent = parent
		self.action = action 
		self.pathCost = pathCost ## ????

	## Gets list of possible actions
	## @return a list of possible actions 
	def getPossibleActions(self):
		return []


		












print FileInputInitState("initTest")






