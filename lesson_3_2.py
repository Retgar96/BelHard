# Второе задание: "Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3"
num_1 = input('Введите число 1').isalnum()
num_2 = input('Введите число 2').isalnum()
num_3 = input('Введите число 3').isalnum()
avg = (num_1+num_2+num_3)/3
print(avg)