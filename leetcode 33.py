#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:38:25 2020

@author: luojierong
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        le, ri = 0, n - 1
        while le <= ri:
            mid = (le + ri) // 2
            if nums[mid] == target:
                return mid
            if nums[le] <= nums[mid]:
                if  nums[le] <= target <= nums[mid]:
                    ri = mid - 1
                else:
                    le = mid + 1
            else:
                if nums[mid] <= target <= nums[ri]:
                    le = mid + 1
                else:
                    ri = mid - 1
        return -1 
                    