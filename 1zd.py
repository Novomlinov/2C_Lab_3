#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    if len(A) != 10:
       print("Неверный размер списка", file=sys.stderr)
       exit(1)
    s = 0
    for item in A:
       if (((item) > 3) and ((item) < 8)):
          s += item
    print(s)