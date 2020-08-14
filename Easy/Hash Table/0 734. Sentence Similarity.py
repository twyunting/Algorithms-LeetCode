class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        
        if len(words1)!=len(words2):
            return False
        from collections import defaultdict
        edges = defaultdict(set)
        # edges={}
        
        for a,b in pairs:
            edges[a].add(b)
            edges[b].add(a)
        for a in words1:
            edges[a].add(a)
        for b in words2:
            edges[b].add(b)
        
        """
        # print(edges)
        
        {'great': {'fine', 'great'},
        'fine': {'fine', 'great'},
        'drama': {'acting', 'drama'},
        'acting': {'acting', 'drama'},
        'skills': {'talent', 'skills'}, 
        'talent': {'talent', 'skills'}})
        """
        
        for a,b in zip(words1,words2):
            if a not in edges[b]:
                return False
            
        return True
        
        
