import os, glob, json

root_dir = './newstext'
dic_file = root_dir + '/word_dic.json'
data_file = root_dir + '/data.json'
data_file_min = root_dir + '/data_mini.json'

# 어구를 자르고 ID로 변환하기
word_dic = { '_MAX' : 0 }
def text_to_ids(text) :
    text = text.strip()
    words = text.split(" ")
    result = []
    for n in words :
        n = n.strip()
        if n == "" :
            continue
        if not n in word_dic :
            wid = word_dic[n] = word_dic['_MAX']
            word_dic['_MAX'] += 1
            print(wid, n)
        else :
            wid = word_dic[n]
        result.append(wid)
    return result
    