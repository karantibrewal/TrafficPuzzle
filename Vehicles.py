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
					   self.loc2[0] == self.loc3[0]# is the car oriented row-wise?

	# @return a list of locations of the car
	def getLocation(self): 
		return [self.loc1, self.loc2, self.loc3]


# Test 1
s = Car((0,1), (0,2), "**")
assert s.isRedCar() == True
assert s.rowWise == True
assert s.getLocation() == [(0,1), (0,2)]


# Test 2
s = Truck((0,1), (0,2), (0,3), "T")
assert s.isRedCar() == False
assert s.rowWise == True
assert s.getLocation() == [(0,1), (0,2), (0,3)]
