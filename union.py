class Solution:
    def unionArray(self, nums1, nums2):
        union=[]
        i=0
        j=0
        n=len(nums1)
        m=len(nums2)
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                if not union or union[-1]!=nums1[i]:
                    union.append(nums1[i])
                i=i+1
            elif nums2[j]<nums1[i]:
                if not union or union[-1]!=nums2[j]:
                    union.append(nums2[j])
                j=j+1
            else:
                if not union or union[-1]!=nums2[j]:
                    union.append(nums1[i])
                i=i+1
                j=j+1
        while i<n:
                if not union or union[-1]!=nums1[i]:
                    union.append(nums1[i])
                i=i+1
        while j<m:
                if not union or union[-1]!=nums2[j]:
                    union.append(nums2[j])
                j=j+1
        return union


            
            