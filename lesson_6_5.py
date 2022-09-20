# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

data = [1, 2, 3, 4, 5]

size = len(data)


for i in range(size):
        i += 1
        index = size-i
        data.append(data[index])

for i in data:
    data.remove(i)
