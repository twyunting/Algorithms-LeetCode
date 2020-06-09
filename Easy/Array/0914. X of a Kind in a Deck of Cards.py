class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        #from fractions import gcd
        count = collections.Counter(deck).values()
        
        return reduce(gcd, count) >= 2
    
"""
reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

gcd = 最大公因數
"""

