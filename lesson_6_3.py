# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

numbers = [1, 2, 3, 4, 5]

def transform(n:int, numbers:list):
    for i in range(len(numbers)):
        numbers[i] = numbers[i]+n
    return  numbers

print(transform(5, numbers))

#Или так:

numbers = [1, 2, 3, 4, 5]
n = 5
print(list(map(lambda x: x+n, numbers)))

