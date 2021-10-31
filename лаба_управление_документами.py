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
    nama = "нет такого документа"
    for s in documents:
        if num == s['number']:
            nama = s['name']
    return nama


def shelf():
    shelf_num = ""
    for key in directories:
        if vvod in directories[key]:
            shelf_num = key
    if shelf_num == "":
        print('нет такого дока')
    return shelf_num


def list_1():
    for str_spis in documents:
        print(str_spis['type'], str_spis['number'], str_spis['name'])
    str_spis = 0
    return


def add_sh():
    num_sh = "999"
    str_spis = {}
    str_spis['type'] = str(input("тип документа: "))
    str_spis['number'] = str(input("номер документа: "))
    str_spis['name'] = str(input("Владелец документа: "))
    while num_sh not in directories.keys():
        num_sh = str(input("полка документа: "))
        if num_sh not in directories.keys():
            print('Не тупи')
    documents.append(str_spis)
    directories[num_sh] = str_spis['number']
    return str_spis


def del_str(nomdoc):
    i = 0
    for str_spis in documents:
        if nomdoc in str_spis.values():
            print('нашел-убил')
            del documents[i]
            # del documents[i]
            # del documents[i]
        else:
            print('нету')
        i += 1
    print(documents)
    return


def mov_sh(nomdoc):
    if shelf() == '':
        return
    kuda = str(input("куда: "))
    nom_spis = 0
    sh = 0
    if kuda not in directories.keys():
        print("mimo")
        return
    for key in directories:
        i = 0
        for els in directories[key]:
            if nomdoc == els:
                sh = key
                nom_spis = i
                print(sh, nom_spis)
                print("было ", directories)
                del directories[sh][nom_spis]

                directories[kuda].append(nomdoc)
                print("стало ", directories)
                return
            i += 1
    return


def add_shelf():
    polka = str(input("номер: "))
    if polka in directories.keys():
        print("есть такая")
        return
    else:
        directories[polka] = []
    print(directories)
    return


vvod = str(input("номер документа: "))
action = str(input("действие: "))
if action == 'a':
    add_sh()
if action == 'l':
    list_1()
if action == 's':
    print(shelf(vvod))
if action == 'p':
    print(people_doc(vvod))
if action == 'd':
    del_str(vvod)
if action == 'm':
    mov_sh(vvod)
if action == 'as':
    add_shelf()