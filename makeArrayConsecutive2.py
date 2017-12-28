#!/usr/bin/env python
# -*- coding: utf-8 -*-
def makeArrayConsecutive2(statues):
    statues = sorted(statues)
    count = 0
    min = statues[0]
    max = statues[len(statues)-1]
    for i in range(min, max):
        if i not in statues:
            count += 1
    return count
