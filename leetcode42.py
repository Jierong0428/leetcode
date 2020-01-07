#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:20:43 2020

@author: luojierong
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        n = len(height)
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = height[stack[-1]]
                stack.pop()
                if stack:
                    ans += (min(height[i],height[stack[-1]]) - top) * (i - stack[-1] - 1)
     
            stack.append(i)
        return ans 