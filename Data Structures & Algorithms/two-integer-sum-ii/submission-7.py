class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        while l < r:
            summation = numbers[r]+numbers[l]

            if summation > target:
                r -= 1
            else:
                l += 1

            if summation == target:
                return [l,r+1]
            
            