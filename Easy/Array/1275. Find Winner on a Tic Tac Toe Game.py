class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        # 語法: seq[start:end:step]
        
        aList = moves[0::2]
        bList = moves[1::2]
        
        if [0,0] in aList and [1,1] in aList and [2,2] in aList or [2,0] in aList and [1,1] in aList and [0,2] in aList:
            return "A"
        if [0,0] in bList and [1,1] in bList and [2,2] in bList or [2,0] in bList and [1,1] in bList and [0,2] in bList:
            return "B"
        
        a_Xaxis = {}
        a_Yaxis = {}
        b_Xaxis = {}
        b_Yaxis = {}
        
        for i in aList:
            a_Xaxis[i[0]] = a_Xaxis.get(i[0], 0) + 1 # add up the values
            a_Yaxis[i[1]] = a_Yaxis.get(i[1], 0) + 1
        
        for i in bList:
            b_Xaxis[i[0]] = b_Xaxis.get(i[0], 0) + 1 # add up the values
            b_Yaxis[i[1]] = b_Yaxis.get(i[1], 0) + 1
        
        for i in range(3):
            if i in a_Xaxis:
                if  a_Xaxis[i] == 3:
                    return "A"
                
            if i in a_Yaxis:
                if  a_Yaxis[i] == 3:
                    return "A"
                
            if i in b_Xaxis:
                if  b_Xaxis[i] == 3:
                    return "B"   
            
            if i in b_Yaxis:
                if  b_Yaxis[i] == 3:
                    return "B"
                
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
                
                
                
                
                
        
  
