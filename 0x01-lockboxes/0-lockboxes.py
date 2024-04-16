#!/usr/bin/python3
""" Implementing solution for lockboxes problem
"""


def canUnlockAll(boxes):
    bfsInfo = []
    queue = []
    for i in range(len(boxes)):
        bfsInfo.append({"distance": None, "predecessor": None})
    bfsInfo[0]["distance"] = 0
    queue.append(0)

    while len(queue) != 0:
        u = queue.pop(0)
        for i in range(len(boxes[u])):
            v = boxes[u][i]
            if v < len(boxes):
                if bfsInfo[v]["distance"] is None:
                    bfsInfo[v]["distance"] = bfsInfo[u]["distance"] + 1
                    bfsInfo[v]["predecessor"] = u
                    queue.append(v)
    for i in range(len(bfsInfo)):
        if bfsInfo[i]["distance"] is None:
            return False
    return True
