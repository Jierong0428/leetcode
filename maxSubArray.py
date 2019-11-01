#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:00:28 2019

@author: luojierong
"""

class Solution:
    def maxSubArray(self, nums):
        current_max=nums[0]
        global_max=nums[0]
        n=len(nums)
        for i in range(1,n):
            if current_max<0:
                current_max=0
            current_max+=nums[i]
            global_max=max(global_max,current_max)
        return global_max
        
        
        