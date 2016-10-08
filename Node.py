### Karan Tibrewal, Williams College
### (c) 2016
### karan.tibrewal@williams.edu

from Actions import MoveRightBy
from Actions import MoveLeftBy
from Actions import MoveUpBy
from Actions import MoveDownBy
import copy

## @return deep copy of this 2d list
def copyThis(arr): 
	l = []
	for a in arr: 
		l.append(copy.copy(a))
	return l

## This class represents a node in the search space. 
## It contains informations about:
## board representation of this state
## its parent
## action used to generate it
## its heuristic calculation
class Node: 
	# @param board TrafficBoard object for this state
	# @param parent the parent of this node
	# @param action action used on parent to generate this node
	# @param g path cost
	# @param heuristic function
	def __init__(self, board, parent, action, g, h):
		self.board = board
		self.parent = parent
		self.action = action 
		self.pathCost = g 
		self.f = g + h(board)

	## Gets list of possible actions
	## @return a list of possible actions
	def getPossibleActions(self):
		actions = []
		for v in self.board.vehicles:
			vehicle = self.board.vehicles[v]
			for i in range(1,6):
				matrix = copyThis(self.board.board)
				if MoveRightBy.isPossible(i, copyThis(self.board.board), copy.copy(vehicle)):
					actions.append(MoveRightBy(i, copyThis(self.board.board), copy.copy(vehicle)))
				if MoveLeftBy.isPossible(i, copyThis(self.board.board), copy.copy(vehicle)):
					actions.append(MoveLeftBy(i, copyThis(self.board.board), copy.copy(vehicle)))
				if MoveUpBy.isPossible(i, copyThis(self.board.board), copy.copy(vehicle)):
					actions.append(MoveUpBy(i, copyThis(self.board.board), copy.copy(vehicle)))
				if MoveDownBy.isPossible(i, copyThis(self.board.board), copy.copy(vehicle)):
					actions.append(MoveDownBy(i, copyThis(self.board.board), copy.copy(vehicle)))
		return actions

	# implements a comparator for nodes
	def __cmp__(self, other):
		if self.pathCost < other.pathCost:
			return -1
		else:
			return 1


from Input import FileInputInitState
# Test 1
board1 =  FileInputInitState("initTest")
print board1

