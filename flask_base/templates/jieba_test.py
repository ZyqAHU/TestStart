# -*- codeing = utf-8 -*-
# @Time : 2022/4/12 20:11
# @Author : ahu_zyq
# @File : jieba_test.py
# @softwawre : PyCharm
import jieba
import numpy as np


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist(r'D:\pycharm\flask_douban\hit_stopwords.txt')
    # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


file1 = r"D:\pycharm\flask_douban\word_data.txt"
inputs = open(file1, 'r', encoding='utf-8')
# 读取路径与待分词文档位置一致
outputs = open(r'D:\pycharm\flask_douban\result.txt', 'w', encoding='utf-8')
# 写入路径与分词后写入文档的位置
for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()
