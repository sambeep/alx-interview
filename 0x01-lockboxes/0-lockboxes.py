#!/usr/bin/python3
"""Solution to Lockboxes problem"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if (type(boxes) is not list or len(boxes) == 0):
        return False
    for n in range(1, len(boxes) - 1):
        unlocked = False
        for i in range(len(boxes)):
            unlocked = n in boxes[i] and n != i
            if unlocked:
                break
        if unlocked is False:
            return unlocked
    return True
