import collections
import re

vowels = set(['a', 'e', 'i', 'o', 'u'])
bad_strs = set(['ab', 'cd', 'pq', 'xy'])
nice = 0

with open('input.txt') as f:
    for line in f:
        poss_str = line.strip()

        found_pair = False
        for idx, c1 in enumerate(poss_str):
            if idx + 2 > len(poss_str):
                break

            c2 = poss_str[idx+1]
            str_to_match = c1+c2

            if str_to_match in poss_str[idx+2:]:
                found_pair = True
                break

        if not found_pair:
            continue

        found_repeat = False
        for idx, c1 in enumerate(poss_str):
            if idx + 3 > len(poss_str):
                break

            c2 = poss_str[idx+1]
            c3 = poss_str[idx+2]
            if c3 == c1:
                found_repeat = True
                break

        if not found_repeat:
            continue

        print '%s is nice!' % poss_str
        nice += 1

print nice
