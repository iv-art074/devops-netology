from typing import Any

import socket as sckt
import time as time
import json
import yaml

srv_lst = {'mail.google.com':'0.0.0.0', 'drive.google.com':'0.0.0.0','google.com':'0.0.0.0'}


while True : #бесконечный цикл
  data=[]
  hosts: Any
  for hosts in srv_lst:
    ip = sckt.gethostbyname(hosts)
    if ip != srv_lst[hosts]:
      with open('file1.json', 'a') as js:
        print('[изменен] ' + str(hosts) +' IP mistmatch: '+srv_lst[hosts]+' '+ip)
        json_data= json.dumps({hosts:ip})
        js.write(json_data)
      with open('file1.yaml', 'a') as ym:
        yaml_data= yaml.dump({hosts:ip})
        ym.write(yaml_data)
      srv_lst[hosts]=ip
  time.sleep(5)