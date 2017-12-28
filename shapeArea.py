#!/usr/bin/env python
# -*- coding: utf-8 -*-
def shapeArea(n):
    val = 1
    for i in range(1,n):
        val += 4 * i
    return val
