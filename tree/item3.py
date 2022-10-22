'''
พ่อจ๋าอยู่ไหน
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            current = self.root

            while True:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                elif data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break
                else:
                    break


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


def father(r: Node, data, parent=None):

    if r != None:
        if int(r.data) == int(data):
            if parent == None:
                return 'None Because {} is Root'.format(data)
            return parent
        else:
            if int(data) < int(r.data):
                return father(r.left, data, r.data)
            else:
                return father(r.right, data, r.data)
    return 'Not Found Data'

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
print(father(tree.root, data[1]))
