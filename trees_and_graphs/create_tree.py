from Node import Node
import random

class random_tree:
    def __init__(self, size):
        new_list = [i for i in range(size)]
        with_neg = []
        for i in range(size):
            if random.randint(0,1):
                with_neg.append(i * -1)
            else:
                with_neg.append(i)
        self.negative = self.list_to_tree(with_neg)
        self.balanced = self.list_to_tree(new_list)
        self.unbal = self.unbalanced_tree_generator()

    def list_to_tree(self, l):
        return self.to_tree_helper(l, 0, len(l)-1)


    def to_tree_helper(self, sorted_list, l, r):
        if l > r:
            return None
        mid = int((l+r)/2)
        node = Node(sorted_list[mid])
        node.left = self.to_tree_helper(sorted_list, l, mid-1)
        node.right = self.to_tree_helper(sorted_list, mid+1, r)
        
        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node

        return node
    
    def unbalanced_tree_generator(self):
        root = Node(1)
        node = root
        for _ in range(random.randint(5, 10)):
            left = Node(random.randint(0, 100))
            right = Node(random.randint(0, 100))
            left.parent = right.parent = node
            node.left = left
            node.right = right
            i = random.randint(0,1)
            if i:
                node = node.left
            else:
                node = node.right
        
        return root

    def list_of_depth(self, root):
        return self.list_of_depth_helper(root, 0, [])


    def list_of_depth_helper(self, root, d, list_of_lists):
        if not root:
            return None

        if len(list_of_lists) == d:
            list_of_lists.append([root.val])
        else:
            list_of_lists[d].append(root.val)

        self.list_of_depth_helper(root.left, d+1, list_of_lists)
        self.list_of_depth_helper(root.right, d+1, list_of_lists)

        return list_of_lists
            
