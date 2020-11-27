#!/usr/bin/env python
from rle import *
import os

if __name__=='__main__':
    print('sup')
    uniform_orig = open('../uniform.bin','rb').read()
    random_orig = open('../random.bin','rb').read()

    random_cmp = compress(random_orig)
    uniform_cmp = compress(uniform_orig)

    open('random_cmp.bin','wb').write(random_cmp)
    open('uniform_cmp.bin','wb').write(uniform_cmp)

    open('random_dcmp.bin','wb').write(decompress(random_cmp))
    open('uniform_dcmp.bin','wb').write(decompress(uniform_cmp))
