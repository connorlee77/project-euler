class Node:

	leftParent = None
	rightParent = None
	value = 0
	
	def __init__(self, leftParent, rightParent, value):
		if leftParent is not None:
			self.leftParent = leftParent
		if rightParent is not None:
			self.rightParent = rightParent
		self.value = value

	def getLeftParent(self):
		return self.leftParent

	def getRightParent(self):
		return self.rightParent
	
	def getValue(self):
		return self.value
	
	def setValue(self, val):
		self.value = val
		return True



def getData():
	import sys

	oldNodes = []
	for line in sys.stdin:
		newNodes = []	
		line = line.strip().split()

		if len(oldNodes) == 0:
			currNode = Node(None, None, int(line[0]))
			newNodes.append(currNode)
		else:

			for i, val in enumerate(line):

				if val[0] == '0':
					val = val[1]

				if i == 0:
					currNode = Node(None, oldNodes[0], int(val))
				elif i == len(line) - 1:
					currNode = Node(oldNodes.pop(0), None, int(val))
				else:
					currNode = Node(oldNodes.pop(0), oldNodes[0], int(val))
				newNodes.append(currNode)
		oldNodes = newNodes

	return oldNodes

def traverse(nodes):
	for node in nodes:
		print node.getValue()

		if node.getLeftParent() != None:
			print node.getLeftParent().getValue()
		else:
			print node.getLeftParent()

		if node.getRightParent() != None:
			print node.getRightParent().getValue()
		else:
			print node.getRightParent()
		print


def findMaxPath(data):

	if len(data) == 1:
		return data[0].getValue()

	nodes = []
	for i in range(len(data) - 1):
		left = data[i]
		right = data[i + 1]

		currVal = left.getRightParent().getValue()
		left.getRightParent().setValue(currVal + max(right.getValue(), left.getValue()))
		nodes.append(left.getRightParent())
	return findMaxPath(nodes)

nodes = getData()
print findMaxPath(nodes)






