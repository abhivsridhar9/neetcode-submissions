class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map=dict()

        for s in strs:
            sorted_string=tuple(sorted(s))
            if sorted_string not in ana_map:
                ana_map[sorted_string]=[]
            
            ana_map[sorted_string].append(s)
        
        return list(ana_map.values())