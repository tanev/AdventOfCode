#!/usr/bin/env python3

import itertools
import sys

def getfreqchanges(ifile):
    with open(ifile) as ftarget:
        return [
            int(i.rstrip('\n')) for i in ftarget.readlines()
            if i != ''
        ]

def pattern():
    pass

def getchange(changes):
    '''changes: list of integers, calculates just the differences between the present and
    the previous one (starting with 0).
    returns the first frequency seen twice with the list of changes'''
    resfreq = 0
    frequencies = [resfreq]
    for change in itertools.cycle(changes):
        resfreq += change
        if resfreq in frequencies:
            return resfreq
        frequencies.append(resfreq)
    return None

def dotests():
    '''just ensure examples are working'''
    assert getchange([1, -1]) == 0
    assert getchange([3, 3, 4, -2, -4]) == 10
    assert getchange([-6, +3, +8, +5, -6]) == 5
    assert getchange([+7, +7, -2, -7, -4]) == 14

def main(ifile):
    '''
    ifile str path to file to read frequency changes from.

    Gets all frequency changes from ifile, sums the changes in the frequency.
    returns sum'''
    listchanges = getfreqchanges(ifile)
    print('answer to part1: {a}'.format(a=sum(listchanges)))
    dotests()
    print('answer to part2: {c}'.format(c=getchange(listchanges)))

if __name__ == '__main__':
    try:
        INFILE = sys.argv[1]
    except IndexError:
        exit("Usage: {b} INFILE")
    main(INFILE)
