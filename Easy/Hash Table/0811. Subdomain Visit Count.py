class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        counter = Counter()
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            subs = domain.split(".")
            for i in range(len(subs)):
                counter[".".join(subs[i:])] += int(count)
                
        return [ f'{count} {domain}' for domain, count in counter.items()]
        
        
