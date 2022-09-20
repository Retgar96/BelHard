#Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

action_list = ['*','/','+','-','^','%']
while True:
    A = input('Введите первое число\n')
    action = input('Введите действие\n')
    B = input('Введите второе число\n')

    if A.isdigit() and B.isdigit():
        A = float(A)
        B = float(B)
    else:
        print(f'Введите числа в формате цифр')
        continue

    if action in action_list:
        print(eval(f'{A} {action} {B}'))
    else:
        print('Введите один из указанных знаков *,/,+,-,^,%')


