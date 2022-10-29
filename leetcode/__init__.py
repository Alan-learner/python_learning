# encoding: utf-8
# author: Alan-learner

import math
from collections import deque
from math import inf
from typing import List
from bisect import bisect_left, bisect_right
from functools import reduce
from heapq import heappush, heappop, heapreplace, heapify
from math import comb
from executing import cache
from yarl import cache_clear

from numpy import lcm

from sortedcontainers import SortedList
from itertools import permutations, combinations

lowbit = lambda x: x & -x
MOD = int(1e9 + 7)
INF = int(1e20)
