'''
จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  

LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

*** Hint ***

ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ
'''

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def delete(self, dlt):
        if dlt in self.items:
            return self.items.remove(dlt)

    def clear(self):
        self.items = []

    def __str__(self):
        return str(self.items)


s = Stack()
def ManageStack(value):

    for i in value:
        num = i[2:]
        less, more = i[3:], i[3:]

        if i[0] == 'A':
            s.push(num)
            print("Add = {} ".format(num))
        elif i[0] == 'P':
            if s.isEmpty():
                print(-1)
            else:
                print("Pop = {} ".format(s.pop()))
        elif i[0] == 'D':
            if s.isEmpty():
                print(-1)
            else:
                dl = num
                while dl in s.items:
                    s.delete(dl)
                    print("Delete = {} ".format(dl))

        elif i[0] == 'L' and i[1] == 'D':
            tempL = Stack()
            if s.isEmpty():
                print(-1)
            else:
                for x in s.items:
                    count = int(x)
                    target = int(less)
                    if count < target:
                        
                        tempL.push(x)

                tempL.items.reverse()        
                for x in tempL.items:
                    if x in s.items:
                        s.delete(x)
                        print(
                            "Delete = {} Because {} is less than {}".format(x, x, less))
            tempL.clear()

        elif i[0] == 'M' and i[1] == 'D':
            tempM = Stack()
            if s.isEmpty():
                print(-1)
            else:
                for x in s.items:
                    count = int(x)
                    target = int(less)
                    if count > target:
                        tempM.push(x)
                tempM.items.reverse()
                for x in tempM.items:
                    if x in s.items:
                        s.delete(x)
                        print("Delete = {} Because {} is more than {}".format(x, x, more))
            tempM.clear()


def main():
    value = input("Enter Input : ").split(",")
    ManageStack(value)
    print("Value in Stack = ", end="")
    print([int(x) for x in s.items])


if __name__ == '__main__':
    main()
