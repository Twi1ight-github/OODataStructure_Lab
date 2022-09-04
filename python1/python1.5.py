print("*** Fun with countdown ***")
ls=[]
countdown = []
cleanlist = []
result = []
ls = [int(item) for item in input("Enter List : ").split()]


for i in range(len(ls)-1,-1,-1):
    
        
        
    if ls[i]+1 == ls[i-1] : #check sort number
        if i == 0 and ls[0]-1 == ls[1] : #last number
            countdown.append(ls[0])
        countdown.append(ls[i])
        
    else:
        try:
            if i!=0 and i!= len(ls)-1 and ls[i]-1 == ls[i+1]:
                countdown.append(ls[i])
        except :
            countdown.append(ls[i])
            

        if i == 0 and ls[0]-1 == ls[1]: #last number
            countdown.append(ls[0])
        
        if ls[i] == 1 and 1 not in countdown:
            countdown.append(1)

        countdown.sort(reverse=True)
        cleanlist.append(countdown)
        countdown = []

#claer empty list

while [] in cleanlist :
    cleanlist.remove([])

cleanlist.reverse()
n = len(cleanlist)
result.append(n)
result.append(cleanlist)
print(result)

        
   



    