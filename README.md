
# 1. Ошибка

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
# 2. Запись в файл
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

