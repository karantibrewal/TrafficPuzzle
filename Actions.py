### Karan Tibrewal, Williams College
### (c) 2016
### karan.tibrewal@williams.edu


from Vehicles import Car
from Vehicles import Truck
## This class represents the action of moving the given car one square to the
## right
class MoveRight:
	# CONSTRUCTIOR
	# @param board board configuration
	# @param car car to be moved
	def __init__(self, board, car):
		self.board = board
		self.car = car

	# Executes the action, returning resulting board config
	# @return tuple of resulting board config, new location of cars
	def execute(self):
		assert self.isPossible(self.board, self.car)
		board = self.board
		position = self.car.getLocation()
		newLocations = []
		for loc in position:
			board[loc[0]][loc[1]] = 0
			newLocations.append((loc[0], loc[1]+1))
		for loc in newLocations:
			board[loc[0]][loc[1]] = self.car.carName
		return (board, newLocations)

	# @return is this action legal?
	@staticmethod
	def isPossible(board, car):
		if not car.rowWise:
			return False
		position = car.getLocation()
		for loc in position:
			if loc[1]+1 >= len(board) or \
			   (board[loc[0]][loc[1]+1] != car.carName and \
			   board[loc[0]][loc[1]+1] != 0) :
			   return False
		return True

# Test 1
board = [[0 for _ in range(4)] for _ in range(4)]
board[0][0] = "A"
board[1][0] = "A"
assert MoveRight.isPossible(board, Car((0,0), (1,0), "A")) == False

# Test 2
board = [[0 for _ in range(4)] for _ in range(4)]
board[0][0] = "A"
board[0][1] = "A"
assert MoveRight.isPossible(board, Car((0,0), (0,1), "A")) == True
result = MoveRight(board, Car((0,0), (0,1), "A")).execute()
board2 = [[0 for _ in range(4)] for _ in range(4)]
board2[0][1] = "A"
board2[0][2] = "A"
assert result[0] == board2
assert result[1] == [(0,1), (0,2)]

# Test 3
board = [[0 for _ in range(4)] for _ in range(4)]
board[0][2] = "A"
board[0][3] = "A"
assert MoveRight.isPossible(board, Car((0,2), (1,3), "A")) == False

# Test 4
board = [[0 for _ in range(5)] for _ in range(5)]
board[0][0] = "A"
board[0][1] = "A"
board[0][2] = "B"
board[0][3] = "B"
assert MoveRight.isPossible(board, Car((0,0), (0,1), "A")) == False
assert MoveRight.isPossible(board, Car((0,2), (0,3), "B")) == True

# Test 5
board = [[0 for _ in range(5)] for _ in range(5)]
board[0][0] = "A"
board[0][1] = "A"
board[0][2] = "A"
assert MoveRight.isPossible(board, Truck((0,0), (0,1), (0,2), "A")) == True


## This class represents the action of moving the given car one square to the
## left
class MoveLeft:
	# CONSTRUCTIOR
	# @param board board configuration
	# @param car car to be moved
	def __init__(self, board, car):
		self.board = board
		self.car = car

	# Executes the action, returning resulting board config
	# @return tuple of resulting board config, new location of cars
	def execute(self):
		assert self.isPossible(self.board, self.car)
		board = self.board
		position = self.car.getLocation()
		newLocations = []
		for loc in position:
			board[loc[0]][loc[1]] = 0
			newLocations.append((loc[0], loc[1]-1))
		for loc in newLocations:
			board[loc[0]][loc[1]] = self.car.carName
		return (board, newLocations)

	# @return is this action legal?
	@staticmethod
	def isPossible(board, car):
		if not car.rowWise:
			return False
		position = car.getLocation()
		for loc in position:
			if loc[1]-1 < 0 or \
			   (board[loc[0]][loc[1]-1] != car.carName and \
			   board[loc[0]][loc[1]-1] != 0) :
			   return False
		return True

# Test 1
board = [[0 for _ in range(4)] for _ in range(4)]
board[0][0] = "A"
board[1][0] = "A"
assert MoveLeft.isPossible(board, Car((0,0), (1,0), "A")) == False

# Test 2
board = [[0 for _ in range(4)] for _ in range(4)]
board[0][0] = "A"
board[0][1] = "A"
assert MoveLeft.isPossible(board, Car((0,0), (0,1), "A")) == False


# Test 3
board = [[0 for _ in range(4)] for _ in range(4)]
board[0][2] = "A"
board[0][3] = "A"
assert MoveLeft.isPossible(board, Car((0,2), (0,3), "A")) == True
result = MoveLeft(board, Car((0,2), (0,3), "A")).execute()
board2 = [[0 for _ in range(4)] for _ in range(4)]
board2[0][1] = "A"
board2[0][2] = "A"
assert result[0] == board2
assert result[1] == [(0,1), (0,2)]

# Test 4
board = [[0 for _ in range(5)] for _ in range(5)]
board[0][0] = "A"
board[0][1] = "A"
board[0][2] = "B"
board[0][3] = "B"
assert MoveLeft.isPossible(board, Car((0,0), (0,1), "A")) == False
assert MoveLeft.isPossible(board, Car((0,2), (0,3), "B")) == False

# Test 5
board = [[0 for _ in range(5)] for _ in range(5)]
board[0][2] = "A"
board[0][3] = "A"
board[0][4] = "A"
assert MoveLeft.isPossible(board, Truck((0,4), (0,3), (0,2), "A")) == True


## This class represents the action of moving the given car one square to the
## up
class MoveUp:
	# CONSTRUCTIOR
	# @param board board configuration
	# @param car car to be moved
	def __init__(self, board, car):
		self.board = board
		self.car = car

	# Executes the action, returning resulting board config
	# @return tuple of resulting board config, new location of cars
	def execute(self):
		assert self.isPossible(self.board, self.car)
		board = self.board
		position = self.car.getLocation()
		newLocations = []
		for loc in position:
			board[loc[0]][loc[1]] = 0
			newLocations.append((loc[0]-1, loc[1]))
		for loc in newLocations:
			board[loc[0]][loc[1]] = self.car.carName
		return (board, newLocations)

	# @return is this action legal?
	@staticmethod
	def isPossible(board, car):
		if car.rowWise:
			return False
		position = car.getLocation()
		for loc in position:
			if loc[0] -1 < 0 or \
			   (board[loc[0]-1][loc[1]] != car.carName and \
			    board[loc[0]-1][loc[1]] != 0) :
			   return False
		return True

# Test 1
board = [[0 for _ in range(4)] for _ in range(4)]
board[0][0] = "A"
board[1][0] = "A"
assert MoveUp.isPossible(board, Car((0,0), (1,0), "A")) == False

# Test 2
board = [[0 for _ in range(4)] for _ in range(4)]
board[0][0] = "A"
board[0][1] = "A"
assert MoveUp.isPossible(board, Car((0,0), (0,1), "A")) == False


# Test 3
board = [[0 for _ in range(4)] for _ in range(4)]
board[2][0] = "A"
board[3][0] = "A"
assert MoveUp.isPossible(board, Car((2,0), (3,0), "A")) == True
result = MoveUp(board, Car((2,0), (3,0), "A")).execute()
board2 = [[0 for _ in range(4)] for _ in range(4)]
board2[1][0] = "A"
board2[2][0] = "A"
assert result[0] == board2
assert result[1] == [(1,0), (2,0)]


# Test 4
board = [[0 for _ in range(5)] for _ in range(5)]
board[1][0] = "A"
board[2][0] = "A"
board[3][0] = "B"
board[4][0] = "B"
assert MoveUp.isPossible(board, Car((2,0), (1,0), "A")) == True
assert MoveUp.isPossible(board, Car((3,0), (4,0), "B")) == False

## This class represents the action of moving the given car one square to the
## bottom
class MoveDown:
	# CONSTRUCTIOR
	# @param board board configuration
	# @param car car to be moved
	def __init__(self, board, car):
		self.board = board
		self.car = car

	# Executes the action, returning resulting board config
	# @return tuple of resulting board config, new location of cars
	def execute(self):
		assert self.isPossible(self.board, self.car)
		board = self.board
		position = self.car.getLocation()
		newLocations = []
		for loc in position:
			board[loc[0]][loc[1]] = 0
			newLocations.append((loc[0]+1, loc[1]))
		for loc in newLocations:
			board[loc[0]][loc[1]] = self.car.carName
		return (board, newLocations)

	# @return is this action legal?
	@staticmethod
	def isPossible(board, car):
		if car.rowWise:
			return False
		position = car.getLocation()
		for loc in position:
			if loc[0] + 1 >= len(board) or \
			   (board[loc[0]+1][loc[1]] != car.carName and \
			    board[loc[0]+1][loc[1]] != 0) :
			   return False
		return True

# Test 1
board = [[0 for _ in range(4)] for _ in range(4)]
board[0][0] = "A"
board[1][0] = "A"
assert MoveDown.isPossible(board, Car((0,0), (1,0), "A")) == True
result = MoveDown(board, Car((0,0), (1,0), "A")).execute()
board2 = [[0 for _ in range(4)] for _ in range(4)]
board2[1][0] = "A"
board2[2][0] = "A"
assert result[0] == board2
assert result[1] == [(1,0), (2,0)]


# Test 2
board = [[0 for _ in range(4)] for _ in range(4)]
board[0][0] = "A"
board[0][1] = "A"
assert MoveDown.isPossible(board, Car((0,0), (0,1), "A")) == False


# Test 3
board = [[0 for _ in range(4)] for _ in range(4)]
board[2][0] = "A"
board[3][0] = "A"
assert MoveDown.isPossible(board, Car((2,0), (3,0), "A")) == False


# Test 4
board = [[0 for _ in range(5)] for _ in range(5)]
board[0][0] = "A"
board[1][0] = "A"
board[2][0] = "B"
board[3][0] = "B"
assert MoveDown.isPossible(board, Car((1,0), (0,0), "A")) == False
assert MoveDown.isPossible(board, Car((3,0), (2,0), "B")) == True
