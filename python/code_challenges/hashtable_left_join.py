from data_structures.hashtable import Hashtable


def left_join(hash_one, hash_two, key, value):
    new_list = []

    while hash_one is not None:
        for Hashtable._buckets in hash_one:
            if hash_one.has(key) != hash_two.has(key):
                no_match = hash_two[0](key, None)
                new_list.append(hash_one.set(key, value, no_match))
            elif hash_one(key) == hash_two(key):
                new_list.append(hash_one(key, value))
                new_list.append(hash_two(value))
    return new_list


if __name__ == '__main__':
    hash_test_one = Hashtable(10)
    hash_test_two = Hashtable(11)
    hash_test_two.set("diligent", "employed")
    hash_test_two.set("font", "enamored")
    hash_test_two.set("outfit", "garb")
    hash_test_one.set("diligent", "idle")
    hash_test_one.set("font", "averse")
    hash_test_one.set("flow", "jam")
