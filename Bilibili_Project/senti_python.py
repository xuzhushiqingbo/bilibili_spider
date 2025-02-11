# Author : Троцкий

# 2019-05-16 08：40


import jieba

import numpy as np

import pymysql


# 打开词典文件，返回列表
def open_dict(Dict='hahah', path=r'/Users/apple/PycharmProjects/Bilibili_Project/'):
    path = path + '%s.txt' % Dict
    dictionary = open(path, 'r', encoding='utf-8')
    dict = []
    for word in dictionary:
        word = word.strip('\n')
        dict.append(word)
    return dict


def judgeodd(num):
    if (num % 2) == 0:
        return 'even'
    else:
        return 'odd'


deny_word = open_dict(Dict='否定词', path=r'/Users/apple/PycharmProjects/Bilibili_Project/')
posdict = open_dict(Dict='positive', path=r'/Users/apple/PycharmProjects/Bilibili_Project/')
negdict = open_dict(Dict='negative', path=r'/Users/apple/PycharmProjects/Bilibili_Project/')

degree_word = open_dict(Dict='程度级别词语', path=r'/Users/apple/PycharmProjects/Bilibili_Project/')
mostdict = degree_word[degree_word.index('extreme')+1: degree_word.index('very')]
# 权重4，即在情感词前乘以4
verydict = degree_word[degree_word.index('very')+1: degree_word.index('more')]
# 权重3
moredict = degree_word[degree_word.index('more')+1: degree_word.index('ish')]
# 权重2
ishdict = degree_word[degree_word.index('ish')+1: degree_word.index('last')]
# 权重0.5


def sentiment_score_list(dataset):
    seg_sentence = dataset.split('。')

    count1 = []
    count2 = []
    for sen in seg_sentence:
        segtmp = jieba.lcut(sen, cut_all=False)
        i = 0
        a = 0
        poscount = 0
        poscount2 = 0
        poscount3 = 0
        negcount = 0
        negcount2 = 0
        negcount3 = 0
        for word in segtmp:
            if word in posdict:  # 判断词语是否是情感词
                poscount += 1
                c = 0
                for w in segtmp[a:i]:  # 扫描情感词前的程度词
                    if w in mostdict:
                        poscount *= 4.0
                    elif w in verydict:
                        poscount *= 3.0
                    elif w in moredict:
                        poscount *= 2.0
                    elif w in ishdict:
                        poscount *= 0.5
                    elif w in deny_word:
                        c += 1
                if judgeodd(c) == 'odd':  # 扫描情感词前的否定词数
                    poscount *= -1.0
                    poscount2 += poscount
                    poscount = 0
                    poscount3 = poscount + poscount2 + poscount3
                    poscount2 = 0
                else:
                    poscount3 = poscount + poscount2 + poscount3
                    poscount = 0
                a = i + 1  # 情感词的位置变化

            elif word in negdict:
                negcount += 1
                d = 0
                for w in segtmp[a:i]:
                    if w in mostdict:
                        negcount *= 4.0
                    elif w in verydict:
                        negcount *= 3.0
                    elif w in moredict:
                        negcount *= 2.0
                    elif w in ishdict:
                        negcount *= 0.5
                    elif w in degree_word:
                        d += 1
                if judgeodd(d) == 'odd':
                    negcount *= -1.0
                    negcount2 += negcount
                    negcount = 0
                    negcount3 = negcount + negcount2 + negcount3
                    negcount2 = 0
                else:
                    negcount3 = negcount + negcount2 + negcount3
                    negcount = 0
                a = i + 1
            elif word == '！' or word == '!':
                for w2 in segtmp[::-1]:
                    if w2 in posdict or negdict:
                        poscount3 += 2
                        negcount3 += 2
                        break
            i += 1
            # 扫描词位置前移

            pos_count = 0
            neg_count = 0
            if poscount3 < 0 and negcount3 > 0:
                neg_count += negcount3 - poscount3
                pos_count = 0
            elif negcount3 < 0 and poscount3 > 0:
                pos_count = poscount3 - negcount3
                neg_count = 0
            elif poscount3 < 0 and negcount3 < 0:
                neg_count = -poscount3
                pos_count = -negcount3
            else:
                pos_count = poscount3
                neg_count = negcount3

            count1.append([pos_count, neg_count])
        count2.append(count1)
        count1 = []

    return count2


def sentiment_score(senti_score_list):
    score = []
    for review in senti_score_list:
        score_array = np.array(review)
        Pos = np.sum(score_array[:, 0])
        Neg = np.sum(score_array[:, 1])
        AvgPos = np.mean(score_array[:, 0])
        AvgPos = float('%.1f'%AvgPos)
        AvgNeg = np.mean(score_array[:, 1])
        AvgNeg = float('%.1f'%AvgNeg)
        StdPos = np.std(score_array[:, 0])
        StdPos = float('%.1f'%StdPos)
        StdNeg = np.std(score_array[:, 1])
        StdNeg = float('%.1f'%StdNeg)
        score.append([Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg])
    return score


if __name__ == "__main__":

    conn = pymysql.connect(user="root", password="root", port=3306, db="test", host="127.0.0.1", charset="utf8")
    cursor = conn.cursor()
    sql = "select comment from bilibili_comment"
    cursor.execute(sql)
    q = cursor.fetchall()
    baconFile = open('result.txt', 'w')
    for i in q:
        res = sentiment_score(sentiment_score_list(i[0]))[0]
        baconFile.write(str(res)+"\n")
    baconFile.close()


