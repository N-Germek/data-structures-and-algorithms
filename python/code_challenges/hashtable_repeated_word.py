from data_structures.hashtable import Hashtable


def first_repeated_word(phrase):
    # phrase = "Long, long ago, in a land far far away"
    words = ''
    hashtable = Hashtable()
    for word in phrase:
        lowercase = word.lower()
        if ord(lowercase) in range(ord('a'), ord('z') + 1):
            words += lowercase
        elif len(words):
            if hashtable.has(words):
                return words
            else:
                hashtable.set(words, None)
                words = ''
    if len(words) and hashtable.has(words):
        return words
    return None

    # words = phrase.split(" ")
    # print(words)
    # dict_counter = Counter(words)
    # for key in words:
    #     if dict_counter[key] > 1:
    #         print(key)
    #         return

