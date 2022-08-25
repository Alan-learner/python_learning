from copy import copy


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        cnt = 0
        res_list = list()
        while cnt <= length // 2:
            if nums1 and nums2:
                if nums1[0] <= nums2[0]:
                    num =  nums1.pop(0)
                else:
                    num = nums2.pop(0)
            else:
                if nums1:
                    num =  nums1.pop(0)
                else:
                    num = nums2.pop(0)
            res_list.append(num)
            cnt+=1
        if cnt == 1:
            res = res_list[0]
        if length % 2 == 0:
            res = (res_list[-1]+res_list[-2])/2
        else:
            res = res_list[-1]
        return float(res)
copy