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

    def findBelow(self, lst, n):

        temp = []
        for i in lst:
            if i < n:
                temp.append(i)

        for i in range(len(temp)):
            for j in range(i + 1, len(temp)):

                if temp[i] > temp[j]:
                    temp[i], temp[j] = temp[j], temp[i]

        return temp

    def preorder(self, root, temp=[]):

        if root:
            
            temp.append(root.data)
            # Then recur on left child
            self.preorder(root.left, temp)
            # Finally recur on right child
            self.preorder(root.right, temp)

        return temp

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [i for i in input('Enter Input : ').split("|")]
inp[0] = inp[0].split()

# corvert all element to int
tree_input = [eval(i) for i in inp[0]]
n = int(inp[1])


for i in tree_input:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
preorder = T.preorder(root)
below = T.findBelow(preorder, n)

print("Below {} : ".format(n), end="")
if len(below)==0:
    print("Not have")

else:
    for i in below:
        print(i, end=' ')