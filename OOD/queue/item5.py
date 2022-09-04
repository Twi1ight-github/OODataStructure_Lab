class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
    def display(self):
        return self.items

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def popIndex(self, index):
        return self.items.pop(index)
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items

def main():
    mirror_bomb = Queue()
    mirror = Stack()
    real = Stack()

    inReal,inMirror = input('Enter Input (Normal, Mirror) : ').split(' ')

    #push input to stack
    for i in range(len(inMirror)):
        mirror.push(inMirror[i])

    for i in range(len(inReal)):
        real.push(inReal[i])

    #In Mirror
    mirror_combo = 0
    count = mirror.size() - 1
    while count >= 0:
        if count >=2:
            if mirror.items[count] == mirror.items[count-1] and mirror.items[count-1] == mirror.items[count-2]:
                mirror_combo +=1
                mirror_bomb.enqueue(mirror.items[count])
                
                for delt in range(3):
                    mirror.popIndex(count-delt)

                count = mirror.size() - 1
                continue
            else:
                count -= 1
        else:
            count-=1

    #In Real
    real_combo = 0
    fail =0
    count = 0
    while count < real.size():
        if count < real.size()-2:
            if real.items[count] == real.items[count+1] and real.items[count+1] == real.items[count+2]:
                if not mirror_bomb.isEmpty():
                    real.items.insert(count+2,mirror_bomb.dequeue())
                    if real.items[count] == real.items[count+1] and real.items[count+1] == real.items[count+2]:
                        fail+=1
                        for _ in range(3):
                            real.popIndex(count)
                        count = 0
                        continue
                else:
                    if real.items[count] == real.items[count+1] and real.items[count+1] == real.items[count+2]:
                        real_combo+=1
                        for _ in range(3):
                            real.popIndex(count)
                        count = 0
                        continue

        count+=1
        
    print('NORMAL : ')
    print(real.size())
    if real.isEmpty():
        print('Empty')
    else:
        for x in reversed(real.items):
            print(x,end='')
        print()
    print('{} Explosive(s) ! ! ! (NORMAL)'.format(real_combo))

    if fail == 0:
        pass
    else:
        print('Failed Interrupted {} Bomb(s)'.format(fail))

    print('------------MIRROR------------')

    print(': RORRIM')
    print(mirror.size())
    if mirror.isEmpty():
        print('ytpmE')
    else:
        for x in mirror.items:
            print(x,end='')
        print()
    print('(RORRIM) ! ! ! (s)evisolpxE {}'.format(mirror_combo))
            
        
  
    
if __name__ == '__main__':
    main()





