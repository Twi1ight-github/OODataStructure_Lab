
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
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
                    p.prev = cur
                    p.next = None

                    break
                cur = cur.next

    def addHead(self, item):
        p = Node(item)
        p.next = self.head
        if self.head != None:
            self.head.previous = p
            self.head = p
            p.previous = None

        else:
            self.head = p
            self.tail = p
            p.previous = None

    def size(self):
        temp = self.head
        count = 0

        while (temp != None):
            count += 1
            temp = temp.next
        return count

    def sortList(self):
        # Check whether list is empty
        if (self.head == None):
            return
        else:
            # Current will point to head
            current = self.head
            while (current.next != None):
                # Index will point to node next to current
                index = current.next
                while (index != None):
                    # If current's data is greater than index's data, swap the data of current and index
                    if (int(current.value) < int(index.value)):
                        temp = current.value
                        current.value = index.value
                        index.value = temp
                    index = index.next
                current = current.next

    def isEmpty(self):
        return self.head == None

    def clear(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value)+" "

        while cur.next != None:

            s += str(cur.next.value)+" "
            cur = cur.next

        return s

    def display(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value)

        while cur.next != None:

            s += ' -> '+str(cur.next.value)
            cur = cur.next

        return s


before = LinkedList()
after = LinkedList()


def radix():

    
    rd = 0
    addDigit = 1

    while 1:
        if int(before.size()) == int(after.size()) and int(digit) == 0:
            break
        print('------------------------------------------------------------')
        print('Round : {}'.format(rd+1))
        for num in range(10):
            temp = LinkedList()
            cur = before.head
            while cur != None:
                digit = (int(abs(cur.value)) % (10*addDigit))//addDigit
                if abs(digit) == num:
                    data = cur.value
                    temp.append(data)

                cur = cur.next
            temp.sortList()
            if temp.isEmpty() == True:
                print('{} : '.format(num))
            else:
                print('{} : {}'.format(num, temp))
            if temp.size() == before.size() and digit == 0:
                t = temp.head
                while t != None:
                        after.append(t.value)
                        t = t.next
                        
        addDigit *= 10
        rd += 1
       
        
    print('------------------------------------------------------------')
    print('{} Time(s)'.format(rd-1))


def main():

    inp = input('Enter Input : ').split(" ")

    for i in inp:
        before.append(int(i))

    radix()

    print('Before Radix Sort : {}'.format(before.display()))
    print('After  Radix Sort : {}'.format(after.display()))


if __name__ == '__main__':
    main()
