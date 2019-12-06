#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:29:11 2019

@author: luojierong
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode,t=0) -> ListNode:
       
        res = ListNode(l1.val + l2.val + t)
        t = res.val // 10
        if l1.next or l2.next or t:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            res.next = self.addTwoNumbers(l1.next,l2.next,t)
        res.val -= t * 10
        return res