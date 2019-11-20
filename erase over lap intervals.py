#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:47:43 2019

@author: luojierong
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        ans = 0
        n = len(intervals)
        if n == 0:
            return 0
        last = intervals[0][0]
        for i in range(n):
            if intervals[i][0] >= last:
                n -= 1
                last = intervals[i][1]
        return n