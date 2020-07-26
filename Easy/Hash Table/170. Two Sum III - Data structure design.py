class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.d:
            self.d[number] += 1
        else:
            self.d[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in self.d.keys():
            comple = value - i
            if i != comple:
                if comple in self.d:
                    return True
            elif self.d[i] > 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


# Second Method

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.arr.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        d = {}
        for i in self.arr:
            if i in d:
                return True
            else:
                d[value-i] = i
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)



