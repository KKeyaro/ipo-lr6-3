kstr = int(input("Введите количество строк: ")) #Просим пользователя ввести количество строк
while kstr <= 0: #Используем цикл for
    kstr = int(input("Количество строк должно быть положительным. Введите снова: ")) #Выведется если условие будет выполнено
lines = [] #Создаем список
for i in range(kstr): #Используем цикл for
    lines.append(input("Введите строку: ")) #Добавляем в список то что введет пользователь
text = ' '.join(lines) #Конвертируем список в строку
words = text.split() #Разделяем строку на слова
print(f"Количество слов: {len(words)}") #Выводим количество слов
