# # задание 3
#
#
def thesaurus(*names):
    new_list = dict()
    for name in names:
        new_list.setdefault(name[0], [])
        new_list[name[0]].append(name)
    return new_list

print(thesaurus("Иван", "Мария", "Петр", "Илья"))