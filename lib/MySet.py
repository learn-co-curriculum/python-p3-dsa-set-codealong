class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'

    def add(self, value):
        self.dictionary[value] = True # Add a value as a key on the hash
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()

# new_set = MySet([1,2,3,4,5,5,6,7,-1])
# new_set.add(10)
# print(new_set)
# new_set.delete(2)
# print(new_set.size())
# new_set.delete(10)
# new_set.delete(1)
# print(new_set.has(-1))
# print(new_set)
