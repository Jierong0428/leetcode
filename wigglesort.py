#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:15:27 2019

@author: luojierong
"""

class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2=nums.copy()
        nums2.sort()
        n = len(nums)
        if n%2:
            midpoint = n//2
        else:
            midpoint = n//2-1
        j=n-1
        i=midpoint
        point=0
        while j > midpoint:
            nums[point] = nums2[i]
            nums[point+1] = nums2[j]
            j-=1
            i-=1
            point+=2
        if n%2:
            nums[-1]=nums2[0]
        print(nums)
            
    
            