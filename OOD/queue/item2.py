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

main = Queue()
c1 = Queue()
c2 = Queue()
q,minute = input("Enter people and time : ").split(" ")

max_c1,max_c2 =5,5
for i in q:
    main.enqueue(i)

count = 0
minute = int(minute)
while count < minute:
    count+=1
    if count % 2 == 0 : 
        if not c2.isEmpty():
            c2.dequeue()
      
    if (count-1) % 3 == 0 :
        if not c1.isEmpty():
            c1.dequeue()

    if c1.size() < max_c1:
        if main.isEmpty() == False:
            c1.enqueue(main.dequeue())
    
    elif c2.size() < max_c2:
        if main.isEmpty() == False:
            c2.enqueue(main.dequeue())

    print("{} {} {} {}".format(count,main.items,c1.items,c2.items))  
    

