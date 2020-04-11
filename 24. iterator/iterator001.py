class MyIterator:

    def __init__(self, *val):
        self._value = val
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count < len(self._value):
            res = self._value[self._count]
            self._count += 1
            return res
        else:
            raise StopIteration()
        
obj = MyIterator("one", "two", "three", "four", "five")
for val in obj:
    print(val)
