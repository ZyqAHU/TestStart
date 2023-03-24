# -*- codeing = utf-8 -*-
# @Time : 2022/4/8 21:17
# @Author : ahu_zyq
# @File : wordcloudtest.py
# @softwawre : PyCharm
import numpy as np
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import  Image
import sqlite3



text =open(r"D:\pycharm\flask_base\result.txt", "r", encoding='utf-8').read() #准备词云所需的文字

#分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))
# print(string)

x, y = np.ogrid[:300, :300]

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 1000 * mask.astype(int)

# img = Image.open('apple-touch-icon.png')
# img_array = np.array(img)   #将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask = mask,
    font_path = "msyh.ttc"
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')

plt.show()
