### Karan Tibrewal, Williams College
### (c) 2016
### karan.tibrewal@williams.edu

from TrafficBoard import TrafficBoard
from Vehicles import Car
from Vehicles import Truck

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

