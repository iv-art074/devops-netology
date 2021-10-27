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
