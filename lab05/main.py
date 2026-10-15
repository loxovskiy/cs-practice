
from tablestats import *

with open('events.csv', mode='r', encoding='utf-8', newline='') as f:

    print(read_rows(f))
