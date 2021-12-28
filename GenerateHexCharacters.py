#!/usr/bin/python
import sys
for x in range(1,256):
        sys.stdout.write ("0x" + '{:02x}'.format(x)+"\n")
