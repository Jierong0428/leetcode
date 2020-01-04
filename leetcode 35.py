#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:22:31 2020

@author: luojierong
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        le, ri = 0 , n - 1
        if target > nums[n - 1]:
            return n
        if target < nums[0]:
            return 0
        while le <= ri:
            mid = (le + ri) // 2
            if nums[mid] == target:
                return mid 
            if target <= nums[mid]:
                ri = mid - 1
            else:
                le = mid + 1
        return le