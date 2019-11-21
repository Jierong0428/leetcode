#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:38:16 2019

@author: luojierong
"""

import heapq
class MedianFinder:

    def __init__(self):
        self.n0 = 0
        self.n1 = 0
        self.h0 = []
        self.h1 = []
        

    def addNum(self, num: int) -> None:
        if not self.n0  or num > -self.h0[0]:
            heapq.heappush(self.h1,num)
            self.n1 += 1
            if self.n1 > self.n0 + 1:
                heapq.heappush(self.h0,-heapq.heappop(self.h1))
                self.n0 += 1
                self.n1 -= 1
        else:
            heapq.heappush(self.h0,-num)
            self.n0 += 1
            if self.n1 < self.n0:
                heapq.heappush(self.h1,-heapq.heappop(self.h0))
                self.n0 -= 1
                self.n1 += 1
                
        

    def findMedian(self) -> float:
        if self.n0 == self.n1:
            return (self.h1[0] - self.h0[0])/2
        else:
            return self.h1[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()