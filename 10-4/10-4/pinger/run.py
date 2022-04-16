#!/usr/bin/env python3

import logging
import random
import time
import datetime

#dt_now = datetime.datetime.now()

logging.basicConfig(filename='./logs/file.log',format='%(asctime)s,%(levelname)s ,%(message)s',datefmt='%Y-%m-%dT%H:%M:%S')
#logging.basicConfig(filename='./logs/file.log',format='{\"level\":\"%(levelname)s\",\"message\":\"%(message)s\"}')
while True:

    number = random.randrange(0, 4)
    if number == 0:
        logging.info('Hello there!!')
    elif number == 1:
        logging.warning('Hmmm....something strange')
    elif number == 2:
        logging.error('OH NO!!!!!!')
    elif number == 3:
        logging.exception(Exception('this is exception'))

#    dt_now = datetime.datetime.now()
    time.sleep(1)
"""    if number == 0:
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info('Hello there!!')
    elif number == 1:
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.WARNING)
        logging.warning('Hmmm....something strange')
    elif number == 2:
        logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.ERROR)
        logging.error('OH NO!!!!!!')
    elif number == 3:
        logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.DEBUG)
        logging.exception(Exception('this is exception'))
"""

