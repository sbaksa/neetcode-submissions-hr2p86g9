class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            if not stack:
                stack.append(i)
            while stack and temperatures[stack[-1]] < v:
                tempvalue = stack.pop()
                result[tempvalue] = i - tempvalue
            stack.append(i)

        return result