from typing import Any
from pprint import pprint
import socket as sckt
import time as time
import json
import yaml
import sys

if len(sys.argv) > 1:
    file=sys.argv[1]

    try:
        with open(file, encoding='utf-8') as f:#читаем json
            data: Any = json.load(f)
            pprint(data)
            with open(file.rsplit( ".", 1 )[ 0 ]+'.yaml', 'w') as ym:
                yaml_data = yaml.dump(data, ym)
               
    except json.JSONDecodeError as exx:
        if exx.msg=="Extra data" or exx.msg=="Expecting value": #несоответствие формата
           print('Это не JSON, пробуем YAML')
        else:  #битый файл
            print("Ошибка декодирования JSON строка ",exx.lineno)
            quit()
        try:
            datay: Any
            with open(file, encoding='utf-8') as fy:#читаем yaml
                datay = yaml.load(fy, Loader=yaml.FullLoader)
                pprint(datay)
                with open(file.rsplit( ".", 1 )[ 0 ]+'.json', 'w') as js:
                  json_data = json.dump(datay, js)
        except yaml.YAMLError as exc:
              if hasattr(exc, 'problem_mark'):
                mark = exc.problem_mark
                print("Ошибка преобразования Yaml файла строка %s" % (mark.line))
                if mark.line==0:
                    print("это не наш формат")
              else:
                print("Что-то не так с файлом YAML")
        else:
            print('Это YAML, обработано YAML-JSON')
    else:
        print("Обработано JSON-YAML")

else:
  print ("пусто в аргументах")
