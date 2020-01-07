#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:02:04 2020

@author: luojierong
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums1 = []
        used = []
        n = len(nums)
        for i in range(n):
            if nums[i] not in nums1:
                nums1.append(nums[i])
                used.append(1)
            else:
                index = nums1.index(nums[i])
                used[index] += 1
        ans = []
        a = []
        n1 = len(nums1)
        def dfs(x):
            if x == n:
                ans.append(a.copy())
                return
            for i in range(n1):
                if used[i]:
                    a.append(nums1[i])
                    used[i] -= 1
                    dfs(x + 1)
                    used[i] += 1
                    a.pop()
        dfs(0)
        return ans