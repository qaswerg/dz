class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(10)]

    def insert(self, key, value):
        bucket = self.table[hash(key) % len(self.table)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        bucket = self.table[hash(key) % len(self.table)]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None
    
ht = HashTable()
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("orange", 3)
ht.insert("grape", 4)
ht.insert("apple", 5) 

print(ht.get("apple"))   
print(ht.get("banana"))  
print(ht.get("kiwi"))    
