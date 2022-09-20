#**Вывести четные числа от 2 до N по 5 в строку

while True:
    N = input('Введите значение N\n')
    if N.isdigit():
        N = float(N)
        break
    else:
        print('Введите значение N в числовом формате')



i = 0
count = 0
while i < N:
    i+=1
    if i % 2 == 0:
        count+=1
        if count == 5:
            count = 0
            print(i)
        else:
            print(i,' ', end='')



