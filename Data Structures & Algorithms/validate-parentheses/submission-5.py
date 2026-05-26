class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        close_to_open = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif s[i] == ")" or s[i] == "]" or s[i] == "}":
                if len(stack) == 0:
                    return False
                stack_end = stack.pop()
                if stack_end != close_to_open[s[i]]:
                    return False
        if len(stack) != 0:
            return False
        else: return True
