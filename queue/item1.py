class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return int(len(self.items))

def main():
    q = Queue()
    value = input("Enter Input : ").split(",")
    

    for i in value:
        if i[0] == 'E':
            q.enqueue(i[2:])
            print("Add {} index is {} ".format(i[2:],q.size()-1))
        elif i[0] == 'D':
            if q.isEmpty():
                print(-1)
            else:
                print("Pop {} size in queue is {} ".format(q.dequeue(),q.size()))

    if q.isEmpty():
        print("Empty")
    else:
        q.items.reverse()
        print("Number in Queue is :  {} ".format(q.items))


if __name__ == '__main__':
    main()