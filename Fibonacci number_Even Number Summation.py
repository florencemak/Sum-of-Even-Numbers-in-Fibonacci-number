def even_sum(n):
    a = 1
    b = 1
    sum = 0
    while n > b:
        c = a + b
        a = b
        b = c
        if ((b % 2) == 0) & (n >= b):
            sum = sum + b
    return sum
print((even_sum(4000000)))