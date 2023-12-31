# Алгоритм определения четности целого числа может быть следующим:

def isEven1(value):
    return value & 1 == 0

def isEven2(value):
    return (value >> 1) << 1 == value

# Оба варианта решения основываются на том факте, что последний бит чётного числа всегда равен нулю.
# При выполнении побитового сдвига числа влево и затем вправо, число останется неизменным, и при сравнении с исходным числом результат будет истинным.
# В случае нечётного числа, последний бит, равный единице, будет преобразован в ноль, и при сравнении выдаст ложный результат.
# Побитовая операция И применима как к положительным, так и к отрицательным числам, в отличие от оператора модуля % (остаток от деления).
