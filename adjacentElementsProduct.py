#!/usr/bin/env python
# -*- coding: utf-8 -*-
def adjacentElementsProduct(inputArray):
    Prod = min(inputArray) * max(inputArray)
    for (i,j) in enumerate(inputArray):
        try:
            Prod_Test = j * inputArray[i+1]
        except:
            pass
        if Prod_Test > Prod:
            Prod = Prod_Test
    return Prod
