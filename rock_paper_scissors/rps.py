#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    r = 'rock'
    p = 'paper'
    s = 'scissors'
    if n == 0:
        return([[]])
    if n == 1:
        return [[r], [p], [s]]
    else:
        options = rock_paper_scissors(n-1)
        output = []
        for o in options:
            output += [o + [r]]
            output += [o + [p]]
            output += [o + [s]]
        return(output)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


rock_paper_scissors(2)
