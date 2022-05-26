# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
count = 0
for letter in word.lower():
    if letter in vowels:
        count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(sentence.count(' ') + 1)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
ls = sentence.split(' ')
for word in ls:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
total_words = sentence.count(' ') + 1
total_lenght = len(sentence.replace(' ', ''))
average_length = total_lenght / total_words
print(int(average_length))
