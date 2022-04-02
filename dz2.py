# задание 2

num_eng = ['one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eit', 'nine', 'ten']
num_rus = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
list_transl = dict(zip(num_eng, num_rus))
def num_translate_adv(num):
    if num[0].isupper:
        num = num.lower()
        print(list_transl.get(num).title())
    elif num in list_transl:
        print(list_transl.get(num))
    elif num not in list_transl:
        print(None)
num_translate_adv('Six')
