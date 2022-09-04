l1 = ['1 101','1 102','2 201','2 202']
l2 = ['101','102','201','202']

for i in range(len(l2)):
    for j in range(len(l2)):
        if l2[i] == l1[j][2:]:
            print('found')
        else:
            print('not found')