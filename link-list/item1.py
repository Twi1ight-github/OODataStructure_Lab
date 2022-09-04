class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data)
        
        while cur.next != None:
            
            s +=  " <- "+str(cur.next.data) 
            cur = cur.next
        
        return s

    def append(self,item):
        p = Node(item)
        cur = self.head
        if self.head == None:
            self.head = p
            self.tail = p
        else:
            while 1:
                if cur.next == None:
                    cur.next = p
                    self.tail = p
                    p.next = None

                    break
                cur = cur.next
    def changeHead(self,H):
        cur = self.head
        newcur = self.head
        new_head = Node(H)
        self.tail.next = self.head
        while 1:
            if cur.data == new_head.data:
                self.head = cur
                break
            cur = cur.next
        
        while 1:
            if newcur.next.data == new_head.data:
                self.tail = newcur
                self.tail.next = None
                break
            newcur = newcur.next
            



def main():
    print(' *** Locomotive ***')
    inp = input("Enter Input : ").split(" ")

    train = LinkedList()
    for item in inp:
        train.append(item)

    print('Before : {}'.format(train))
    train.changeHead('0')
    print('After : {}'.format(train))
    

if __name__ == '__main__':
    main()

