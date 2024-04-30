
class HashTable:
    # constructor
    def __init__(self, initial_capacity=20):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # inserting new values to hash table, using chaining
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # if key already in bucket:
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if key not found in bucket, insert at end of list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def getValue(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
       # print(f'Searching for key: {key} in bucket: {bucket}')
       # print(f"bucket contents: {bucket_list}")
        for pair in bucket_list:
            if key == pair[0]:
               # print(f'Found value: {pair[1]}')
                return pair[1]
       # raise KeyError(f'key {key} not found')


    # remove items from hash table
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove(kv[0], kv[1]) # if key is found, remove kv pair

