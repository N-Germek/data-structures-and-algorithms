class Hashtable:
    """
    set (takes in key and value)
        if bucket is empty
            hash key and value
            append key and value to bucket
        else if key is already in bucket
            overwrite new value of key to key value in bucket


    """

    def __init__(self, size=1024):
        self.size = size
        self.bucket = size * [None]
        # print(self.bucket)

    def hash(self, key):
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)

        primed = hash_sum * 3
        index = primed % self.size
        return index

    def set(self, key, value):
        new_index = self.hash(key)
        # print(new_index)
        # print(self.bucket)
        self.bucket[new_index] = {key, value}
        # print(self.bucket)
        # print(new_index)
        print(key, value)
        # for keys in new_index[key]:
        #     if keys is {key}:
        #         keys.value = {key.value}



    def get(self, key):
        pass

    def get(self, key):
        pass

    def has(self, key):
        pass

    def keys(self):
        pass


if __name__ == '__main__':
    hashtable = Hashtable(10)
    test_hash = hashtable.hash("cat")
    hashtable.set("cat", 5)
    hashtable.set("dog", 7)
    hashtable.set("cat", 4)

    # print(hashtable.bucket[936])

