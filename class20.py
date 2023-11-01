"""
Logging: The main purpose is used to debug or get the information execution
- Critical: 50
- Error: 40
- warning: 30
- info: 20
- debug: 10

SYntax
------
import logging
logging.basicConfig()

M1:
--------
logging.basicConfig()# by default logging.WARNING
# it will display only warning messages

M2:
------------
If you need all
    - logging.DEBUG

M3:log file creation
------------------
logging.basicConfig(filename="logs.log",level=logging.DEBUG)
"""

import logging

# Logging.WARNING: by default it will be there
"""
logging.basicConfig()# logging.WARNING
# it will display only warning messages
#
logging.debug('The debug message is displaying')
logging.info('The info message is displaying')
logging.warning('The warning message is displaying')
logging.error('The error message is displaying')
logging.critical('The critical message is displaying')
"""
"""
# logging.DEBUG
logging.basicConfig(level=logging.DEBUG)
# it will display only warning messages
#
logging.debug('The debug message is displaying')
logging.info('The info message is displaying')
logging.warning('The warning message is displaying')
logging.error('The error message is displaying')
logging.critical('The critical message is displaying')
"""


# log file creation
logging.basicConfig(filename="log.log",level=logging.DEBUG,filemode="w")

def function(n):
    try:
        x = []
        logging.info("Code starts Execution")
        for i in range(n):
            logging.info(f"{i} value is ")
            x.append(i*i)
            logging.debug(f"{i*i} appended to x")
        logging.info(f"{x} x value")
        return x
    except Exception as error:
        logging.error(error)

# print(function(10))

def function2(n):
    try:
        x = []
        print("Code starts Execution")
        for i in range(n):
            print(f"{i} value is ")
            x.append(i*i)
            print(f"{i*i} appended to x")
        print(f"{x} x value")
        return x
    except Exception as error:
        print(error)

# print(function2(10))


