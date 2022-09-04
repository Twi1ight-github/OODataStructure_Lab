class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

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
                    p.previous = cur
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

    def insert(self, pos, item):

        p = Node(item)

        if (pos < 0):
            temp = self.tail

            if pos < (-1*self.size()):
                self.addHead(item)
            else:
                for i in range(-1, -1*(self.size()), -1):

                    if i == pos:
                        p.next = temp
                        p.previous = temp.previous

                        temp.previous.next = p
                        temp.previous = p
                        break

                    temp = temp.previous

        elif (pos == 0):
            self.addHead(item)
        else:
            if pos > self.size()-1:
                self.append(item)

            else:
                temp = self.head
                for i in range(0, pos):
                    if (temp != None):
                        temp = temp.next

                if (temp != None and temp.next != None):
                    p.next = temp
                    p.previous = temp.previous
                    temp.previous.next = p
                    temp.previous = p

                elif temp != None and temp.next == None:
                    self.append(item)

                else:
                    pass

    def search(self, item):
        current = self.head

        while current != None:
            if current.value == item:
                return 'Found'

            current = current.next

        return 'Not Found'

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.value == item:
                return index
            current = current.next
            index = index + 1

        return -1

    def size(self):
        temp = self.head
        count = 0

        while (temp != None):
            count += 1
            temp = temp.next
        return count

    def pop(self, pos):
        if (pos < 0):
            return 'Out of Range'
        elif (pos == 0 and self.head != None):
            nodeDelete = self.head
            self.head = self.head.next

            nodeDelete.next = None
            nodeDelete.previous = None
            nodeDelete.value = None

            return 'Success'
        else:

            temp = self.head
            for i in range(0, pos):
                if (temp != None):
                    temp = temp.next

            if (temp != None and temp.next != None):

                temp.previous.next = temp.next
                temp.next.previous = temp.previous

                temp.next = None
                temp.previous = None

                temp = None
                return 'Success'

            elif temp != None and temp.next == None:
                self.tail = temp.previous
                temp.previous = None
                temp.next = None
                self.tail.next = None

                return 'Success'

            else:
                return 'Out of Range'


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
