# -*- coding: utf-8 -*-
import os

a = set()
a.add('a')
print(a)

for i in range(1, 2):
    with open(os.path.dirname(__file__) + '/words_statistics/' + str(i) + '.txt',
              'r') as f:
        while True:
            words = f.readline()
            if words:
                print words.strip()
            else:
                break
