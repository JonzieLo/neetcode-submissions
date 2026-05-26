class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False

        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            if s[i] == ")" or s[i] == "]" or s[i] == "}":
                if len(stack) == 0:
                    return False
                stack_end = stack.pop()
                if stack_end == "(" and s[i] != ")":
                    return False
                if stack_end == "[" and s[i] != "]":
                    return False
                if stack_end == "{" and s[i] != "}":
                    return False
        if len(stack) != 0:
            return False
        else: return True
