import random

class RandomizedSet:
    def __init__(self):
        self.items = set()

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        self.items.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.items:
            self.items.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        random_val = random.choice(list(self.items))
        return random_val


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()