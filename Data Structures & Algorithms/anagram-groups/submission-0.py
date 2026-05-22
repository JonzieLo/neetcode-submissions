class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            sorted_str = sorted(string)
            sorted_strs = ''.join(sorted_str)
            if sorted_strs not in anagrams:
                anagrams[sorted_strs] = [string]
            else:
                anagrams[sorted_strs].append(string)
        return list(anagrams.values())