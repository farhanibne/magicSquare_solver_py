
import math
import os
import random
import re
import sys


def agic_min_cont(s):
    possible_magic_squares = [
        [[8,1,6],[3,5,7],[4,9,2]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[2,7,6],[9,5,1],[4,3,8]]
    ]
    
    min_cost = float('inf')
    for p in possible_magic_squares:
        cur_cost = 0
        for i in range(len(p)):
            for j in range(len(p[i])):
                cur_cost +=abs(s[i][j] - p[i][j])
                
        if cur_cost < min_cost:
            min_cost = cur_cost
            
            
    return min_cost