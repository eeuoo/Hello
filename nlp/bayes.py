import math, sys
from konlpy.tag import Twitter

class BayesianFilter :
    '''베이지안 필터'''
    def __init__(self) :
        self.words = set()   # 출현한 단어 기록
        self.word_dict = {}  # 카테고리마다의 출현 횟수 기록
        self.category_dict = {}  # 카테고리 출현 횟수 기록

    
    # 형태소 분석하기
    def split(self, text) :
        results = []
        twitter = Twitter()

    # 단어의 기본형 사용
    malist = twitter.pos(text, norm = True, stem = True )
    for word in malist :
        # 어미/조사/구두점 등은 대상에서 제외
        if not word[1] in ['Josa', 'Eomi', 'Punctuation'] :
            results.append(word[0])
    return results

    # 단어와 카테고리의 출현 횟수 세기
    def inc_word(self, word, category) :
        # 단어를 카테고리에 추가하기
        if not category in self.word_dict :
            self.word_dict[category] = {}
        if not word in self.word_dict[category] :
            self.word_dict[category][word] = 0
        self.word_dict[category][word] += 1
        self.words.add(word)

    


