class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)
        
        for p, s in cars:
            distance = (target - p) / s
            if not stack or stack[-1] < distance:
                stack.append(distance)
        
        return len(stack)