#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:59:34 2019

@author: luojierong
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        n = len(intervals)
        if n == 0:
            return []
        ans = []
        last = intervals[0][1]
        begin = intervals[0][0]
        for i in range(1,n):
            if intervals[i][0] >last:
                ans.append([begin,last])
                begin = intervals[i][0]
                last = intervals[i][1]
            else:
                last = max(last,intervals[i][1])
        ans.append([begin,last])
        return ans
                