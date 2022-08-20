class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []

    def clear(self):
        self.items.clear()


S = Stack()
T = Stack()

inp = input('Enter Input : ').split(',')

for index in range(len(inp)):

    tree_meter = inp[index][2:]
    key = inp[index][0]

    if key == 'A':
        S.push(tree_meter)
           
    elif key == 'B':
        if not S.isEmpty():
            T.push(S.peek())
              
        for count_tree in range(len(S.items)-1,-1,-1):         
            backTree = T.peek()
            
            if int(backTree) < int(S.items[count_tree]):
                if not S.isEmpty():
                    T.push(S.items[count_tree])
                       
        print(T.size())
        T.clear()