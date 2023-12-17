# [
#   "C...R............G......", // 0 initial state as passed
#   ".C..R............G......", // 1
#   "..C.R............G......", // 2
#   "...CR............G......", // 3
#   "...CR............G......", // 4
#   "....C............O......", // 5 show the car, not the light
#   "....GC...........R......", // 6
#   "....G.C..........R......", // 7
#   "....G..C.........R......", // 8
#   "....G...C........R......", // 9
#   "....O....C.......R......"  // 10
# ]

def traffic_lights(road, n):
    road1 = list(road)
    count = 0
    for i in range(1, len(road1)):
        if i == ".":
            road1[i] == road1[i - 1]
        elif i == "R" and count == 5:

    return [road1]

road = "C...R............G......"
n = 10
print(traffic_lights(road, n))