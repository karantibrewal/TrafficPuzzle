### This serves as the base script for solving the Traffic Puzzle problem. 
### Karan Tibrewal, Williams College
### (c) 2016
### karan.tibrewal@williams.edu

from Input import FileInputInitState
from Input import stdInputInitState
from Heuristics import h1
from Heuristics import h2
from BestFirstSearch import BestFirstSearch
from Node import Node

def printPath(node): 
	if not node.parent is None:
		printPath(node.parent)
	if not node.action is None:
		print node.action



# board1 =  FileInputInitState("test1")
# node = Node(board1, None, None, 0, h1)
# search = BestFirstSearch(node, h1)
# print "************"
# print board1
# node = search.execute()
# while (not node.parent is None):
# 	print node.action
# 	node = node.parent

# print search.totalCount

print "1. Test Puzzle One"
print "2. Test Puzzle Two"
print "3. Test Puzzle Three"
print "4. Input new puzzle from keyboard"
n = int(input("Choose an option [1-4]: "))

if n == 1: 
	board = FileInputInitState("test1")
elif n == 2:
	board = FileInputInitState("test2")
elif n == 3: 
	board = FileInputInitState("test3")

print "1. Obstacles Heuristic"
print "2. Dependency Heuristic"
o = int(input("Choose an option [1-2]: "))

if o == 1: 
	h = h1
else:
	h = h2

print board
node = Node(board, None, None, 0, h)
search = BestFirstSearch(node, h)
result = search.execute()
if not result is None :
	print "Solution: "
	printPath(result)

print "Number of times Goal Test Function is called: " + str(search.totalCount)

























