# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n = int(input('Введите конечное значение ключа\n'))
result = dict()

for x in range(1, n+1):
    result[x] = dict()
    result[x]['name'] = input(f'Введите name у обьекта {x}\n')
    result[x]['email'] = input(f'Введите email у обьекта {x}\n')

print(result)
