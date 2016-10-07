### This serves as the base script for solving the Traffic Puzzle problem. 
### Karan Tibrewal, Williams College
### (c) 2016
### karan.tibrewal@williams.edu


## This class describes a Vehicle
class Vehicle:
	def isRedCar(self): return self.carName == "**" 
	def getLocation(self): return None
	def __init__(self): return None

## This class describes a Car
class Car(Vehicle):

	# @param loc1 1st coordinate of car 
	# @param loc2 2nd coordinate of car
	# @param carName name of truck
	def __init__(self, loc1, loc2, carName):
		self.loc1 = loc1
		self.loc2 = loc2
		self.carName = carName
		self.rowWise = self.loc1[0] == self.loc2[0] # is the car oriented row-wise?

	# @return a list of locations of the car
	def getLocation(self): 
		return [self.loc1, self.loc2]

## This class describes a Truck
class Truck(Vehicle):

	# @param loc1 1st coordinate of truck
	# @param loc2 2nd coordinate of truck
 	# @param loc3 3rd coordinate of truck
 	# @param carName name of truck
	def __init__(self, loc1, loc2, loc3, carName):
		self.loc1 = loc1
		self.loc2 = loc2
		self.loc3 = loc3
		self.carName = carName
		self.rowWise = self.loc1[0] == self.loc2[0]  and \
					   self.loc2[0] == self.loc[3]# is the car oriented row-wise?

	# @return a list of locations of the car
	def getLocation(self): 
		return [self.loc1, self.loc2, self.loc3]

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



## REMOVE 
## TESTING TRAFFIC PUZZLE 
# TrafficBoard.n = 4
# TrafficBoard.numCars = 0
# board = [[0 for x in range(4)] for y in range(4)]
# board = TrafficBoard(board)
# print board

## Function to recieve board lay out for the initial state
## @return a TrafficBoard representing the initial state
def stdInputInitState(): 
	TrafficBoard.n = input("What are the board dimensions(n x n)? ")
	r = input("Enter row coordinate for end gate: ")
	c = input("Enter column coordinate for end gate:")
	TrafficBoard.endGate = (r,c)
	TrafficBoard.numCars = input("How many cars? (excluding SPECIAL car)")
	TrafficBoard.numTrucks = input("How many trucks?")
	cars = []
	trucks = []
	carName = 'A'

	for i in range(TrafficBoard.numCars): 
		r1 = input("Enter #1 row coordinate for (front) car #" + str(i) + " :")
		c1 = input("Enter #1 column coordinate for (front) car #" + str(i) + " :")
		r2 = input("Enter #2 row coordinate for (front) car #" + str(i) + " :")
		c2 = input("Enter #2 column coordinate for (front) car #" + str(i) + " :")
		cars.append(Car((r1,c1), (r2, c2), carName))
		carName = chr(ord(carName)+1)


	for i in range(TrafficBoard.numTrucks): 
		r1 = input("Enter #1 row coordinate for (front) truck #" + str(i) + " :")
		c1 = input("Enter #1 column coordinate for (front) truck #" + str(i) + " :")
		r2 = input("Enter #2 row coordinate for (front) truck #" + str(i) + " :")
		c2 = input("Enter #2 column coordinate for (front) truck #" + str(i) + " :")
		r3 = input("Enter #3 row coordinate for (front) truck #" + str(i) + " :")
		c3 = input("Enter #3 column coordinate for (front) truck #" + str(i) + " :")
		trucks.append(Truck((r1,c1), (r2, c2), (r3, c3), carName))
		carName = chr(ord(carName)+1)

	r1 = input("Enter #1 row coordinate for RED car #" + str(i) + " :")
	c1 = input("Enter #1 column coordinate for RED car #" + str(i) + " :")
	r2 = input("Enter #2 row coordinate for (front) RED #" + str(i) + " :")
	c2 = input("Enter #2 column coordinate for (front) RED #" + str(i) + " :")
	car.append(Car((r1,c1), (r2, c2), "**"))

	board = TrafficBoard.createEmptyMatrix(TrafficBoard.n);
	for car in cars: 
		for loc in car.getLocation():
			board[loc[0]][loc[1]] = car.carName
		carName = chr(ord(carName)+1)
	for truck in trucks: 
		for loc in truck.getLocation():
			board[loc[0]][loc[1]] = truck.carName

	return TrafficBoard(board, cars, trucks)

## Function to read in board lay out for the initial state
## @param file to read from
## @return a TrafficBoard representing the initial state
def FileInputInitState(filename): 
	file = open(filename, 'r')

	TrafficBoard.n = int(file.readline())
	r = int(file.readline())	
	c = int(file.readline())
	TrafficBoard.endGate = (r,c)
	TrafficBoard.numCars = int(file.readline())
	TrafficBoard.numTrucks = int(file.readline())
	cars = []
	trucks = []
	carName = 'A'

	for i in range(TrafficBoard.numCars): 
		r1 = int(file.readline())
		c1 = int(file.readline())
		r2 = int(file.readline())
		c2 = int(file.readline())
		cars.append(Car((r1,c1), (r2, c2), carName))
		carName = chr(ord(carName)+1)


	for i in range(TrafficBoard.numTrucks): 
		r1 = int(file.readline())
		c1 = int(file.readline())
		r2 = int(file.readline())
		c2 = int(file.readline())
		r3 = int(file.readline())
		c3 = int(file.readline())
		trucks.append(Truck((r1,c1), (r2, c2), (r3, c3), carName))
		carName = chr(ord(carName)+1)

	r1 = int(file.readline())
	c1 = int(file.readline())
	r2 = int(file.readline())
	c2 = int(file.readline())
	cars.append(Car((r1,c1), (r2, c2), "**"))

	board = TrafficBoard.createEmptyMatrix(TrafficBoard.n);
	for car in cars: 
		for loc in car.getLocation():
			board[loc[0]][loc[1]] = car.carName
		carName = chr(ord(carName)+1)
	for truck in trucks: 
		for loc in truck.getLocation():
			board[loc[0]][loc[1]] = truck.carName

	return TrafficBoard(board, cars, trucks)



print FileInputInitState("initTest")





