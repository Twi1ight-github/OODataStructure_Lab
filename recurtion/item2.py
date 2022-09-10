


def isPalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return isPalindrome(word[1:-1])

inp = input('Enter Input : ')
print("'"+"".join(inp)+"'"+' is palindrome') if isPalindrome(inp) else print("'"+"".join(inp)+"'"+' is not palindrome')