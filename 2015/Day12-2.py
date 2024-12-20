#!/usr/bin/env python3

import json
import re


with open('Input.12') as f:
    s = f.read()

def get_sum(d):
    if isinstance(d, int):
        return d
    elif isinstance(d, str):
        return 0
    elif isinstance(d, list):
        return sum(get_sum(x) for x in d)
    else:
        return 0 if any(x == 'red' for x in d.values()) else sum(get_sum(x) for x in d.values())


d = json.loads(s)
print(get_sum(d))

