class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        left = 0
        maxF = 0
        output = 0
        
        for i in range(len(s)):
            cnt[s[i]] = 1 + cnt.get(s[i], 0)
            
            maxF = max(maxF, cnt[s[i]])
            while (i - left + 1) - maxF > k:
                cnt[s[left]] -= 1
                left += 1
            output = max(output, i - left + 1)
        return output