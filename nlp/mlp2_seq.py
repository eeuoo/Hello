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

# 파일을 읽고 고정 길이의 배열 리턴하기
def file_to_ids(fname) :
    with open(fname, 'r') as f :
        text = f.read()
        return text_to_ids(text)

# 딕셔너리에 단어 모두 등록하기
def register_dic() :
    files = glob.glob(root_dir + '/*/*.wakati', recursive=True)
    for i in files :
        file_to_ids(i)

# 파일 내부의 단어 세기
def count_file_freq(fname) :
    cnt = [ 0 for n in range(word_dic['_MAX']) ] 
    with open(fname, 'r') as f :
        text = f.read().strip()
        ids = text_to_ids(text)
        for wid in ids :
            cnt[wid] += 1
    return cnt

# 카테고리마다 파일 읽어 들이기
def count_freq(limit = 0) :
    X = []
    Y = []
    max_words = word_dic['_MAX']
    