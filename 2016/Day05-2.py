#!/usr/bin/env python3
import hashlib
from itertools import count

INPUT = 'uqwqemis'
VALID_POS = '01234567'

def next_char(door_id, start=0):
    for idx in count(start):
        text = "{}{}".format(door_id, idx).encode()
        hashi = hashlib.md5(text).hexdigest()
        if hashi.startswith('00000'):
            return (hashi[6], hashi[5], idx)

pwd = [' '] * 8
idx = -1
while ' ' in pwd:
    c, pos, idx = next_char(INPUT, idx+1)
    print("char: {}  pos: {}  idx: {}".format(c, pos, idx))
    if pos in VALID_POS and pwd[int(pos)] == ' ':
        pwd[int(pos)] = c
    else:
        print("-- INVALID")
print("DoorID: {}  Password: {}".format(INPUT, "".join(pwd)))

