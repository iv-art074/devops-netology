from typing import Any
from pprint import pprint
import socket as sckt
import time as time
import json
import yaml
import sys

# srv_lst = {'mail.google.com': '0.0.0.0', 'drive.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}

# data = []


if len(sys.argv) >= 1:
    # for param in sys.argv:
    #       print (param)

    try:
        with open(sys.argv[1], encoding='utf-8') as f:
            data: Any = json.load(f)
            pprint(data)
    except json.JSONDecodeError as exx:
        if exx.msg=="Extra data":
        # print(data)
            print('Это не JSON, пробуем YAML')
        else:
            print("Ошибка декодирования JSON строка ",exx.lineno)
            # quit()
        try:
            datay: Any
            with open(sys.argv[1], encoding='utf-8') as fy:
                datay = yaml.load(fy, Loader=yaml.FullLoader)
                pprint(datay)
        except yaml.YAMLError as exc:
            # print ("Ошибка чтения")
            if hasattr(exc, 'problem_mark'):
                mark = exc.problem_mark
                print("Ошибка преобразования Yaml файла строка %s" % (mark.line))
                if mark.line==0:
                    print("это не наш формат")
            # except yaml.parser.ParserError:
            # print ("Ошибка в строке №",n,line)
            # except yaml.scanner.ScannerError:
            # print ("Ошибка в строке №",n,line)
            else:
                print("Что-то не так с файлом YAML")
            # print('Это не YAML, пипец')
        else:
            print('Это YAML, обработано YAML-JSON')
    else:
        print("Обработано JSON-YAML")

# else:
# print ("пусто в аргументах")