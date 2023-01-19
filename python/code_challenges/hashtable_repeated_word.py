# from data_structures.hashtable import Hashtable
from collections import Counter


def first_repeated_word(phrase):
    phrase = "Long, long ago, in a land far far away"
    words = phrase.split(" ")
    print(words)
    dict_counter = Counter(words)
    for key in words:
        if dict_counter[key] > 1:
            print(key)
            return
