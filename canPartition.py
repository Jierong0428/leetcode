#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:07:38 2019

@author: luojierong
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m = len(nums)
        if sum(nums) % 2:
            return False
        n = int(sum(nums) / 2)
        f = [True] + [False for i in range(n)]
        for i in range(m):
            for j in range(n,-1,-1):
                if j - nums[i] >= 0 and j > 0:
                    f[j] = (f[j] or f[j - nums[i]])
                elif j == 0:
                    f[j] = False
                if j == n and f[j] == True:
                    return True
                
        return False
                    