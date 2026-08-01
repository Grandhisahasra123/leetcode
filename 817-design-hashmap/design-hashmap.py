class MyHashMap:
    def __init__(self):
        self.lst=[-1]*(10**6+1)
    def put(self, key: int, value: int) -> None:
        self.lst[key]=value
    def get(self, key: int) -> int:
        if self.lst[key]!=-1:
            return self.lst[key]
        else:
            return -1
    def remove(self, key: int) -> None:
        if self.lst[key]!=-1:
            self.lst[key]=-1
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)