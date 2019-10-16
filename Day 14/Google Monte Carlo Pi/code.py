#! python3
import random
import sys

# Lambda functions
liesInCircle = lambda point_x, point_y : point_x**2 + point_y**2 <= 1
plotPoint = lambda limit : (random.randrange(-1*limit, limit+1)/limit , random.randrange(-1*limit, limit+1)/limit)

# lambda functions as general functions

# def liesInCircle(point_x, point_y):
#     return point_x**2 + point_y**2 <= 1

# def plotPoint(limit):
#     return (random.randrange(-1*limit, limit+1)/limit , random.randrange(-1*limit, limit+1)/limit)

# Variables
try:
    if sys.argv[1]:
        total_points = int(sys.argv[1])
        print(f"[+] Amount of total points is set to {sys.argv[1]}")
except:
    print("[+] Since no input is provided, Amount of total points is set to default value of 10000")
    total_points = 10000
points_in_circle = 0

# Script
for _ in range(total_points):
    x , y = plotPoint(total_points**2)
    if liesInCircle(x,y):
        points_in_circle += 1
pi = 4 * (points_in_circle / total_points)
print(f"Estimation of pi: \t {str(pi)}")
