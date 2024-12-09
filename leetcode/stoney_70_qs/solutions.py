class Arrays:
    # https://leetcode.com/problems/contains-duplicate/
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use python set as they do not allow duplicates
        if len(set(nums)) == len(nums):
            return False
        else:
            return True


    # https://leetcode.com/problems/missing-number/
    def missingNumber(self, nums: List[int]) -> int:
        # can use enumeration
        # example of enumeration:
        # fruits = ["apple", "banana", "orange"]
        # for index, value in enumerate(fruits):
        #   print(index, value)
        # output: 0 apple  1 banana  2 orange
        
        # solution 1: O(nlogn) because sort is nlogn
        # but rest is linear

        # nums.sort()
        # for i, v in enumerate(nums):
        #     # at some point index will be < v
        #     if(i != v):
        #         return v-1 # or i
            
        #     # edge case in example 2
        #     if v == len(nums)-1:
        #         return v+1


        # solution 2: O(N) iterate through list and sum
        # (twice: once for given list and once for expected using range)
        # len = O(1)
        # range object creation = O(1)
        # sum = O(N)

        # range of len nums+1 because e.g. [3,0,1] if just len nums
        # we would get 0,1,2
        # so here we would have 0+1+2+3 = 6 - 3+0+1 = 2
        return sum(range(len(nums)+1)) - sum(nums)


    # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Problem: Check given list for missing numbers range(1, len(nums))
        # Solution: O(N) iterate  through range and append to new list if
        # not in given list. O(N) space.

        # use a set to get rid of duplicates
        set_nums = set(nums)

        ans = []

        # range 1 to n
        for i in range(1, len(nums)+1):
            
            if i not in set_nums:
                ans.append(i)
        
        return ans


    # https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # Problem: get two numbers in an array that adds up to target
         # Solution: O(N) use hashmap (dict in py) and find the diff between
         # target and value in hashmap

         hash_map = {} # val, idx

         for idx, val in enumerate(nums):
            diff = target - val

            if diff in hash_map:
                return [idx, hash_map[diff]]
            # insert idx and val into hashmap
            hash_map[val] = idx


    # https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Problem: return new list, where for each num[i] in original list,
        # the value in new list is the total of numbers num[i] is bigger than.
        # Solution: instead of iterating twice, sort the list to temp list,
        # dict the value for each num (not identical) in temp list,
        # where index of first new number also represents previous numbers bigger than:
        # O(nlogn) time for sorting & O(N) space for dict.

        temp = sorted(nums)
        d = {}

        # e.g. nums=[8,1,2,2,3]
        # we make the dict d={1:0, 2:1, 3:3, 8:4}
        for i, num in enumerate(temp):
            if num not in d:
                d[num] = i
        
        ans = []

        # this gives us [4,0,1,1,3]
        for i in nums:
            ans.append(d[i])
        
        return ans
