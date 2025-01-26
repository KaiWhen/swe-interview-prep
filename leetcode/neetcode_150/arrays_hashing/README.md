### Valid Anagram - Hash Table (Easy)
https://leetcode.com/problems/valid-anagram/description/

Solution:

```py
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hash_s = {}
    hash_t = {}
    
    for i in range(len(s)):
        hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
        hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
    
    return hash_s == hash_t
```

Time Complexity: O(n)


### Group Anagrams - Hash Map (Medium)

Solution:

```py
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hash_map = defaultdict(list) # char_count, list

    for s in strs:
        count = [0] * 26 # a..z

        for c in s:
            count[ord(c) - ord("a")] += 1 # mapping a to 0, b to 1, etc
        
        hash_map[tuple(count)].append(s)
    
    return hash_map.values()
```

Time Complexity: O(m*n)


### Top K Frequent Elements - Hash Map, Bucket Sort (Medium)

Sort Solution (O(nlogn)):

```py
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hash_map = {}
    for n in nums:
        hash_map[n] = 1+hash_map.get(n, 0)
    
    res = []
    hash_map = dict(sorted(hash_map.items(), key=lambda y:y[1], reverse=True))

    for key in hash_map:
        res.append(key)
        k -= 1
        if k==0:
            break

    return res
```

Bucket Sort Solution (O(n)):

```py
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hash_map = {}
    freqs = [[] for i in range(len(nums)+1)]

    for n in nums:
        hash_map[n] = 1+hash_map.get(n,0)
    for n,c in hash_map.items():
        freqs[c].append(n)
    
    res=[]
    for i in range(len(freqs) - 1, 0, -1):
        for n in freqs[i]:
            res.append(n)
            if len(res) == k:
                return res
```