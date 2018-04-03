# -*- coding:utf-8 -*-
import jieba

for i in range(1, 417):
    with open('./app/sjet/news/' + str(i) + '.txt', 'r') as f:
        data = f.read()

    seg_list = jieba.cut_for_search(data, HMM=False)
    # print(list(seg_list))

    with open('./app/tfidf/words_statistics/' + str(i) + '.txt', 'a') as f:
        for l in set(seg_list):
            f.write(l.encode('utf-8') + '\n')