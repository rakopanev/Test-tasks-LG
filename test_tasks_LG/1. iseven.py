# Алгоритм определения четности целого числа может быть следующим:

def isEven1(value):
    return value & 1 == 0

def isEven2(value):
    return (value >> 1) << 1 == value
