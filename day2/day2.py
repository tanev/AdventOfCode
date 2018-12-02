#!/usr/bin/env python3
'''
--- Day 2: Inventory Management System ---

You stop falling through time, catch your breath, and check the screen on the device.
"Destination reached. Current Year: 1518. Current Location: North Pole Utility Closet 83N10."
You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice.
"...I'm not sure either. But now that so many people have chimneys, maybe he could sneak in
that way?" Another voice responds, "Actually, we've been working on a new kind of suit
that would let him fit through tight spaces like that. But, I heard that a few days ago,
 they lost the prototype fabric, the design plans, everything! Nobody on the team can
 even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse?
They'd be stored together, so the box IDs should be similar. Too bad it would take forever
 to search the warehouse for two similar box IDs..." They walk too far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could
cause if you were discovered - and use your fancy wrist device to quickly scan every box
and produce a list of the likely candidates (your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes again, counting
the number that have an ID containing exactly two of any letter and then separately
counting those with exactly three of any letter. You can multiply those two counts together
to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

    abcdef contains no letters that appear exactly two or three times.
    bababc contains two a and three b, so it counts for both.
    abbcde contains two b, but no letter appears exactly three times.
    abcccd contains three c, but no letter appears exactly two times.
    aabcdd contains two a and two d, but it only counts once.
    abcdee contains two e.
    ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice, and three
of them contain a letter which appears exactly three times. Multiplying these together
produces a checksum of 4 * 3 = 12.

--- Part Two ---

Confident that your list of box IDs is complete, you're ready to find the
 boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position
in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz

The IDs abcde and axcye are close, but they differ by two characters (the second and fourth).
However, the IDs fghij and fguij differ by exactly one character, the third (h and u).
Those must be the correct boxes.

What letters are common between the two correct box IDs?
(In the example above, this is found by removing the differing character
from either ID, producing fgij.)

'''

import sys
import collections


def get(ifile):
    '''Reads elements from the ifile file'''
    with open(ifile) as ftarget:
        return [
            str(i.rstrip('\n')) for i in ftarget.readlines()
            if i != ''
        ]


def getcounts(istr, counts=None):
    '''istr: str - letters
    counts: dict with two keys for two-counts and three-counts

    analyzes string and updates the counts dict with the number
    found in istr'''
    rdict = collections.defaultdict(int)
    for letter in istr:
        rdict[letter] += 1
    for val in [2, 3]:
        if val in set(rdict.values()):
            counts[val] += 1


def oneletter(box1, box2):
    '''box1, box2: str (same length)

    returns True if there is only one letter difference between
    them
    '''
    assert len(box1) == len(box2)
    length = len(box1)
    res = [
        ord(box1[i]) - ord(box2[i]) for i in range(length)
    ]
    res = [i for i in res if i != 0]
    if len(res) == 1:
        return True
    return False


def findflip(lboxes):
    '''Searches for box ID with only one letter difference
    returns results list with tuples containing (box1, box2)'''
    results = []
    oneletter('fghij', 'fguij')
    end = len(lboxes)
    for ind1 in range(end):
        # walk from this one to all the others
        for ind2 in range(ind1+1, end):
            tup = (lboxes[ind1], lboxes[ind2])
            if oneletter(*tup):
                results.append(tup)
    return results


def runtests():
    '''Ensures the provided examples above are working'''
    # part 1
    cases = [
        ('abcdef', {2: 0, 3: 0}),
        ('bababc', {2: 1, 3: 1}),
        ('abbcde', {2: 1, 3: 0}),
        ('abcccd', {2: 0, 3: 1}),
        ('aabcdd', {2: 1, 3: 0}),
        ('abcdee', {2: 1, 3: 0}),
        ('ababab', {2: 0, 3: 1})
    ]
    for case in cases:
        counts = {2: 0, 3: 0}
        getcounts(case[0], counts=counts)
        assert counts == case[1]

    # part 2
    tlist = [
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz'
    ]
    assert findflip(tlist) == [('fghij', 'fguij')]


def main(infile):
    '''Main function'''
    inputs = get(infile)
    runtests()
    counts = {2: 0, 3: 0}
    for istr in inputs:
        getcounts(istr, counts=counts)
    print(
        'Part1 result is {b} * {i} = {r}'.format(
            b=counts[2],
            i=counts[3],
            r=counts[2] * counts[3]
        )
    )
    res = findflip(inputs)
    if len(res) != 1:
        print('Failed to find result for part 2', file=sys.stderr)
    else:
        box1 = res[0][0]
        box2 = res[0][1]
        letters = [
            box1[i] for i in range(len(box1)) if box1[i] == box2[i]
        ]
        print('Part2 result (common letters): {i}'.format(i=''.join(letters)))


if __name__ == '__main__':
    try:
        INFILE = sys.argv[1]
    except IndexError:
        exit("Usage: {b} INFILE")
    main(INFILE)
