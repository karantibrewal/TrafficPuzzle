## HEURISTIC FUNCTION
## @param board a TrafficBoard object with the current state of the board
## @return h(n) = number of cars between the red car and the end gate
def h1(board):
	redCar = board.vehicles["**"]
	locations = []
	endGate = board.endGate
	matrix = board.board
	count = 0
	if redCar.rowWise: 
		row = endGate[0]
		if endGate[1] == 0: 
			i = 0
			while(matrix[row][i] != "**"):
				count += 1 if matrix[row][i] != 0 else 0
				i += 1
		else:
			i = board.n - 1
			while(matrix[row][i] != "**"):
				count += 1 if matrix[row][i] != 0 else 0
				i -= 1
	else: 
		column = endGate[1]
		if endGate[0] == 0:
			i = 0 
			while(matrix[i][column] != "**"):
				count += 1 if matrix[i][column] != 0 else 0
				i += 1
		else:
			i = board.n - 1
			while(matrix[i][column] != "**"):
				count += 1 if matrix[i][column] != 0 else 0
				i -= 1
	return count


from Input import FileInputInitState
# Test 1
board1 =  FileInputInitState("initTest")
assert h1(board1) == 4

# Test 2
board2 =  FileInputInitState("initTest2")
assert h1(board2) == 2

# Test 3
board3 =  FileInputInitState("initTest3")
assert h1(board3) == 3
