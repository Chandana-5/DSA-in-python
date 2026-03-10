class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        max_len = 0

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]

                if s == k:
                    max_len = max(max_len, j - i + 1)

        return max_len
