'''
กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป

ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

อธิบาย Input :   A  <Heights>  แสดงถึงความสูงของต้นไม้  ,   B  คือการหันหลังกลับมามอง

อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 

โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง
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


S = Stack()
T = Stack()

inp = input('Enter Input : ').split(',')

for index in range(len(inp)):

    tree_meter = inp[index][2:]
    key = inp[index][0]

    if key == 'A':
        S.push(tree_meter)
           
    elif key == 'B':
        if not S.isEmpty():
            T.push(S.peek())
              
        for count_tree in range(len(S.items)-1,-1,-1):         
            backTree = T.peek()
            
            if int(backTree) < int(S.items[count_tree]):
                if not S.isEmpty():
                    T.push(S.items[count_tree])
                       
        print(T.size())
        T.clear()
