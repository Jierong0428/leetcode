#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:22:44 2019

@author: luojierong
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        
        if n < 3:
            return None
        ans = sum(nums[:3])
        for mid in range(n):
            l, r = 0 , n - 1
            while l < mid and r > mid:
                s = nums[l] + nums[mid] + nums[r]
                if abs(s - target) < abs(ans - target):
                    ans = s
                
                if s > target:
                    r -= 1
                elif s == target:
                    return s
                else:
                    l += 1
        return ans