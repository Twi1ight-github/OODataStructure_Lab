def required_steps(n):
    if n < 0:
        return 'Only Positive & Zero Number ! ! !'
    if n == 0:
        return 0
    return required_steps(n-1)

print(required_steps(3))