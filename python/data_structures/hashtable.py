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
        if key is {key}:
            key.value = {key.value}
            print(new_index)

    # def get(self, key):
    #     return key.value
        # check if new key matches key in bucket index
        # if key[new_index] is temp_key.key:
        #     temp_key.value[new_index]

        # if {key} is new_key.key:



        # check = self.has(key)
        # if check is False:
        #     pass
            # location = self.bucket[new_key]
            # print(location)

        # else:
        #
        #     if key in self.bucket:

    # def get(self, key):
    #     if key in self.bucket:
    #         hashed_index = hash(key)
    #         return hashed_index

    def has(self, key):
        if key in self.bucket:
            return True
            print("true")
        else:
            return False

    #
    # def keys(self):
    #     if self.bucket:
    #         key_list = [hash]
    #         return key_list


if __name__ == '__main__':
    hashtable = Hashtable(10)
    test_hash = hashtable.hash("cat")
    hashtable.set("cat", 5)
    hashtable.set("dog", 7)
    hashtable.set("cat", 4)

    # print(hashtable.bucket[936])

