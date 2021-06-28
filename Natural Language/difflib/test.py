from difflib import SequenceMatcher
from typing import Mapping


# 相似度函数
def similar(a, b):
    # a: generated statment; b: raw statement
    # return the ratio of matching in sequence b.
    maching_blocks = SequenceMatcher(None, a, b).get_matching_blocks()
    match_len = 0
    for block in maching_blocks[:-1]:
        if block[-1] > 1:
            match_len += block[-1]
    return match_len / maching_blocks[-1][1]


def similar_ratio(a, b):
    # return similarity score for two strings
    return SequenceMatcher(None, a, b).ratio()


# def similar_test():
#     print(similar_ratio(synonyms_2, antonyms_2))
#     print(similar(synonyms_2, antonyms_2))
#     print(similar_ratio(synonyms_3, antonyms_3))
#     print(similar(synonyms_3, antonyms_3))

if __name__ == "__main__":
    while True:
        s1 = input('s1:')
        s2 = input('s2:')
        print(similar_ratio(s1, s2))