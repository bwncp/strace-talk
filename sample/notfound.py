#!/usr/bin/python3

import sys

f = open('somefile', 'rb')




bytes = f.read(5)

f.close()

print(len(bytes), 'bytes read')
