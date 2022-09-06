# Первое задание: "Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами"

# Первый способ
text = input().strip()
text.replace(' ', '-')
print(text)

# Второй способ:
text = input().strip()
text = text.split()
text = '-'.join(text)
print(text)