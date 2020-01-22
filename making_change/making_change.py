#!/usr/bin/python

import sys


def making_change(amount, denominations):
    if n == 0:
        return(1)
    elif (n >= 0) & (n < 5):
        return(n)
    elif (n >= 5) & (n < 10):
        return(2)
    elif (n >= 10) & (n < 25):
        return()
  pass


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")

making_change(10, [1, 5, 10, 25, 50])

1s
5s
5s 1s
10s 1s
10s 5s 1s
