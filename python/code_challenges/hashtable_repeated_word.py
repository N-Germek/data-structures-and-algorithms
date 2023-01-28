from data_structures.hashtable import Hashtable


def first_repeated_word(phrase):
    words = ''
    hashtable = Hashtable()
    for word in phrase:
        lowercase = word.lower()
        if ord(lowercase) in range(ord('a'), ord('z')):
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

