# -*- coding: utf-8 -*-
"""Копия блокнота "DZ_4.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15X-LArPIAVeFQJFbKWru_irQ2R5em0sD
"""

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def people_doc(num):

    ''' узнать владельца документа по его номеру '''

    nama = [dic['name'] for dic in documents if dic['number'] == num]
    return nama


def shelf(vvod):

    '''по номеру документа узнать, на какой полке он хранится'''

    shelf_num = [key for key, value in directories.items() for string in value if string == vvod]
    return shelf_num


def list_1():

    '''увидеть полную информацию по всем документам'''

    for str_spis in documents:
        print(f"№:{str_spis['number']}, тип: {str_spis['type']}, владелец: {str_spis['name']}, полка хранения:{shelf(str_spis['number'])[0]}")
    str_spis = 0
    return


def add_doc():

    ''' добавляем документ'''

    num_sh = "999"
    str_spis = {}
    str_spis['type'] = input("Введите тип документа: ")
    str_spis['number'] = input("Введите номер документа: ")
    str_spis['name'] = input("Введите владельца документа: ")
    while num_sh not in directories.keys():
        num_sh = input("Введите полку документа: ")
        if num_sh not in directories.keys():
            print('\nТакой полки не существует. Добавьте полку командой ads.\n Текущий список документов:\n')
        else:
            print("\nДокумент добавлен. Текущий список документов:\n")
            documents.append(str_spis)
            directories[num_sh].append(str_spis['number'])
        list_1()
    return

def del_str():

    '''по команде «d» может удалить документ из данных'''

    i = 0
    string = ""
    nomdoc=input("Введите номер документа: ")
    for str_spis in documents:
        if nomdoc in str_spis.values():
           del documents[i]
           directories[shelf(nomdoc)[0]].remove(nomdoc)
           string = "\nДокумент удален.\nТекущий список документов:\n"
           break
        else:
           string = "\nДокумент не найден в базе.\nТекущий список документов:\n"
        i += 1
    print(string)
    list_1()
    return


def add_shelf():

    '''добавить полку'''

    polka = input("\nВведите номер полки: ")
    if polka in directories.keys():
        print("Такая полка уже существует. Текущий перечень полок:",",".join(directories.keys()))
        return
    else:
        directories[polka] = []
    print("\nПолка добавлена. Текущий перечень полок:", ",".join(directories.keys()))
    return

def del_shelf(polka):

    '''удалить полку'''

    if directories.get(polka,"absent") != "absent":
       if len(directories.get(polka)):
          print("На полке есть документы, удалите их перед удалением полки. Текущий перечень полок:",",".join(directories.keys()))
       else :
          directories.pop(polka)
          print("\nПолка удалена. Текущий перечень полок:",",".join(directories.keys()))
    else :
       print("Такой полки не существует. Текущий перечень полок:",",".join(directories.keys()))
    return

def mov_sh():

    '''может переместить документ с полки на полку'''

    nomdoc=input("Введите номер документа: ")
    polka=shelf(nomdoc)
    if polka == []:
       print("\nДокумент не найден в базе.\nТекущий список документов:\n")
       list_1()
       return
    kuda = input("Введите номер полки:")
    if kuda not in directories.keys():
       print("\nТакой полки не существует. Текущий перечень полок:\n",",".join(directories.keys()))
       return

    print("\nИсходный список документов:\n")
    list_1()

    #delete
    directories[polka[0]].remove(nomdoc)
    #insert
    directories[kuda].append(nomdoc)
    print("\nДокумент перемещен.\nТекущий список документов:\n")
    list_1()

    return

def main():
  print("""Список доступных команд: \nl - список всех документов\nad - добавить документ\ns - узнать полку
p - узнать владельца\nd - удалить документ\nm - переместить документ\nads - добавить полку\nds - удалить полку\nq - выход""")
  while (action := str(input("\nВведите команду: "))) != 'q':
    if action == 'ad':
      add_doc()
    elif action == 'l':
      list_1()
    elif action == 's':
      vlad = shelf(input("\nВведите номер документа: "))
      print("Документ хранится на полке:",vlad[0]) if vlad != [] else print ("Документ не найден в базе")
    elif action == 'p':
      vlad = people_doc(input("\nВведите номер документа: "))
      print("Владелец документа:",vlad[0]) if vlad != [] else print ("Документ не найден в базе")
    elif action == 'd':
      del_str()
    elif action == 'm':
      mov_sh()
    elif action == 'ads':
      add_shelf()
    elif action == 'ds':
      del_shelf(input("\nВведите номер полки: "))


main()

