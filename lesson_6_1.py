#Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

def transform(number):
    result = 0
    multiplier = 1
    while number != 0:
        result = result + number % 2 * multiplier
        number = number // 2
        multiplier *= 10
    return result

print(transform(55))
