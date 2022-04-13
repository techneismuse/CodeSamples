'''
Written by: Maryse Kiese
Topic: Binary Search Tree 
Year: 2022
'''

# ------------------>>  Abstract Base Class  
class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

# ------------------>>  Insert Function  
def insert(root, value):
	if root is None:
		return Node(value)
	else:
		if root.value == value:
			return root
		elif root.value < value:
			root.right = insert(root.right, value)
		else:
			root.left = insert(root.left, value)
	return root

# Insert Function Using Inorder Traverse as a Method to Insert New Nodes

def inorder(root):
	if root:
		inorder(root.left)
		print(root.value)
		inorder(root.right)

root = insert(None, 50)
insert(root, 57)
insert(root, 75)
insert(root, 39)
insert(root, 40)
insert(root, 7)
insert(root, 6)

print("The Root Value of the Binary Tree Is:")
print(root.value)

print("The Binary Tree's Vertices Are:")
inorder(root)

# ------------------>>  Binary Search Tree: Get Total Height Function 
def get_total_height(root):
    if root is None:
        return 0
    leftHeight=get_total_height(root.left)
    rightHeight=get_total_height(root.right)
    max_height= leftHeight
    if rightHeight>max_height:
        max_height = rightHeight
    return max_height+1

print("Total Height of the Binary Tree Is:")
print(get_total_height(root))


# ------------------>>  Weight Balance Factor Function
def weight_balance_factor(root):
    
    if root is None:
        return 0

    left_height = weight_balance_factor(root.left)

    if left_height == -1:
        return -1

    right_height = weight_balance_factor(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1

# ------------------>>  Printing Jobs 
print("Total Weight Factor of the Binary Tree Is:")
print(weight_balance_factor(root))

print("Total Weight Factor of Binary Tree's Right Side Is:")
print(weight_balance_factor(root.left))

print("Total Weight Factor of Binary Tree's Right Side Is:")
print(weight_balance_factor(root.right))

# ------------------>>  Serialization Function  
# Using preorder
def serialize(root, serial):
    if root != None:
        serial.append(root.value)
        serialize(root.left, serial)
        serialize(root.right, serial)
    else:
        serial.append('x')
print("The Serialized the Binary Tree Is:")
serial = []
serialize(root, serial)

print(serial)
print("The Root Value of the Serialized Binary Tree Is:")
print(root.value)

# ------------------>>  Deserialization Function  
def deserialize(serial):
    serial.reverse()
    return _deserialize(serial)

def _deserialize(serial):
    if not serial:
        return None

    node = None
    value = serial.pop()
    if value != 'n/a':
        node = Node(value)
        node.left = _deserialize(serial)
        node.right = _deserialize(serial)
    return node

root = deserialize(serial)

print("The Root Value of the Deserialized Binary Tree Is:")
print(root.value)

