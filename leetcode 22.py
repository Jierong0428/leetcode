#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:25:19 2019

@author: luojierong
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cur_str,n,pre_sum):
            if n == 0 and pre_sum == 0:
                res.append(cur_str)
                return
            if n:
                dfs(cur_str + "(",n - 1,pre_sum + 1)
            if pre_sum:
                dfs(cur_str + ")",n,pre_sum - 1)
        dfs("",n,0)
        return res