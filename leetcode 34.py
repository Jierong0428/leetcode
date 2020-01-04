#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 14:34:30 2020

@author: luojierong
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1,-1]
        def lowerbound(le,ri):
            while le <= ri:
                mid = (le + ri) // 2
                if target <= nums[mid]:
                    ri = mid - 1
                else:
                    le = mid + 1
            return ri + 1
        def upperbound(le,ri):
            while le <= ri:
                mid = (le + ri) //2
                if target < nums[mid]:
                    ri = mid - 1
                else:
                    le = mid + 1
            return le - 1
        l = lowerbound(0,n - 1)
        if l == n or nums[l] != target:
            return [-1,-1]
        else:
            return[l,upperbound(l,n - 1)]
        