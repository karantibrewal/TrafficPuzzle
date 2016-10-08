### Karan Tibrewal, Williams College
### (c) 2016
### karan.tibrewal@williams.edu

from Heuristics import h1
from Queue import PriorityQueue
from copy import copy
from Vehicles import Car
from Vehicles import Truck
from TrafficBoard import TrafficBoard

class BestFirstSearch: 
	## CONSTRUCTOR
	## @param init initial state
	## @param h heuristic to use
	def __init__(self, init, h):
		self.init = init
		self.h = h
		self.visitedNodes = set()
		self.totalCount = 0

	# GOAL TEST
	# @return is the given board config a win? 
	@staticmethod
	def isGoal(self, board, endGate): 
		self.totalCount += 1
		return board[endGate[0]][endGate[1]] == "**"

	## Function to execute a best first search
	## @return end node if solution is found, else false
	def execute(self):
		totalCount = 0
		visitedNodes = set()
		q = PriorityQueue()
		q.put(self.init)
		while not q.empty(): 
			thisNode = q.get()
			possibleActions = thisNode.getPossibleActions()
			thisBoard = thisNode.board
			thisVehicles = thisBoard.vehicles
			for action in possibleActions:
				matrix, locations = action.execute()
				if not isVisited(matrix, visitedNodes):			
					newVehicles = copy(thisVehicles)
					if len(locations) == 2:
						newVehicles[action.car.carName] = Car(locations[0], \
															  locations[1], \
															  action.car.carName)
					else: 
						newVehicles[action.car.carName] = Truck(locations[0], \
															    locations[1], \
															    locations[2], \
															  action.car.carName)
					newBoard = TrafficBoard(matrix, newVehicles)
					newNode = Node(newBoard, thisNode, action, thisNode.pathCost + 1, self.h)
					if action.car.carName == "**" and \
					self.isGoal(self,matrix, thisBoard.endGate): # goal can only be reached
																 # when the red car is moved.

						return newNode
					q.put(newNode)
					addVisitedNode(newNode, visitedNodes)
				
					

		return False

# Adds the node to the set of visited nodes
# @return void
def addVisitedNode(node, visitedNodes):
	visitedNodes.add(tuple([tuple(x) for x in node.board.board]))

# @return has the given node been visited? 
def isVisited(board, visitedNodes): 
	return tuple([tuple(x) for x in board]) in visitedNodes


from Input import FileInputInitState
from Heuristics import h1
from Node import Node
# Test 1
board1 =  FileInputInitState("test3")
node = Node(board1, None, None, 0, h1)
search = BestFirstSearch(node, h1)
print "************"
print board1
node = search.execute()
while (not node.parent is None):
	print node.action
	node = node.parent

print search.totalCount
