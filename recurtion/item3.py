def addZero(binary,digit):
    lenght = len(str(binary))
    if digit>lenght:
        binary = '0'+binary
        return addZero(binary,digit)
    return binary


def decimalToBinary(dec,digit):
    binary = bin(dec).replace("0b", "")
    lenght = len(str(binary))

    if digit>lenght:
        return addZero(binary,digit)
        
    return binary

def seriesBinary(N, n=0):
    
    if N < 0: 
        print("Only Positive & Zero Number ! ! !")
        return

    print(decimalToBinary(n,N))

    if n < pow(2,N)-1:
        seriesBinary(N, n + 1)

inp = int(input('Enter Number : '))
seriesBinary(inp)
