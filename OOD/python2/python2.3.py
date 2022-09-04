
def range_fn(a, b=None, c=None):
    def format(number):
        return round(number, 3)

    tp = []
    if b == None and c == None:
        a_copy = int(a)
        for i in range(a_copy):
            tp.append(float(i))
    elif c == None:
        a_copy = float(a)
        b_copy = float(b)
        while a_copy <= b_copy:
            tp.append(float(a_copy))
            a_copy = a_copy + 1
    else:
        a_copy = float(a)
        b_copy = float(b)
        c_copy = float(c)

        while a_copy <= b_copy:
            tp.append(float(a_copy))
            a_copy = a_copy + c_copy

    for i in range(0, len(tp)):
        digit = len(str(tp[i]).split(".")[1])

        if int(digit) >= 3:
            tp[i] = float(format(tp[i]))

    tp = tuple(tp)
    return tp


print("*** New Range ***")

input = input("Enter Input : ").split()
length = len(input)
a, b, c = None, None, None
if length == 1:
    a = float(input[0])
if length == 2:
    a = float(input[0])
    b = float(input[1])
if length == 3:
    a = float(input[0])
    b = float(input[1])
    c = float(input[2])


print(range_fn(a, b, c))
