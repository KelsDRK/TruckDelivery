class HashTable:

    def __init__(self, initial_capacity=20):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # Inserts a new item into the hash table
    # Citing source: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
    def add(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:  # O(N) CPU time
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Lookup items in hash table
    def get(self, key):
        # Calculate the hash bucket index
        bucket_index = hash(key) % len(self.list)
        bucket_list = self.list[bucket_index]

        # Search for the key in the bucket list
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]  # Return the associated value if the key is found

        return None  # Return None if the key is not found  # no pair[0] matches key 0

    # Hash remove method - removes item from hash table
    def hash_remove(self, key):
        slot = hash(key) % len(self.list)
        destination = self.list[slot]

        # If the key is found in the hash table then remove the item
        if key in destination:
            destination.remove(key)

    def print(self):
        print('----Packages----')
        for item in self.map:
            if item is not None:
                print(str(item))








