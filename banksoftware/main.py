import re
# 这里以符号“#”表示文法中的空,非终结符号为大写字母，终结符为小写字母
def Type_judge(sentence, vn, vt):
    vn = r'[A-Z]'
    Type = 0
    left, right = sentence.split('->')
    if len(re.findall(vn, left)) != 0:
        if len(left) <= len(right):
            Type = 1
            if len(left) == 1:
                Type = 2
                if len(right) == 1:
                    if right in vt:
                        Type = 3
                elif len(right) == 2:
                    if right[0] in vn and right[1] in vt:
                        Type = 4   # 左线性
                    elif right[1] in vn and right[0] in vt:
                        Type = 5   # 右线性
    return Type

# 读文本文件
with open('test.txt', 'r') as r:
    sentences = [line.rstrip('\n') for line in r.readlines()]

Vn_form = r'[A-Z]'
Vt_form = r'[a-z]'
types = []
Vn = []
Vt = ['#']
#获取四元组
S = re.findall(Vn_form, sentences[0])
P = [such for such in sentences]

for such in sentences:
    Vn.extend(re.findall(Vn_form, such))
    Vt.extend(re.findall(Vt_form, such))
    temp = Type_judge(such, Vn, Vt)
    types.append(temp)
Vt.remove('#')
Vn = list(set(Vn))  # 去重
Vt = list(set(Vt))  # 去重

types = [str(r) for r in types]
types = ' '.join(types)

#判断是否为3型文法
if '4' in types and '5' in types:
    types = types.replace('4', '2').replace('5', '2')
else:
    types = types.replace('4', '3').replace('5', '3')
types = types.split(' ')

# 获得文法类型
types = [int(r) for r in types]
type_result = min(types)

#显示文法类型及四元组
print("该文法为{}型文法".format(type_result))
print("该文法的四元组形式为G ={",Vn,Vt,P,S,"}")
