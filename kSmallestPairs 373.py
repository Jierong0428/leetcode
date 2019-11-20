#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:11:46 2019

@author: luojierong
"""

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        n = len(nums1)
        m = len(nums2)
        if n == 0 or m ==0:
            return ans
        heap = []
        index = [0 for i in range(n)]
        for i in range(n):
            heapq.heappush(heap,(nums1[i] + nums2[index[i]],i))
        while k > 0 and n > 0:
            x = heap[0][1]
            ans.append([nums1[x],nums2[index[x]]])
            heapq.heappop(heap)
            index[x] += 1
            if index[x] < m:
                heapq.heappush(heap,(nums1[x] + nums2[index[x]],x))
            else:
                n -= 1
            k -= 1
        return ans
            
        