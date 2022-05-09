def set_bit(x,n):
    m=1<<n
    return x|m
def reset_bit(x,n):
    m=1<<n
    return x&(~m)
def toggle_bit(x,n):
    m=1<<n
    return x^m
def get_bit(x,n):
    m = 1 << n
    if (x & m == 0):
        return 0
    else:
        return 1

print(set_bit(5,4))
print(reset_bit(5,4))
print(toggle_bit(5,4))
print(get_bit(5,4))