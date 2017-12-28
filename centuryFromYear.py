#!/usr/bin/env python
# -*- coding: utf-8 -*-

def centuryFromYear(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
yyyy = int(input('Enter a year: '))
answer = centuryFromYear(yyyy)
print("Its the %dth century"% answer)
#end
