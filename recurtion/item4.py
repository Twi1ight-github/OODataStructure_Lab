def inputS(ls, newLs=[], index=0, lenght=0):

    if lenght < len(ls)//2:
        data = ls[index]
        newLs.append(data)
        inputS(ls, newLs, index+2, lenght+1)
    return newLs


def inputB(ls, newLs=[], index=1, lenght=0):

    if lenght < len(ls)//2:
        data = ls[index]
        newLs.append(data)
        inputS(ls, newLs, index+2, lenght+1)
    return newLs


def multS(items):
    if len(items) == 1:
        return items[0]
    return items[0] * multS(items[1:])


def sumB(items):
    if len(items) == 1:
        return items[0]
    return items[0] + sumB(items[1:])


def difference(l1, l2, index=0, res=[]):
    if index < len(l1):
        diff = abs(l1[index] - l2[index])
        res.append(diff)
        difference(l1, l2, index+1, res)

    return res


def powerSet(input):

    if len(input) == 0:
        return [[]]
    leading = (input[0])
    new_input = input[1:len(input)]
    ps1 = list((powerSet(new_input)))
    ps2 = map(lambda x: [leading]+x, ps1)

    ps_list = list(map(lambda x: list(x), ps2))

    return ps1 + ps_list


S, B = [], []
inp = input("Enter Input : ").replace(',', ' ').replace(' ', ' ').split()
inp = list(map(int, inp))

S, B = inputS(inp), inputB(inp)

psS, psB = powerSet(S), powerSet(B)
psS.remove([])
psB.remove([])

sMap, bMap = list(map(multS, psS)), list(map(sumB, psB))

diffList = difference(sMap, bMap)
result = min(diffList)
print(result)
