class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        
        count, temp_sum, target = 0, 0, sum(A)//3
        
        for i in A:
            temp_sum += i
            if temp_sum == target:
                count += 1
                temp_sum = 0
                
        return count >= 3
    
            
        """
        
        Python 主要的算术运算符与C/C++类似。+, -, *, /, //, **, ~, %
        分别表示加法或者取正、减法或者取负、乘法、除法、整除、乘方、取补、取余。
        
        >>, <<表示右移和左移。&, |, ^表示二进制的AND, OR, XOR运算。
        >, <, ==, !=, <=, >=用于比较两个表达式的值，分别表示大于、小于、等于、不等于、小于等于、大于等于。
        在这些运算符里面，~, |, ^, &, <<, >>必须应用于整数。
        
        """
        
        
