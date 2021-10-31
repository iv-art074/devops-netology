
## 1. Ошибка

```
{ "info" : "Sample JSON output from our service\t",
    "elements" :[
        { "name" : "first",
        "type" : "server",
        "ip" : 7175 
        },
        { "name" : "second",
        "type" : "proxy",
    "ip": "71.78.22.43"        кавычек не было
        }
    	 ]
}
```
## 2. Запись в файл
```
from typing import Any

import socket as sckt
import time as time
import json
import yaml

srv_lst = {'mail.google.com': '0.0.0.0', 'drive.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}

data = []
while True:  # бесконечный цикл

    hosts: Any
    for hosts in srv_lst:
        ip = sckt.gethostbyname(hosts)
        if ip != srv_lst[hosts]:
            with open('file1.json', 'w') as js:
                print('[изменен] ' + str(hosts) + ' IP mismatch: ' + srv_lst[hosts] + ' ' + ip)
                data.append({hosts: ip})
                json_data = json.dump(data, js)
            with open('file1.yaml', 'w') as ym:
                yaml_data = yaml.dump(data, ym)
            srv_lst[hosts] = ip
    time.sleep(5)
```
![Screenshot_3](https://user-images.githubusercontent.com/87374285/139209570-a64c6b85-8ea9-432e-b2b1-47cbf5d77270.png)

![Screenshot_1](https://user-images.githubusercontent.com/87374285/139209905-58252bdc-3c18-42a8-b3e8-96fe92307345.png)

# 3. Парсер JSON-YAML
```
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
```
![results](https://user-images.githubusercontent.com/87374285/139353586-14a0cb0f-4d07-4ce2-badb-44fee08c1f33.png)
