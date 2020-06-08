#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:00:52 2020

@author: luojierong
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = ["+","-","*","/"]
        n = len(tokens)
        for i in range(n):
            if tokens[i] in operand:
                if  tokens[i] == "+":
                    num = stack[-1] + stack[-2]
                elif tokens[i] == "-":
                    num = stack[-2] - stack[-1]
                elif tokens[i] == '*':
                    num = stack[-2] * stack[-1]
                elif tokens[i] == '/':
                    num = int(stack[-2] / stack[-1])
                del stack[-1]
                del stack[-1]
                stack.append(num)
            else:
                num = int(tokens[i])
                stack.append(num)
        res = stack[-1]
        return res
                