class Hashtable:
    """
    set (takes in key and value)
        if bucket is empty
            hash key and value
            append key and value to bucket
        else if key is already in bucket
            overwrite new value of key to key value in bucket

    get(take in key)
         return the value associated with that key

    has(take in key)
        iterates through list
            if key in list
            return boolean True

    keys(takes in self)
        iterates through list
            if keys exist in list
                return a list of all keys

    hash() - Should take in the argument of the key and return the index of the collection of that key.
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]
        # print(self.bucket)

    def hash(self, key):
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)

        primed = hash_sum * 11
        index = primed % self.size
        return index

    def set(self, key, value):
        new_index = self.hash(key)
        if self._buckets[new_index] is None:
            self._buckets[new_index] = [[key, value]]
        else:
            for item in self._buckets[new_index]:
                if item[0] == key:
                    item[1] = value
                    return
            self._buckets[new_index].append([key, value])
        print(key, value)

    def get(self, key):
        check_index = self.hash(key)
        if self._buckets[check_index] is not None:
            for item in self._buckets[check_index]:
                if item[0] == key:
                    return item[1]

    def has(self, key):
        check_key_value = self.hash(key)
        if self._buckets[check_key_value] is not None:
            for item in self._buckets[check_key_value]:
                if item[0] == key:
                    return True
        else:
            return False

    def keys(self):
        list_of_keys = []
        for main_bucket in self._buckets:
            if main_bucket is not None:
                for item in main_bucket:
                    list_of_keys.append(item[0])
        return list_of_keys


if __name__ == '__main__':
    hashtable = Hashtable(10)
    test_hash = hashtable.hash("cat")
    hashtable.set("cat", 5)
    hashtable.set("dog", 7)
    hashtable.set("cat", 4)
