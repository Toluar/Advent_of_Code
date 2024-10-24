#!/usr/bin/env python3

import json
import re


with open('Input.12') as f:
    s = f.read()

print(sum(map(int, re.findall(r'-?\d+', s))))
