#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:34:50 2019

@author: luojierong
"""

class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        dct = {}
        st = 0
        res = 0
        if not s:
            return 0
        for i in range(len(s)):
            last_pos = dct.get(s[i],-1)
            dct[s[i]] = i
            st = max(st,last_pos + 1)
            res = max(res,i - st + 1)
        return res
            