def sharp(n):
    print('#'*n, end='')


def underScore(n):
    print('_'*n, end='')


def staircase(n, count=0):

    if n == 0:
        print("Not Draw!")
        return

    if n > 0:
        underScore(n-1)
        sharp(count+1)
        print()
        if n > 1:
            staircase(n-1, count+1)

    elif n < 0:
        underScore(count)
        sharp(abs(n))
        print()
        if n < -1:
            staircase(n+1, count+1)

    else:
        return


staircase(int(input("Enter Input : ")))
