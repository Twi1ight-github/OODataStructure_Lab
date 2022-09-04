


def targetSum(arr, target):
    result_list = []
    
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if int(arr[i])+int(arr[j])+int(arr[k]) == target: 
                    result_list.append([int(arr[i]),int(arr[j]),int(arr[k])])
                    result_list.sort()
    for i in range(0,len(result_list)):
        result_list[i].sort()
    cleanlist = []
    [cleanlist.append(x) for x in result_list if x not in cleanlist]
    return cleanlist
       
           
target = 5
list = []
list = input("Enter Your List : ").split()
if len(list)<3:
    print("Array Input Length Must More Than 2")
    exit()
print(targetSum(list, target))
