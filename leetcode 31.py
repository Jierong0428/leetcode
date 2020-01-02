#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:59:38 2020

@author: luojierong
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        flag = False
        for i in range(n - 2,-1, -1):
            if nums[i] < nums[i + 1]:
                flag = True
                break
        if not flag:
            nums = nums.reverse()
        else:
            for j in range(n - 1, i, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
            nums[i + 1:] = nums[i + 1:][ : :-1]