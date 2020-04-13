#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:32:00 2020

@author: luojierong
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ind = n - 1
        while digits[ind] == 9:
            digits[ind] = 0
            ind -= 1
        if ind == -1:
            digits.append(0)
            digits[ind + 1] += 1
        else:
            digits[ind] += 1
        return digits