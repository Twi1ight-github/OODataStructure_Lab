def fibo(n):
    n = int(n)
    if n==0:
        return 0
    elif n ==1:
        return 1
    else:
        return int(fibo(n-1)) + int(fibo(n-2))

n = input('Enter Number : ')
print('fibo({}) = {}'.format(n,fibo(n)))