#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:00:13 2020

@author: luojierong
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        ans = []
        ans. append("1")
        for i in range(n - 1):
            sample = ans[i]
            say = ''
            cnt = 1
            j = 0
            while j < len(sample):
                if j + 1 < len(sample) and sample[j] == sample[j + 1]:
                    cnt += 1
                else:
                    say += str(cnt) + sample[j]
                    cnt = 1
                j += 1
            ans.append(say)
        return ans[n - 1]
                