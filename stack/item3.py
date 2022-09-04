class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()
    def pop(self, index):
        return self.items.pop(index)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


inp = input('Enter Input : ').split()

S = Stack()
# push to stack
for i in inp:
    if i >= 'A' and i <= 'Z' and len(i) == 1:
        S.push(i)
    else:
        exit()

# count same items in stack

i = 0
combo = 0
while i < S.size():

    if i < S.size()-1:
        if S.items[i] == S.items[i+1] and S.items[i+1] == S.items[i+2]:
            combo +=1
            # delete same items in stack
            S.pop(i)            
            S.pop(i)
            S.pop(i)

            # reset i
            i = 0 
            continue
    i += 1


S.items.reverse()
# display
print(S.size())
for i in S.items:
    print(i, end='')
if S.isEmpty():
   print('Empty')
else:
   print()
if combo >= 2:
     print('Combo : {} ! ! !'.format(combo))

