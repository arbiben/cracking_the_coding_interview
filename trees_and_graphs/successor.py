# find the next "in order" node given a current node in a bst
# each node has a link to its parent 
from Node import Node
from create_tree import random_tree

def successor(node):
    if not node:
        return None
    if node.right:
        return get_most_left(node.right)
    return successor_helper(node, node.parent)

def get_most_left(node):
    if node.left:
        return get_most_left(node.left)
    else:
        return node

def successor_helper(child, parent):
    if not parent:
        return None
    if parent.left is child:
        return parent
    return successor_helper(parent, parent.parent)


# tester - generate a bst and create test cases
t = random_tree()
tree = t.balanced
two = tree.left.right
three = two.right
five = tree.right.left
six = five.right
nine = tree.right.right.right

print("Successor of 2 should be 3: {}".format(successor(two).val))
print("Successor of 3 should be 4: {}".format(successor(three).val))
print("Successor of 4 should be 5: {}".format(successor(tree).val))
print("Successor of 5 should be 6: {}".format(successor(five).val))
print("Successor of 6 should be 7: {}".format(successor(six).val))
print("Successor of 9 should be None: {}".format(successor(nine)))
