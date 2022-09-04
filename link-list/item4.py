class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        dummyH = Node(None)
        dummyT = Node(None)

        self.cursor = Node("|")
        self.head = dummyH
        self.tail = dummyT

        self.cursor.next = self.tail
        self.tail.prev = self.cursor
        self.head.next = self.cursor
        self.cursor.prev = self.head

    def isEmpty(self):
        return self.head == None

    def insert(self, item):

        p = Node(item)
        current = self.head
        while current.next != self.cursor:
            current = current.next
        current.next = p
        self.cursor.prev = p
        p.next = self.cursor
        p.prev = current

    def left(self):
        CurNext = self.cursor.next
        CurPrev = self.cursor.prev
        CurPrevNext = self.cursor.prev.next
        CurPrevPrev = self.cursor.prev.prev
        if CurPrevPrev != None:
            self.cursor.prev = CurPrevPrev
            self.cursor.next = CurPrev
            self.cursor.next.prev = self.cursor
            self.cursor.next.next = CurNext
            self.cursor.prev.next = CurPrevNext
            self.cursor.next.next.prev = CurPrev

    def right(self):
        CurNext = self.cursor.next
        CurPrev = self.cursor.prev
        CurNextNext = self.cursor.next.next
        if CurNextNext != None:
            self.cursor.next = CurNextNext
            self.cursor.next.prev = self.cursor
            self.cursor.prev = CurNext
            self.cursor.prev.next = self.cursor
            self.cursor.prev.prev = CurPrev
            self.cursor.prev.prev.next = CurNext

    def back(self):
        CurPrevPrev = self.cursor.prev.prev
        if CurPrevPrev != None:
            self.cursor.prev = CurPrevPrev
            self.cursor.prev.next = self.cursor

    def delete(self):
        cnn = self.cursor.next.next
        if cnn != None:
            self.cursor.next = cnn
            self.cursor.next.previouis = self.cursor
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head.next, str(self.head.next.value) + " "
        while cur.next != self.tail:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

def main():
    vim = LinkedList()
    inp = input('Enter Input : ').split(',')
    for i in range(len(inp)):
        cmd = inp[i][0]
        txt = inp[i][2:]
    
        if cmd == "I":
            vim.insert(txt)
        elif cmd == "L":
            vim.left()
        elif cmd == "R":
            vim.right()
        elif cmd == "B":
            vim.back()
        elif cmd == "D":
            vim.delete()
    print(vim)

if __name__ == '__main__':
    main()