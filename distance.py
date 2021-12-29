from abc import ABCMeta, abstractmethod
import numpy as np


class IDistanceAlgo(metaclass=ABCMeta):
    """Inherit from interface to crete Distance algorithm classes,
    and implement the abstract methods

    def rules : pass the rules of each class , or algorithm
    def distance : return the distance value of the algorithm
    """

    @abstractmethod
    def rules(self) -> None: pass

    @abstractmethod
    def distance(self) -> int: pass


class TwoStings(IDistanceAlgo):
    """Basically this is base class of comparing two strings algorithms.
    a : first string , b : second string . then trigger rules assertion.
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.rules()

    def rules(self):
        """make sure that both string are str
        else will raise assertion error
        :return: None
        """
        assert isinstance(self.a, str), "a must be instance of str"
        assert isinstance(self.b, str), "b must be instance of str"

    def distance(self): return 0


class Hamming(TwoStings):
    def rules(self):
        """Hamming distance is a metric for comparing two binary data strings.
        While comparing two binary strings of equal length .
        Make sure both are the same length
        ref: https://en.wikipedia.org/wiki/Hamming_distance
        """
        super(Hamming, self).rules()
        assert len(self.a) == len(self.b), "a and b must have same length"

    def distance(self):
        distance = 0
        for c1, c2 in zip(self.a, self.b):
            # if char not the same
            # increase the distance by one
            if c1 != c2:
                distance += 1
        return distance


class Levenshtein(TwoStings):

    def distance(self):
        # return self.__recursive(0, 0)
        return self.__dynamic()

    def __recursive(self, idx_a, idx_b):
        """ ------- NOT USED ------
        recursive implementation of the algo , not recommended to use
        only for compare the output of the dynamic implementation.
        :param idx_a: the current index of string a
        :param idx_b: the current index of string b
        for init idx_a=0,idx_b=0
        :return: int
        ref: https://en.wikipedia.org/wiki/Levenshtein_distance /Definition
        """
        if len(self.a[idx_a:]) == 0:
            return len(self.b[idx_b:])
        elif len(self.b[idx_b:]) == 0:
            return len(self.a[idx_a:])
        elif self.a[idx_a] == self.b[idx_b]:
            return self.__recursive(idx_a + 1, idx_b + 1)
        else:
            return 1 + min(self.__recursive(idx_a + 1, idx_b),
                           self.__recursive(idx_a, idx_b + 1),
                           self.__recursive(idx_a + 1, idx_b + 1))

    def __dynamic(self):
        """dynamic implementation of the algo, this more efficient than recursive
        :return: int , the distance value
        ref: https://en.wikipedia.org/wiki/Levenshtein_distance /Iterative with full matrix
        """
        if len(self.a) == 0:
            # if a is empty sting , return the length of b
            return len(self.b)
        if len(self.b) == 0:
            # if b is empty sting , return the length of a
            return len(self.b)

        # init of array
        size = (len(self.a), len(self.b))
        arr = np.zeros(size, dtype=int)
        # set the first row and first col to the max values that can contains
        # the max values is the indexes
        arr[:, 0] = [i for i in range(len(self.a))]
        arr[0, :] = [i for i in range(len(self.b))]

        for i in range(1, len(self.a)):
            for j in range(1, len(self.b)):
                # check if the char is the same
                # if yes set replace to 0 else 1
                # replace is like cost variable
                if self.a[i] != self.b[j]:
                    replace = 1
                else:
                    replace = 0
                # get the minimum value of :
                # 1 - previous row value with add char cost
                # 2 - previous col value with sub char cost
                # 3 - previous value with replace cost
                arr[i, j] = min(arr[i - 1, j] + 1,
                                arr[i, j - 1] + 1,
                                arr[i - 1, j - 1] + replace)
        # return the last value in the 2d array
        # which the most optimal value
        return arr[-1, -1]
