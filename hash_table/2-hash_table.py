# -*- coding: utf-8 -*-

hash_table = [[] for _ in range(10)]

def hashing_func(key):
    return key % len(hash_table)


def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    bucket = hash_table[hash_key]
    key_exist = False
    for i, (k, v) in enumerate(bucket):
        if k == key:
            # Resolve collision with chaining.
            # This allows multiple items to exist in the same bucket.
            key_exist = True
            bucket[i] = (key, value)
            break
    if not key_exist:
        bucket.append((key, value))

def search(hash_table, key):
    hash_key = hashing_func(key)
    bucket = hash_table[hash_key]
    for k, v in bucket:
        if k == key:
            return v

def delete(hash_table, key):
    hash_key = hashing_func(key)
    bucket = hash_table[hash_key]
    found = False
    for i, (k, v) in enumerate(bucket):
        if k == key:
            found = True
            del bucket[i]
            break
    if not found:
        print("Item with key `%s` not found." % key)

insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')

print(hash_table)
print(search(hash_table, 10))
delete(hash_table, 100)

delete(hash_table, 10)
print(hash_table)
