n=int(input("Введите количество строк: ")) #ввод количества
if n<=0: #если ввели 0 или меньше 0
    print("Ошибка") #вывод ошибки
s=str(input("Введите строки: ")) #ввод строк
words=s.split() #разделяем на слова
words_count=0 #начало подсчета
for i in words: #использование цикла
    words_count +=1 #работа подсчета
print("Количество слов: ", words_count) #вывод