class Hashtable():
    def __init__(self, hashf=None):
        if hashf == None:
            self.hash_func = self.hashf
        else:
            self.hash_func = hashf
        self.n = 0
        self.min_size = 8
        self.keys = [None for _ in range(self.min_size)]
        self.values = [None for _ in range(self.min_size)]

    def __search_index(self, key):
        index = self.hash_func(key) % len(self.keys)
        for i in range(len(self.keys)):
            j = (index+i) % len(self.keys)
            if self.keys[j] == key:
                return j
            if self.keys[j] == None:
                return j

        # there is no free place left
        return len(self.keys)

    def contains(self, key):
        index = self.__search_index(key)
        return index < len(self.keys) and self.keys[index] == key

    def get_value(self, key):
        index = self.__search_index(key)
        if index < len(self.keys) and self.keys[index] == key:
            return self.values[index]
        else:
            None

    def set_value(self, key, value):
        index = self.__search_index(key)
        if index >= len(self.keys):
            return False

        self.keys[index] = key
        self.values[index] = value
        return True

    def insert(self, key, value):
        index = self.__search_index(key)
        while index >= len(self.keys):
            self.keys.append(None)
            self.values.append(None)

        if self.keys[index] == key:
            return False
        else:
            self.keys[index] = key
            self.values[index] = value
            self.n += 1
            if(self.__has_to_resize()):
                self.__resize()
            return True

    def size(self):
        return self.n

    def __has_to_resize(self):
        if self.n <= self.min_size:
            return False
        else:
            return self.n > 4 / 6 * len(self.keys) or self.n < 1 / 6 * len(self.keys)

    def __resize(self):
        m = self.n * 4  # 1 / 4 filled
        old_keys = self.keys
        old_values = self.values
        self.keys = [None for _ in range(m)]
        self.values = [None for _ in range(m)]
        for key, value in zip(old_keys, old_values):
            if key != None:
                self.insert(key, value)

    def delete(self, key):
        index = self.__search_index(key)
        if index < len(self.keys) and self.keys[index] == key:
            self.keys[index] = None
            self.values[index] = None
            i = 1
            while(self.keys[index+i] != None):
                next_key = self.keys[index+i]
                next_value = self.values[index+i]
                self.keys[index+i] = None
                self.values[index+i] = None
                self.insert(next_key, next_value)
                i += 1
                if(self.__has_to_resize()):
                    self.__resize()
            return True
        else:
            return False

    def insert_all(self, keys, values):
        if len(keys) == len(values):
            hash_keys = [None for i in range(2*len(keys) + 8)]
            hash_values = [None for i in range(2*len(values) + 8)]
            hashtable = (hash_keys, hash_values)
            for key, value in zip(keys, values):
                self.insert(key, value)
            return hashtable
        return ([], [])

    def collisions(self):
        collisions = 0
        for index, key in enumerate(self.keys):
            if key != None:
                j = self.hash_func(key) % len(self.keys)
                collisions += abs(j-index)
        return collisions

    def hashf(self, name):
        hash_value = 0
        prime = 83
        m = 8
        for i in range(min(m, len(name))):
            hash_value *= prime
            hash_value += ord(name[i])
        return hash_value


def simple_test():
    keys = ['0', '1', '2']
    values = ['Berta', 'Hans', 'Thomas']

    hashtable = Hashtable()
    hashtable.insert_all(keys, values)

    print(hashtable.get_value('1'))
    hashtable.set_value('1', 'Peter')
    print(hashtable.get_value('1'))
    print(hashtable.insert('2', 'Anna'))
    print(hashtable.get_value('2'))
    print(hashtable.insert('3', 'Anna'))
    print(hashtable.get_value('3'))


def insert_and_delete_test():
    n = 1000
    # intentionally bad hash function!
    hashtable = Hashtable(lambda i: int(i) % 100)
    for i in range(n):
        hashtable.insert(str(i), i)

    for i in range(0, n, 10):
        hashtable.delete(str(i))

    print(all([hashtable.get_value(str(i)) ==
          i for i in range(n) if i % 10 != 0]))


if __name__ == "__main__":
    simple_test()
    insert_and_delete_test()
