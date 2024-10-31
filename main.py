# Написать программу, которая:
# - Запрашивает у пользователя количество строк. (*должно быть проверка*)
# - Затем сами строки.
# - Определяет, сколько различных слов содержится в этом тексте, и выводит из количество
# *Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.*

kstr = int(input("Введите количество строк: ")) #Запрашиваем у пользователя количество строк
while kstr <= 0: #Используем цикл
    kstr = int(input("Количество строк должно быть положительным. Введите снова: ")) #Если число не положительное, просим ввести снова
lines = [] #Создаем пустой список для хранения строк
for i in range(kstr): #Используем цикл
    line = input("Введите строку: ") #Запрашиваем ввод строки
    lines.append(line) #Добавляем строку в список
text = ' '.join(lines) #Объединяем все строки в одну с пробелами между ними
words = text.split() #Разделяем текст на слова
unique = set(words) #Определяем количество уникальных слов, используя множество
print(f"Количество различных слов: {len(unique)}") #Выводим количество различных слов
