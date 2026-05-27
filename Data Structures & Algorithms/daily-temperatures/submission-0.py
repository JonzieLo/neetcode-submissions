class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        if len(temperatures) == 1:
            return [0]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                output[stack_i] = i - stack_i
            stack.append((t,i))
        return output
            