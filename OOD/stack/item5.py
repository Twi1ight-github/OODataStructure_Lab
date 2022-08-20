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


blue = Stack()
red = Stack()
def main():
    
    print("******** Parking Lot ********")

    #input
    m,s,o,n = input("Enter max of car,car in soi,operation : ").split()

    #clean input
    s=s.split(',')
    s = [int(i) for i in s]
    if s == [0]:
        s = []

    m,n = int(m),int(n)

    
    # add car in soi
    for car_id in s:
        if blue.size() < m:
            blue.push(car_id)
        else:
            print('car {} cannot arrive : Soi Full'.format(car_id))

    # operation
    if o == 'arrive':
        if n in blue.items:
            print('car {} already in soi'.format(n))
        else:
            if blue.size() < m:
                blue.push(n)
                print('car {} arrive! : Add Car {}'.format(n,n))
            else:
                print('car {} cannot arrive : Soi Full'.format(n))
    elif o == 'depart':
        if blue.isEmpty():
            print('car {} cannot depart : Soi Empty'.format(n))

        else:
            if n in blue.items:
                while True:
                    if blue.peek() == n:
                        blue.pop()
                        print('car {} depart ! : Car {} was remove'.format(n,n))
                        break
                    else :
                        red.push(blue.pop())
            else:
                print('car {} cannot depart : Dont Have Car {}'.format(n,n))

            
    # push car back to blue soi
    while not red.isEmpty():
        blue.push(red.pop())
        
    # print result    
    print(blue.items)

if __name__ == '__main__':
    main()
