'''
ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4

***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***

*** สามารถสร้างได้มากกว่า 1 stack ***
'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []

    def clear(self):
        self.items.clear()


blue = Stack()
red = Stack()
def main():
    
    print("******** Parking Lot ********")

    #input
    m,s,o,n = input("Enter max of car,car in soi,operation : ").split()

    #clean input
    s=s.split(',')
    s = [int(i) for i in s]
    if s == [0]:
        s = []

    m,n = int(m),int(n)

    
    # add car in soi
    for car_id in s:
        if blue.size() < m:
            blue.push(car_id)
        else:
            print('car {} cannot arrive : Soi Full'.format(car_id))

    # operation
    if o == 'arrive':
        if n in blue.items:
            print('car {} already in soi'.format(n))
        else:
            if blue.size() < m:
                blue.push(n)
                print('car {} arrive! : Add Car {}'.format(n,n))
            else:
                print('car {} cannot arrive : Soi Full'.format(n))
    elif o == 'depart':
        if blue.isEmpty():
            print('car {} cannot depart : Soi Empty'.format(n))

        else:
            if n in blue.items:
                while True:
                    if blue.peek() == n:
                        blue.pop()
                        print('car {} depart ! : Car {} was remove'.format(n,n))
                        break
                    else :
                        red.push(blue.pop())
            else:
                print('car {} cannot depart : Dont Have Car {}'.format(n,n))

            
    # push car back to blue soi
    while not red.isEmpty():
        blue.push(red.pop())
        
    # print result    
    print(blue.items)

if __name__ == '__main__':
    main()
