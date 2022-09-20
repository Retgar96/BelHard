# Вывести первые N цисел кратные M и больше K

N = int(input('Введите N\n'))
M = int(input('Введите М\n'))
K = int(input('Введите K\n'))

count = 0
i = 0
while True:
    if count == N:
        print('Конец списка')
        break
    else:
        i += 1
        if i % M == 0:
            if i > K:
                count+=1
                print(i,'\n')

