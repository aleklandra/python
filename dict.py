#Найти самый часто встречающийся в строке (кодировка UTF-8) символ. Если несколько символов встречаются одинаковое кол-во раз, то можно вывести любой.


string = input("Введите строку:")
print(string)
dictionary = {}

for simbol in list(string):
    dictionary.setdefault(simbol,0)
    dictionary[simbol]+=1
    
print(dictionary)

key = 'no simbols'
num = 0

for simbol in dictionary:
    if dictionary[simbol]>num:
        num = dictionary[simbol]
        key = simbol
        
print(key,' ', num)
    

