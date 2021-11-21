import random
import time
# A Huffman Tree Node
class node:
	def __init__(self, freq, symbol, left=None, right=None):
		# frequency of symbol
		self.freq = freq

		# symbol name (character)
		self.symbol = symbol

		# node left of current node
		self.left = left

		# node right of current node
		self.right = right

		# tree direction (0/1)
		self.huff = ''

# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree


def printNodes(node, val=''):
	# huffman code for current node
	newVal = val + str(node.huff)

	# if node is not an edge node
	# then traverse inside it
	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

		# if node is edge node then
		# display its huffman code
	if(not node.left and not node.right):
		dictionary_to[node.symbol] = str(newVal)
		dictionary_from[str(newVal)] = node.symbol
		print(f"{node.symbol} -> {newVal}")


# characters for huffman tree
chars = list(set("йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,.! "))

# frequency of characters
random.seed(time.time())
freq = [random.randint(0, 1000) for _ in range(len("йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,.! "))]

# list containing unused nodes
nodes = []
dictionary_to = {}
dictionary_from = {}
# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
	nodes.append(node(freq[x], chars[x]))

while len(nodes) > 1:
	# sort all the nodes in ascending order
	# based on theri frequency
	nodes = sorted(nodes, key=lambda x: x.freq)

	# pick 2 smallest nodes
	left = nodes[0]
	right = nodes[1]

	# assign directional value to these nodes
	left.huff = 0
	right.huff = 1

	# combine the 2 smallest nodes to create
	# new node as their parent
	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

	# remove the 2 nodes and add their
	# parent as new node among others
	nodes.remove(left)
	nodes.remove(right)
	nodes.append(newNode)

# Huffman Tree is ready!
printNodes(nodes[0])

s = "Здравствуйте Денис Сергеевич! Могу вас заверить, что новый год буду встречать в маске и перчатках."
encoded = ""
for i in s:
	encoded+=dictionary_to[i]
tmp = ""
decoded = ""
for i in encoded:
	tmp+=i
	if tmp in dictionary_from:
		decoded+=dictionary_from[tmp]
		tmp = ""
print(encoded.replace("0", "Денис").replace("1", "Сергеевич"))

# 128!/(128-69)! ~ 3 * 1e135