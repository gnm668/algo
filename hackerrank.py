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
