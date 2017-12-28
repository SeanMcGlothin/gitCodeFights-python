#!/usr/bin/env python
# -*- coding: utf-8 -*-
def checkPalindrome(inputString):
    if inputString[::-1] == inputString:
        return True
    else:
        return False

