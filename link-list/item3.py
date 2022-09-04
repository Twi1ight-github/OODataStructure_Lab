


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        p = Node(data)
        
        if self.head == None: # null list
            self.head = p 
        else:
            t = self.head
            while t.next != None :
                t = t.next 
            
            t.next = p

    def display(self):
        p = self.head
        while p != None:
            print(p.data+" ",end='') 
            p = p.next
        print()



def main():
    l1,l2 = input('Enter Input (L1,L2) : ').split(' ')
    
    
    l1=l1.split('->')
    l2=l2.split('->')

    linkedlist1 = LinkedList()
    linkedlist2 = LinkedList()
    mergelist = LinkedList()
    
    for i in l1:
        linkedlist1.append(i)

    for i in l2:
        linkedlist2.append(i)

    for i in l1:
        mergelist.append(i)

    for i in reversed(l2):
        mergelist.append(i)

    print('L1    : ',end = '')
    linkedlist1.display()

    print('L2    : ',end = '')
    linkedlist2.display()

    print('Merge : ',end = '')
    mergelist.display()

    

if __name__ == '__main__':
    main()
