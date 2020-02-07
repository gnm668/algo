# John works at a clothing store. He has a large pile of socks that he must
# pair by color for sale. Given an array of integers representing the color of
# each sock, determine how many pairs of socks with matching colors there are.

# For example, there are
# socks with colors . There is one pair of color and one of color . There are
# three odd socks left, one of each color. The number of pairs is .


def sockMerchant(n, ar):
    pairCount = 0
    colorCount = {}

    for color in ar:
        if color not in colorCount:
            colorCount[color] = 1
        else:
            colorCount[color] += 1

    for key in colorCount:
        pairCount += (colorCount[key] // 2)

    return pairCount


# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention
# to small details like topography. During his last hike he took exactly steps.
# For every step he took, he noted if it was an uphill, , or a downhill, step.
# Gary's hikes start and end at sea level and each step up or down represents a

# unit change in altitude. We define the following terms:

#     A mountain is a sequence of consecutive steps above sea level, starting with
# 	a step up from sea level and ending with a step down to sea level.

#     A valley is a sequence of consecutive steps below sea level, starting with
# 	a step down from sea level and ending with a step up to sea level.

# Given Gary's sequence of up and down steps during his last hike, find and print
# the number of valleys he walked through.

# For example, if Gary's path is
# , he first enters a valley units deep. Then he climbs out an up onto a mountain
# units high. Finally, he returns to sea level and ends his hike.

def countingValleys(n, s):
    valleys = 0
    level = 0
    for step in s:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        elif step == 'D':
            level -= 1
    return valleys

    # Emma is playing a new mobile game that starts with consecutively numbered clouds.
# Some of the clouds are thunderheads and others are cumulus. She can jump on any
# cumulus cloud having a number that is equal to the number of the current cloud
#  plus or

# . She must avoid the thunderheads. Determine the minimum number of jumps it will
# take Emma to jump from her starting postion to the last cloud. It is always possible
# to win the game.

# For each game, Emma will get an array of clouds numbered
# if they are safe or if they must be avoided. For example, indexed from .
# The number on each cloud is its index in the list so she must avoid the clouds at
# indexes and . She could follow the following two paths:
#     or . The first path takes jumps while the second takes .

# def jumpingOnClouds(c):
#     jumps = 0
#     finished = False
#     pos = 0

#     while finished is False:
#         jumpOne = None
#         jumpTwo = None

#         if pos + 1 < len(c):
#             jumpOne = pos + 1
#         if pos + 2 < len(c):
#             jumpTwo = pos + 2

#         if jumpTwo is not None and c[jumpTwo] == 0:
#             pos = jumpTwo
#             jumps += 1
#         elif jumpOne is not None and c[jumpOne] == 0:
#             pos = jumpOne
#             jumps += 1

#         if pos >= len(c) - 1:
#             finished = True

#     return jumps

def jumpingOnClouds(c):
    jumps = 0
    idx = 0

    while idx < len(c) - 1:
        if idx + 2 < len(c) and c[idx+2] == 0:
            idx += 2
            jumps += 1
        else:
            idx += 1
            jumps += 1
    return jumps


def repeatedString(s, n):
    length = len(s)
    times = n // length
    remainder = n % length
    count = 0

    for char in s:
        if char == 'a':
            count += 1

    count = (count * times)

    for i in range(remainder):
        if s[i] == 'a':
            count += 1

    return count
