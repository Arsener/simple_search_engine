# -*- coding: utf-8 -*-
import os, jieba, math
from flask import render_template, redirect, request, url_for, flash, current_app
from . import sjet
from .forms import SjetForm

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


@sjet.route('/')
def index():
    return redirect(url_for('.sjet'))


# 展示新闻内容
@sjet.route('/news_page/<int:id>', methods=['GET'])
def news_page(id):
    BASE_DIR = os.path.dirname(__file__)
    file_dir = os.path.join(BASE_DIR, 'news/')
    with open(file_dir + str(id) + '.txt', 'r') as f:
        title = f.readline()
        content = []
        while True:
            c = f.readline()
            if c:
                content.append(c)
            else:
                break

    return render_template('news.html', title=title, content=content)


@sjet.route('/sjet', methods=['GET', 'POST'])
def sjet():
    form = SjetForm()
    if form.validate_on_submit():
        query = form.query.data
        BASE_DIR = os.path.dirname(__file__)
        file_dir = os.path.join(BASE_DIR, 'news/')
        '''
        results[i] = [index, title, content, result]
        words_count[i] = {'word1': count1,
                    'word2': count2,
                    ......
                    
                    'word_n': count_n}
        '''
        results = []  # 保存每篇文章信息以及与query的相似度(result)
        words_count = []  # 保存每篇文章每个词的tf值

		# 计算语料库中每个文章没歌词的tf值
        for i in range(1, 417):
            with open(file_dir + str(i) + '.txt', 'r') as f:
                news = []
                news.append(i)
                title = f.readline()
                news.append(title.strip())

                content = ''
                while True:
                    words = f.readline()
                    if words:
                        content += words.strip()
                    else:
                        break

                seg_list = jieba.cut_for_search(title + content, HMM=False)
                wc = {}
                seg_l = list(seg_list)
                for word in seg_l:
                    wc[word] = (wc.get(word, 0.0) + 1.0)

                for key in wc:
                    wc[key] /= (len(seg_l) * 1.0)

                words_count.append(wc)
                news.append(content)
                results.append(news)

        # 计算query每个词的tfidf
        seg_list = jieba.cut_for_search(query, HMM=False)
        words_in_query = list(seg_list)
		
		# 对query中每个词，计算在query中出现的次数
        tfidf_in_query = {}
        for word in words_in_query:
            word = word.strip()
            if len(word) > 0:
                tfidf_in_query[word] = tfidf_in_query.get(word, 0.0) + 1.0
		

        a_pow = 0.0  # query向量模长的平方
        # 计算语料库中有多少文章出现了query中的这个词， 最后直接计算这个词的tfidf
        for key in tfidf_in_query:
            news_count = 1.0
            for i in range(416):
                if words_count[i].get(key, -1) != -1:
                    news_count += 1.0
            tfidf_in_query[key] = tfidf_in_query[key] / len(words_in_query)\
                                    * math.log10(416.0 / news_count)
            a_pow += tfidf_in_query[key] ** 2

        for i in range(416):
            ab = 0.0  # 向量内积
            b_pow = 0.0  # 文章向量模长的平方
			# 计算文章每个词的tfidf
            for key in words_count[i]:
                sum = 1.0
                for j in range(416):
                    if words_count[j].get(key, -1) != -1:
                        sum += 1.0
                words_count[i][key] *= math.log10(416 / sum)
                ab += tfidf_in_query.get(key, 0.0) * words_count[i][key]
                b_pow += words_count[i][key] ** 2

            tfidf = ab / (a_pow * b_pow) ** 0.5
            results[i].append(tfidf)
		
		# 将文章按照相似度从大到小排序
        results = sorted(results, key=lambda news: news[-1], reverse=True)

        return render_template('sjet.html', form=form, results=results)

    return render_template('sjet.html', form=form)