# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

result = dict()
text = input()
for x in text:
    result[x] = text.count(x)

print(result)



