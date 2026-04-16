class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        # iterate through list
        # add each to list
        # take current ith and subtract it by target
        # if target - ith = difference
        # look for difference in hash

        for i, n in enumerate(nums):
            difference = target - n

            if difference in seen:
                j = seen[difference]
                return [min(i,j), max(i,j)]


            seen[n] = i

        
        return []