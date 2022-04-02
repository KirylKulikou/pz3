# задание 1

num_eng = ['one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eit', 'nine', 'ten']
num_rus = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
dict_transl = dict(zip(num_eng, num_rus))
def num_translate(x):
    if x in dict_transl:
        print(dict_transl[x], None)
num_translate('ten')
num_translate('два')
# не смог сделать с рус на анг(