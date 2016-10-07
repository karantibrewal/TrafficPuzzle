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

#### CAN THIS BE MADE BETTER ??? 
#### Instead of keeping a set of visited nodes, let us keep a map of 
#### visitedNode => (minCost to get to node, ref to node min cost)
#### This way, if we find a smaller path, we can use that instead?? even if it
#### is after finding path to end?? 

		
visitedNodes = set()
# Adds the node to the set of visited nodes
# @return void
def addVisitedNode(node):
	visitedNodes.add(tuple([tuple(x) for x in node.board]))

# @return has the given node been visited? 
def isVisited(node): 
	return tuple([tuple(x) for x in node.board]) in visitedNodes


# GOAL TEST
# @return is the given board config a win? 
def isGoal(board, endGate): 
	return board[endGate[0]][endGate[1]] == "**"

























