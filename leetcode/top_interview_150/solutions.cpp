#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;


class ArrayString {
public:

    // Merge Two Sorted Arrays - Easy
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if (n == 0)  return;
        int len1 = m+n;
        int end_idx = m+n-1;
        while(n > 0 && m > 0) {
            // if nums2[n-1] is >= nums1[m-1] then put nums2[n-1] at the end_idx of nums1 array
            if(nums2[n-1] >= nums1[m-1]) {
                nums1[end_idx] = nums2[n-1];
                n--;
            }
            else {
                nums1[end_idx] = nums1[m-1];
                m--;
            }
            end_idx--;
        }
        while (n > 0) {
            nums1[end_idx] = nums2[n-1];
            n--;
            end_idx--;
        }
    }

    // Remove Duplicates from sorted array 
    int removeDuplicates(vector<int>& nums) {
        //use two pointers, i and k
        int k = 1;
        // start from 1 since first element always unique, then if nums[i] is != the prev element then place nums[i] at nums[k]
        for (int i=1; i<nums.size(); i++) {
            if (nums[i] != nums[i-1]) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }

    // Remove duplicates from sorted array where each unique element apppears at most twice
    int removeDuplicates2(vector<int>& nums) {
        int k = 0;
        for(auto element : nums) {
            // if first and second element place them there, or if nums[k-2] is != current element then put in k position
            if(k == 0 || k == 1 || nums[k-2] != element) {
                nums[k] = element;
                k++;
            }
        }
        return k;
    }

    // rotate array to the right by k
    void rotate(vector<int>& nums, int k) {
        k=k%nums.size();
        // reverse 0 -> k
        reverse(nums.begin(),nums.begin()+(nums.size()-k));
        // reverse k -> end
        reverse(nums.begin()+(nums.size()-k),nums.end());
        // reverse whole thing
        reverse(nums.begin(),nums.end());
    }
};


class TwoPointer {
public:
    // Valid Palindrome - easy
    // after remove all non alphanumeric chars check if is palindrome
    bool isPalindrome(string s) {
        // two pointers start and end
        int start = 0;
        int end = s.size()-1;
        while(start <= end) {
            // just ignore if is not alnum
            if(!isalnum(s[start])) {
                start++;
                continue;
            }
            if(!isalnum(s[end])) {
                end--;
                continue;
            }
            // return false if char not same
            if(tolower(s[start]) != tolower(s[end])) return false;
            else {
                start++;
                end--;
            }
        }
        return true;
    }

    // Two Sum II - Input array is sorted
    vector<int> twoSum2(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;

        while (left < right) {
            int total = numbers[left] + numbers[right];
            if (total == target) {
                return {left + 1, right + 1};
            }
            // if total > target, the right pointer should decrease as the array is sorted and we need a smaller number
            // else if it's less then target we increase left pointer so that the total is bigger
            else if (total > target) {
                right--;
            }
            else {
                left++;
            }
        }
        return {-1, -1};
    }

    
};


class HashMap {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        int n = nums.size();

        // Build the hash table
        for (int i = 0; i < n; i++) {
            numMap[nums[i]] = i;
        }

        // Find complement
        for (int i=0; i<n; i++) {
            int complement = target - nums[i];
            // if the complement is found and the index is not the same as i
            if (numMap.count(complement) && numMap[complement] != i) {
                return {i, numMap[complement]};
            }
        }
        return {};
    }
};

// TODO: reverse linked list and other common coding interview questions
