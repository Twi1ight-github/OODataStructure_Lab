'''
ส่วนไหน
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

    def checkpos(self,r: Node,check,parent):
        if r:
            if r.data == check:
                if r.right is None and r.left is None:
                    return 'Leaf'
                elif parent == None:
                    return 'Root'
                else:
                    return 'Inner'
            else:
                if int(check) < int(r.data):
                    return self.checkpos(r.left,check,r.data)
                else:
                    return self.checkpos(r.right,check,r.data)
        return 'Not exist'

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
ins = inp[1:]
check = inp[0]
for i in ins:
    root = T.insert(i)
T.printTree(root)
print(T.checkpos(T.root,check,None))
