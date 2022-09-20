# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

number = [1, 2, 3, 4, 5, 6]


A = list(filter(lambda x: x%2, number))
B = list(filter(lambda x: not x%2, number))
result = A+B
print(result)



