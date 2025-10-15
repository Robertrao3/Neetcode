class RandomizedSet(object):

    def __init__(self):
        self.map = {}
        self.data = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        
        self.map[val] = len(self.data)
        self.data.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.map:
            return False
        
        last_val = self.data[-1]
        index_to_remove = self.map[val]
        self.map[last_val] = index_to_remove
        self.data[index_to_remove] = last_val

        self.data[-1] = val

        self.data.pop()

        self.map.pop(val)
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data)