# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countTable = {}
        for i in xrange(len(nums)):
            countTable[nums[i]] = countTable[nums[i]] + 1 if nums[i] in countTable else 1
            
        freqTable = [[] for i in xrange(len(nums) + 1)]
        
        for key in countTable:
            freqTable[countTable[key]].append(key)
        
        result = []
        for i in xrange(len(freqTable) - 1, - 1, -1):
            result += freqTable[i]
            if len(result) == k:
                break
        return result