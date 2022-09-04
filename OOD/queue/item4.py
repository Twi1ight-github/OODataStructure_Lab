class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []

q = Queue()
sec_id,op = input('Enter Input : ').split('/')
sec_id = sec_id.split(',')
op = op.split(',')
countE = 0
depart_list = []
found_status = False

for item in op:
    de = item[0]
    employee = item[2:]
    
    if de == 'D':
        if q.isEmpty():
            print('Empty')
        else:
            print(q.dequeue())

    
    elif de == 'E':
        countE += 1
        if countE == 1: #first Enqueue
            q.enqueue(employee)
            continue
          
        for i in range(len(sec_id)): #find hold department
            if employee == sec_id[i][2:]:
                holdDepart = sec_id[i][0]
                break
          
        for i in range(len(q.items)): #list depart in queue
            for j in range(len(sec_id)):
                if q.items[i] == sec_id[j][2:]:
                    depart_list.append(sec_id[j][0])

        for i in range(len(depart_list)-1,-1,-1): #find index for insert
            if depart_list[i] == holdDepart:
                ins_index = i+1
                found_status = True
                break
            else:
                found_status = False
            
        if found_status == True: #insert
            q.items.insert(ins_index,employee)
        else:
            q.enqueue(employee)

        #clear list
        depart_list = []  


        
        

                
        
        
        

        

        

