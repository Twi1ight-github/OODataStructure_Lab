print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
#heart
for row in range((n*-1)+1,n+n-1):
    for col in range((n*-1)-(n-2),n+n-1):
        if abs(row)+abs(col) == n+n-2 or (abs(row)==abs(col) and row<=0):
            print("*",end="")
        elif abs(row)+abs(col)<= n+n-3 and abs(col) >= abs(row):
            print("+",end="")
        elif abs(col)<= n-2 and row>=0 and abs(col)+row <= n+n-3:
            print("+",end="")
        else:
            print(".",end="")
    
    print()
        