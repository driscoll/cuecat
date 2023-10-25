#!/usr/bin/python3
#
# Decode the output of a CueCat scanner
# 
# Rewritten for Python 3 
# based on code found on the web, e.g.
# https://linas.org/banned/cuecat/cc.index.html
# http://www.beau.lib.la.us/~jmorris/linux/cuecat/
#
# Original author $UNKNOWN (maybe you, @inklesspen?)
#
# This code is STILL public domain code.

import sys

seq = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-'

def decode(s):
    s = [seq.find(x) for x in s]
    l = len(s) % 4
    if l:
        if l == 1: raise ValueError()
        l = 4-l
        s.extend([0]*l)
    r = ''
    while s:
        n = ((s[0] << 6 | s[1]) << 6 | s[2]) << 6 | s[3]
        r = r + chr((n >> 16) ^ 67) + chr((n >> 8 & 255) ^ 67) + chr((n & 255) ^ 67)
        s = s[4:]
    return l and r[:-l] or r

def cc(s):
    return " ".join(['%02d' % (ord(x) ^ 0x20) for x in s])

def do(s):
    s = [x for x in s.split('.') if x and x[0] > ' ']
    s = list(map(decode, s))
    if len(s) == 3:
        print('Serial: '+s[0])
        print('Type: '+s[1])
        if s[1] == 'CC!':
            print('Code: C 01 '+cc(s[2]))
        else:
            print('Code: '+s[2])
    else:
        for x in s: print(x)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        do(sys.argv[1])
    else:
        while 1:
            try:
                s = input('Scan/Enter> ')
            except EOFError:
                break
            if not s: break
            try:
                do(s)
            except ValueError:
                print('Invalid input')
