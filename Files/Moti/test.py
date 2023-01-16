import time
from termcolor import colored, cprint
import os, sys


def delay_print(s):
    for c in s:
        sys.stdout.flush()
        print(c)
        time.sleep(0.15)
while 1:
 delay_print(colored('hello world','red', attrs=['reverse', 'blink']))
 