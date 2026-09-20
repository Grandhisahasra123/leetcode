class MyHashSet:

    def __init__(self):
        self.d=[0]*1000001
    def add(self, key: int) -> None:
        if self.d[key]==0:
            self.d[key]=1
    def remove(self, key: int) -> None:
       if self.d[key]==1:
            self.d[key]=0
    def contains(self, key: int) -> bool:
        if self.d[key]==1:
            return True
        else:
            return False
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)