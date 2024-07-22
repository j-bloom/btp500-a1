#    main author(s):
#    main reviewer(s):

class HashTable:

    # you cannot change the function prototypes below.  other than that
    # how you implement the class is your choice as long as it is a hash table

    def __init__(self, cap=32):
        self.cap = cap
        self.hash_table = [None] * self.cap
        self.count = 0
        self.table_load_factor = 0.7
        self.status = ['empty'] * cap 

    def resize_and_rehash(self, hash_index):
        if self.table_load_factor <= self.count/self.cap:
            new_cap = self.cap * 2
            new_hash_table = [None] * new_cap
            new_status_array = ['empty'] * new_cap

        # rehash all existing key-value pairs into the new table
            for entry in self.hash_table:
                if entry is not None:
                    key, value = entry
                    hash_value = hash(key)
                    index = hash_value % new_cap
                    while new_hash_table[index] is not None:
                        index += 1
                        if index >= new_cap:
                            index = 0
                    new_hash_table[index] = key, value
                    new_status_array[index] = 'occupied'

            self.hash_table = new_hash_table
            self.cap = new_cap
            self.status = new_status_array

    def insert(self,key, value):
        if key in self.hash_table:
            return False

        self.count = self.count +1
        hash_value = hash(key)
        hash_index = hash_value % self.cap

        if self.hash_table[hash_index] == None:
            self.hash_table[hash_index] = key, value
            self.status[hash_index] = 'occupied'
            # if loadfactor of 0.7 is reached, resize list
            # after resize rehash elements in array
            self.resize_and_rehash(hash_index)
            return True

        curkey, curvalue = self.hash_table[hash_index]

        if curkey == key:
            self.count -= 1
            return False
        start = hash_index - 1
        hash_index += 1
        if hash_index >= self.cap:
            hash_index = 0

        while hash_index != start:
            if self.hash_table[hash_index] != None:
                curkey, curvalue = self.hash_table[hash_index]

                if curkey == key:
                    self.count -= 1
                    return False
            else:
                self.hash_table[hash_index] = key, value
                self.status[hash_index] = 'occupied'
                self.resize_and_rehash(hash_index)
                return True
            if hash_index != self.cap-1:
                hash_index += 1
            else:
                hash_index = 0

        self.count -= 1
        return False

    def modify(self, key, value):
        
        index_hash = hash(key)
        index = index_hash % self.cap
        
        while self.hash_table[index] is not None:
            existing_key, modifying_value = self.hash_table[index]
            # update new value
            modifying_value = value
            
            if existing_key == key:
                # if key found update table with new value
                self.hash_table[index] = existing_key, modifying_value
                return True  

            # linear probing: move to the next slot (wrap around)
            index += 1
            if index >= self.cap:
                index = 0
            
        if self.hash_table[index] is None:
            return False

    
    def remove(self, key):
        index = hash(key) % self.cap
        initial_index = index

        for _ in range(self.cap):
            if self.status[index] == 'empty':
                return False  # Key not found

            if self.status[index] == 'occupied' and self.hash_table[index][0] == key:
                self.hash_table[index] = [None, None]
                self.status[index] = 'deleted'
                self.count -= 1
                return True

            index = (index + 1) % self.cap

        return False  # If we've examined all slots and didn't find the key
        
    def search(self, key):
        index_hash = hash(key)
        index = index_hash % self.cap
        initial_index = index
        while self.hash_table[index] is not None:
            existing_key, existing_value = self.hash_table[index]
            if existing_key == key:
                return existing_value  # key found, return the associated value

            # linear probing: move to the next slot (wrap around)
            index += 1
            if index >= self.cap:
                index = 0

            # search current cluster until next empty index
            if index is None:
                return None

        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.count


############### Helper Functions ###############

    def find_cluster_size(self, index):
        current_cluster_size = 0
        start_of_array = -1
        
        while self.hash_table[index] is not None:
            current_cluster_size += 1
            index += 1
            start_of_array = self.end_of_table(index)
            if start_of_array == 0 and self.hash_table[start_of_array] is not None:
                current_cluster_size += 1
                index += 1
        return current_cluster_size

    def hashed_index(self, index):
        index_hash = hash(index)
        return index_hash % self.cap

    def is_between(self, key, start, end):
        current_index = start
        while current_index <= end:
            current_index += 1
        self.end_of_table(current_index)
        
        
    def end_of_table(self, index):
        if index >= self.cap:
            index = 0
        return index
