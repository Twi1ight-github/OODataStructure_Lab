'''
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา

A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

P                 ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def main():
    stack = Stack()
    value = input("Enter Input : ").split(",")
    
    for i in value:
        if i[0] == 'A':
            stack.push(i[2:])
            print("Add = {} and Size = {}".format(i[2:],stack.size()))

        elif i[0] == 'P':
            if stack.is_empty():
                print(-1)
            else:
                print("Pop = {} and Index = {}".format(stack.pop(),stack.size()))
        else:
            exit()
        
        

    if stack.is_empty():
        print("Value in Stack = Empty")
    else:
        print("Value in Stack = "+" ".join(stack.items))


if __name__ == '__main__':
    main()
