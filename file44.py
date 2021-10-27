from typing import Any
import yaml
import json
from pprint import pprint

with open('file1.json', encoding = 'utf-8') as f:
    data: Any=json.load(f)
    pprint (data)

with open('file1.yaml', encoding='utf-8') as fy:
    datay: Any = yaml.load(fy,Loader=yaml.FullLoader)
    pprint(datay)