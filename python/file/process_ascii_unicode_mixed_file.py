# -*- coding:utf-8 -*-

import os
import os.path as osp
import sys
import codecs

# How to make directories (mkdir) with ascii-unicode mixed name in Python2?
# Here is a solution (tested on Windows 7, Pycharm 2016.3 and Ubuntu 16.04):

sys.stdin = codecs.getwriter('utf-8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

filename = 'ascii_unicode_mixed.txt'

if __name__ == '__main__':
    target_file = open(filename, 'r')
    target_lines = [line.rstrip('\n') for line in target_file]
    target_file.close()

    for idx, line in enumerate(target_lines):
        items = line.split(',')
        s0 = items[0]
        s1 = items[1]
        s2 = items[2]
        print s0.decode('utf-8')
        print s1.decode('utf-8')
        print s2.decode('utf-8')

        if osp.isdir(s1.decode('utf-8')) == False:
            os.mkdir(s1.decode('utf-8'))
