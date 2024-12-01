#!/usr/bin/env python3
import hashlib
from itertools import count

INPUT = 'uqwqemis'

def next_char(door_id, start=0):
    for idx in count(start):
        text = "{}{}".format(door_id, idx).encode()
        hashi = hashlib.md5(text).hexdigest()
        if hashi.startswith('00000'):
            return (hashi[5], idx)

def next_char2(door_id, start=0):
    for idx in count(start):
        text = "{}{}".format(door_id, idx).encode()
        hashi = hashlib.md5(text).hexdigest()
        if hashi.startswith('00000'):
            return (hashi[6], hashi[5], idx)

pwd = []
idx = -1
for i in range(8):
    c, idx = next_char(INPUT, idx+1)
    print("char: {}  idx: {}".format(c, idx))
    pwd.append(c)
print("DoorID: {}  Password: {}".format(INPUT, "".join(pwd)))


