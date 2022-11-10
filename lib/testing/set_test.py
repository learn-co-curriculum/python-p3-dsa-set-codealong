#!/usr/bin/env python3
from MySet import MySet

class TestSet:

    def test_init(self):
        '''Test __init__ set with list'''
        test_set = MySet([1,2,3,4])
        set_list = [1,2,3,4]
        for num in set_list:
            assert(num in test_set.dictionary)

    def test_add(self):
        '''Test add() to set'''
        test_set = MySet([1,2,3,4])
        test_set.add(5)
        set_list = [1,2,3,4,5]
        for num in set_list:
            assert(num in test_set.dictionary)

    def test_delete(self):
        '''Test delete()'''
        test_set = MySet([1,2,3,4])
        test_set.delete(2)
        set_list = [1,3,4]
        for num in set_list:
            assert(num in test_set.dictionary)

    def test_has(self):
        '''Test has()'''
        test_set = MySet([1,2,3,4])
        assert(test_set.has(1) == True)
        assert(test_set.has(7) == False)

    def test_size(self):
        '''Test size()'''
        test_set = MySet([1,2,3,4])
        assert(len(test_set.dictionary) == 4)



# Bonus test
"""
    def test_clear(self):
        '''Test clearing set'''
        test_set = MySet([1,2,3,4])
        test_set.clear()
        assert(len(test_set.dictionary) == 0)

    def test_str(self):
        '''Test __str__()'''
        test_set = MySet([1,2,3,4])
        assert(str(test_set) == 'MySet: {1,2,3,4}')
"""