#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:55:33 2020

@author: luojierong
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for cur_str in strs:
            item = ''.join(sorted(cur_str))
            dct[item] = dct.get(item,[]) + [cur_str]
        return dct.values()