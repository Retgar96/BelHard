# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)


data = {'1': {'name': 'andrey', 'surname': 'nikolaev', 'phone': '51345134', 'mail': 'test@mail.com'},
        '2': {'name': 'anton', 'surname': 'ferarry', 'phone': '111111', 'mail': ''},
        '3': {'name': '3name', 'surname': '3surname', 'phone': '443142'}}



for key, value in data.items():
    if 'mail' in value.keys() and value['mail'] != '':
        print(data[key])
