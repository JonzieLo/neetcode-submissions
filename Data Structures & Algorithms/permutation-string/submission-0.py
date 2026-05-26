class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target_cnt = Counter(s1)
        window_cnt = Counter(s2[:len(s1)])
        if window_cnt == target_cnt:
            return True
        for i in range(len(s1), len(s2)):
            new_char = s2[i]
            window_cnt[new_char] += 1

            prev_char = s2[i-len(s1)]
            window_cnt[prev_char] -= 1

            if window_cnt[prev_char] == 0:
                del window_cnt[prev_char]

            if window_cnt == target_cnt:
                return True
        return False
            