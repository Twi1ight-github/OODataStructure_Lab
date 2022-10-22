'''
จักกับ Binary Search Tree
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return self.root
        else:
            cur = self.root
            while True:
                if node.data < cur.data:
                    if cur.left is None:
                        cur.left = node
                        return self.root
                    else:
                        cur = cur.left

                else:
                    if cur.right is None:
                        cur.right = node
                        return self.root
                    else:
                        cur = cur.right

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
