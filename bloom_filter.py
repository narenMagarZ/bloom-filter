import mmh3

class BloomFilter:
    def __init__(self, k: int, size: int) -> None:
        self.__size = size
        self.__k = k
        self.__arr = [0] * size
    
    def add(self, key: str):
        for i in range(self.__k):
            val = mmh3.hash(key, i)
            hash = val % self.__size
            self.__arr[hash] = 1

    def test(self):
        return self.__arr
    
    def isExists(self, key: str):
        for i in range(self.__k):
            val = mmh3.hash(key, i)
            hash = val % self.__size
            if self.__arr[hash] == 0:
                return False
        return True





filter = BloomFilter(3, 100)

filter.add("narenmagarz")
print(filter.isExists("narenmagarz"), "narenmagarz check")
print(filter.isExists("narenmagar"), "narenmagar check")
filter.add("narenmagar")
print(filter.isExists("narenmagar"), "narenmagar check")



    