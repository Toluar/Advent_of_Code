#!/usr/bin/env python3
import hashlib
from itertools import count

Data = 'yzbqklnj'

for i in count():
    S = (Data + str(i)).encode('ascii')
    if hashlib.md5(S).hexdigest()[:5] == '00000':
        print(i)
        break


