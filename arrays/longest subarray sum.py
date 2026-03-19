class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsumcount = {}
        prefixsum = 0
        prefixsumcount[0] = 1
        cnt = 0

        for i in range(len(nums)):
            prefixsum += nums[i]
            remove = prefixsum - k

            if remove in prefixsumcount:
                cnt += prefixsumcount[remove]

            prefixsumcount[prefixsum] = prefixsumcount.get(prefixsum, 0) + 1

        return cnt
