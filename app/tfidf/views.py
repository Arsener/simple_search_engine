# -*- coding: utf-8 -*-
import os, math
import jieba
from flask import render_template, flash
from . import tfidf
from .forms import FileForm
from flask_uploads import UploadSet, TEXT


@tfidf.route('/', methods=['GET', 'POST'])
def index():
    form = FileForm()
    text = UploadSet('text', TEXT)
    if form.validate_on_submit():
        filename = text.save(form.text_file.data)
        flash(u'文件上传成功')
        BASE_DIR = os.path.dirname(__file__)
        file_dir = os.path.join(BASE_DIR, 'upload_files/')
        result = tfidf_calc(file_dir, filename)
        return render_template('tfidf.html', form=form, result=result)

    return render_template('tfidf.html', form=form)


def tfidf_calc(file_dir, filename):
    with open(file_dir + filename, 'r') as f:
        data = f.read()
    seg_list = jieba.cut_for_search(data, HMM=False)

    word_count = {}  # 计算上传的文本中每个词语的数量
    text_count = {}  # 计算每个词语出现在语料库的多少文本中
    tfidf_result = {}  # 计算结果
    word_sum = 0.0  # 计算文本的总的词数量
    text_sum = 416.0  # 语料库中总的文本数量
    for word in list(seg_list):
        try:
            word_count[word] += 1.0
        except:
            word_count[word] = 1.0
            text_count[word] = 1.0
        word_sum += 1.0

    for i in range(1, 417):
        word_set = set()  # 语料库每个文本的词语集合
        with open(os.path.dirname(__file__) + '/words_statistics/' + str(i) + '.txt',
                  'r') as f:
            while True:
                words = f.readline()
                if words:
                    word_set.add(words.strip())
                else:
                    break

        for key in text_count:
            if key in word_set:
                text_count[key] += 1.0

    # 解决编码问题
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    import datetime
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    result = []
    # 计算上传文本每个词的TFIDF并写入文件
    with open(os.path.dirname(__file__) + '/tfidf_result/' + str(nowTime)
                      + '_' + filename, 'a') as f:
        for key in word_count:
            tfidf_result[key] = (word_count[key] / word_sum) *\
                                math.log(text_sum / text_count[key])
            re = key + '---' + str(tfidf_result[key])
            f.write(re + '\n')
            result.append(re)

    return result


