class HashTable:

    def __init__(self, size=10):
        self.hash_table = [[] for _ in range(size)]

    def hashing_func(self, key):
        # Naive implementation.
        return key % len(self.hash_table)

    def insert(self, key, value):
        hash_key = self.hashing_func(key)
        bucket = self.hash_table[hash_key]
        key_exist = False
        for i, (k, v) in enumerate(bucket):
            if k == key:
                key_exist = True
                bucket[i] = (key, value)
                break
        if not key_exist:
            bucket.append((key, value))

    def get(self, key):
        hash_key = self.hashing_func(key)
        bucket = self.hash_table[hash_key]
        for (k, v) in bucket:
            if k == key:
                return v

    def delete(self, key):
        hash_key = self.hashing_func(key)
        bucket = self.hash_table[hash_key]
        found = False
        for i, (k, v) in enumerate(bucket):
            if k == key:
                found = True
                del bucket[i]
                break
        if not found:
            print('Key `%s` not found' % key)


h = HashTable(size=11)

h.insert(0, 'Hello')
h.insert(5, 'Yellow')
h.insert(10, 'Goodbye')

print(h.hash_table)
print(h.get(5))

h.delete(50)
h.delete(10)
print(h.hash_table)
