from collections import defaultdict
from typing import List


class Solution:
    # https://leetcode.com/problems/course-schedule-ii/
    # Twilio
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of prereqs
        prereq = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 possible states:
        # visited => crs has been added to output
        # visiting => crs not added to output, but added to cycle
        # unvisited => crs not added to output or cycle
        
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
    

    # https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
    # Twilio
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0

        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1

        for n in nums:
            prefix_sum += n
            remain = prefix_sum % k

            res += prefix_cnt[remain]
            prefix_cnt[remain] += 1
        return res
    

# https://leetcode.com/problems/lru-cache/
# Twilio/Twitch
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        # left=LRU, right=MRU
        self.left, self.right = Node(0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the linked list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
