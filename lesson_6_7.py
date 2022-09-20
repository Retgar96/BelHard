# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка


numbers = [1, 2, 3, 4, 5]

size = len(numbers)
for i in range(size):
    right = i+1
    if right == size:
        right = 0
    left = i-1
    print(numbers[left]+numbers[right])