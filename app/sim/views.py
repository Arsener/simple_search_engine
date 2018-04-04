# -*- coding: utf-8 -*-
import jieba
from flask import render_template, redirect, url_for
from . import sim
from .forms import SimForm


@sim.route('/')
def index():
    return redirect(url_for('.sim'))


@sim.route('/sim', methods=['GET', 'POST'])
def sim():
    form = SimForm()
    if form.validate_on_submit():
		# 获取输入的两个句子并分词
        sentence1 = form.sentence1.data
        sentence2 = form.sentence2.data
        seg_list_1 = list(jieba.cut_for_search(sentence1, HMM=False))
        seg_list_2 = list(jieba.cut_for_search(sentence2, HMM=False))

        result_transvection_1 = transvection_1(seg_list_1, seg_list_2)
        result_transvection_2, result_cos, result_jaccard = similarity(seg_list_1, seg_list_2)
        # result_cos = cos(seg_list_1, seg_list_2)
        # result_jaccard = jaccard(seg_list_1, seg_list_2)
        return render_template('sim.html', form=form, result_cos=result_cos,
                               result_transvection_1=result_transvection_1,
                               result_transvection_2=result_transvection_2,
                               result_jaccard=result_jaccard)

    return render_template('sim.html', form=form)


# 计算内积（二值）
def transvection_1(seg_list_1, seg_list_2):
    seg_1 = set(seg_list_1)
    seg_2 = set(seg_list_2)

    count = 0.0
    for s in seg_1:
        if s in seg_2:
            count += 1.0

    return count


# 计算内积（加权）、余弦、Jaccard
def similarity(seg_list_1, seg_list_2):
    seg_1 = {}
    seg_2 = {}

    # 统计第一句话中每个词出现的数量
    for word in seg_list_1:
        try:
            seg_1[word] += 1.0
        except:
            seg_1[word] = 1.0

    # 统计第二句话中每个词出现的数量
    for word in seg_list_2:
        try:
            seg_2[word] += 1.0
        except:
            seg_2[word] = 1.0

    # 计算内积（加权）
    result_transvection_2 = 0.0
    # 计算向量模长
    cos_denominator_1 = 0.0
    cos_denominator_2 = 0.0
    for key in seg_1:
        try:
            result_transvection_2 += (seg_1[key] * seg_2[key])
        except:
            pass
        cos_denominator_1 += seg_1[key] ** 2

    for key in seg_2:
        cos_denominator_2 += seg_2[key] ** 2
	# 计算余弦
    result_cos = result_transvection_2 / (cos_denominator_1 * cos_denominator_2) ** 0.5
	# 计算Jaccard
    result_jaccard = result_transvection_2 / (cos_denominator_1 + cos_denominator_2 - result_transvection_2)
    return result_transvection_2, result_cos, result_jaccard


# 计算余弦
def cos(seg_list_1, seg_list_2):
    pass


# 计算Jaccard
def jaccard(seg_list_1, seg_list_2):
    pass
