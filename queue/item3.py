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


book_shelf = Queue()
book,op = input('Enter Input : ').split('/')

book = book.split(' ')
op = op.split(',')

for item in book:
    book_shelf.enqueue(item)

for item in op:
    ed = item[0]
    id_book = item[2:]

    if ed == 'D':
        book_shelf.dequeue()

    elif ed == 'E':
        book_shelf.enqueue(id_book)


if len(book_shelf.items) != len(set(book_shelf.items)):
    print("Duplicate")
else:
    print("NO Duplicate")