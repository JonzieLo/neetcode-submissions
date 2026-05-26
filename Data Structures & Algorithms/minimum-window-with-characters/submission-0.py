class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        if len(s)< len(t):
            return ""

        t_cnt = {}
        for i in t:
            t_cnt[i] = 1 + t_cnt.get(i, 0)
        
        win = {}
        curr = 0
        output = [0,len(s)]
        output_len = len(s) + 1
        left = 0
        for right in range(len(s)):
            char = s[right]
            win[char] = 1 + win.get(char, 0)

            if char in t_cnt and win[char] == t_cnt[char]:
                curr += 1
            
            while curr == len(t_cnt):
                if (right - left + 1) < output_len:
                    output = [left, right]
                    output_len = right - left + 1
                
                win[s[left]] -= 1
                if s[left] in t_cnt and win[s[left]] < t_cnt[s[left]]:
                    curr -= 1
                left += 1
        left, right = output
        if output_len != len(s) + 1:
            return s[left: right + 1]    
        else: return ""

        
        
            
