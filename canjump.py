#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:37:20 2020

@author: luojierong
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump = nums[0]
        n = len(nums)
        i = 0
        while i < maxjump:
            if maxjump >= n - 1:
                return True
            i += 1
            currjump = nums[i] + i
        
            maxjump = max(currjump,maxjump)
        if maxjump < n - 1:
            return False
        return True