from copy import deepcopy
from functools import lru_cache
from typing import List
from typing import Tuple

problem = """144
10
75
3
36
80
143
59
111
133
1
112
23
62
101
137
41
24
8
121
35
105
161
69
52
21
55
29
135
142
38
108
141
115
68
7
98
82
9
72
118
27
153
140
61
90
158
102
28
134
91
2
17
81
31
15
120
20
34
56
4
44
74
14
147
11
49
128
16
99
66
47
125
155
130
37
67
54
60
48
136
89
119
154
122
129
163
73
100
85
95
30
76
162
22
79
88
150
53
63
92
"""

example = """16
10
15
5
1
11
7
19
6
12
4"""


def distribution(nums: List[int]):
    count_by_difference = {
        1: 0,
        2: 0,
        3: 0
    }
    s = sorted(nums)
    s.append(max(s) + 3)
    s.insert(0, 0)
    for i in range(1, len(s)):
        count_by_difference[s[i] - s[i - 1]] += 1

    print(count_by_difference)
    print(count_by_difference[3] * count_by_difference[1])


@lru_cache()
def distinct_arrangements(nums: Tuple[int], prev: int):
    head = nums[0]
    remaining = nums[1:]
    if head - prev > 3:
        return 0
    if not remaining:
        return 1
    # all possibilities = (possibilities using head) + (possibilities not using head)
    return distinct_arrangements(remaining, head) + distinct_arrangements(remaining, prev)


if __name__ == '__main__':
    nums = [int(n) for n in problem.splitlines()]
    # part 1
    distribution(nums)

    # part 2
    # tuple so repeated calls can be cached
    print(distinct_arrangements(tuple(sorted(nums)), 0))
