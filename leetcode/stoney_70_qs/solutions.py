from collections import deque
from typing import List


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


    # https://leetcode.com/problems/minimum-time-visiting-all-points/
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # clarifying q: do we have to start at (0,0) or can we start at the
        # first point? we can start at first point
        # Problem: from a list of points, calculate the min distance between first
        # and last point
        # Solution: If the next node is +10x and -5y away, it's going to take
        # exactly 10 steps, because you can only move 1 x at a time and the diff
        # in y is made up by diagonal moves during the process of overcoming the
        # difference in x. Time: O(N) Space: O(1)
        # Note: distance between two points in max difference of one coord

        res = 0
        x1, y1 = points.pop()
        # while points is not empty
        while points:
            x2, y2 = points.pop()
            res += max(abs(y2 - y1), abs(x2 - x1))
            x1, y1 = x2, y2
        return res
    

    # https://leetcode.com/problems/spiral-matrix/
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Problem: given an m x n matrix, return all elements in spiral order
        # O(N)
        ans = []
        while matrix:
            #1) add first row/list of matrix
            ans += (matrix.pop(0))

            #2) append last element of all lists in order
            if matrix and matrix[0]:
                for row in matrix:
                    ans.append(row.pop())

            #3) add reverse of last row/list
            if matrix:
                ans += (matrix.pop()[::-1])
            
            #4) append first element of all rows/lists in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
        
        return ans
    

    # https://leetcode.com/problems/number-of-islands/
    def numIslands(self, grid: List[List[str]]) -> int:
        # Problem: given a 2d m*n grid, where 1 is land and 0 is water,
        # return the no of islands
        # Solution: Iterate through and perform DFS or BFS after find a '1'
        # to mark neighbours as visited, and complete the island. Time & Space:
        # O(M*N). Visit each cell once during initial iteration and potentially
        # twice when exploring BFS in each direction (4 - up down left right)
        # and we do this for M*N vertices. It might help to think of worse case
        # scenario - matrix is all '1' so we visit every cell and explore every
        # adjacent cell. For space, it could be we stack/queue the entire grid if 
        # it is all 1s.

        if not grid:
            return 0
        
        def bfs(r, c):
            search_q = deque()
            visited.add((r,c))
            search_q.append((r,c))

            # once search queue is empty, that means all the surrounding 1s have
            # been searched i.e. an island was found
            while search_q:
                row, col = search_q.popleft()
                directions = ([1,0], [-1,0], [0,1], [0,-1])

                for dr, dc in directions:
                    r,c = row-dr, col-dc

                    if (r in range(rows) and c in range(cols) and grid[r][c]=='1' and (r,c) not in visited):
                        search_q.append((r,c))
                        visited.add((r,c))

        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        for r in range(rows):

            for c in range(cols):
                
                # once we find an unvisited '1' we run bfs and add it to the search
                # queue to be searched
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    count += 1
        
        return count