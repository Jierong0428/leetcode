#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:32:17 2019

@author: luojierong
"""

nixushu=0
def merge(left,right):
    global nixushu
    ans=[]
    left=mergesort(left)
    right=mergesort(right)
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            ans.append(left[i])
            i+=1
        else:
            nixushu+=len(left) - i
            ans.append(right[j])
            j+=1
    if i<len(left):
        ans+=left[i:]
    if j<len(right):
        ans+=right[j:]
    return ans   
def mergesort(seq):
    if len(seq)<=1:
        return seq
    midpoint=len(seq)//2
    left = seq[:midpoint]
    right = seq[midpoint:]
    return merge(left,right)
print(mergesort([3,1,2,5,4]))
print(nixushu)
    
        