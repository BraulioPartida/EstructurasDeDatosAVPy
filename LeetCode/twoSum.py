from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

        return []  # Return an empty list if no solution is found


d = Solution()
list = [2, 7, 11, 15]
print(d.twoSum(list, 9))
