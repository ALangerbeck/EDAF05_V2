from array import array
from operator import truediv
import sys
import numpy as np
import matplotlib.pyplot as plt
import math

DEBUG = False

def dprint(text:str):
    if DEBUG:
        print(text)


p0 = 0

def read_points():
    dprint("Started Reading Data")
    dimensions,nbr_of_points = sys.stdin.readline().split(" ")
    dprint("N = "+ nbr_of_points)
    points = []
    only_int = True
    y_min = float("inf")
    x_min = float("inf")
    index_y_min = 0
    for i,line in enumerate(sys.stdin):
        inputs = line.split(" ")
        x = float.fromhex(inputs[0])
        y = float.fromhex(inputs[1])
        if y < y_min or (y == y_min and x < x_min):
            y_min = y
            x_min = x
            index_y_min = i 
        points.append((x,y))
        only_int = only_int and  x.is_integer() and y.is_integer
        dprint(f"x: {x}  y: {y}")


    return nbr_of_points,points,index_y_min,only_int




def direction(p1,p2,p3):
    # if the cross product area is positive or negative tell us in
    # the vectors are clockwise or counter clockwise of each other
    
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])
    
def polar_angle_and_distance(point):
    # Calculate polar angle and distance to the pivot
    angle = math.atan2(point[1] - p0[1], point[0] - p0[0])
    distance = math.dist(point, p0)
    return (angle, distance)

def graham_scan(nbr_of_points, index_y_min,points):
    n = nbr_of_points
    i = index_y_min
    dprint(f" Minimum y point is {points[i]}")
    points[0],points[i] = points[i],points[0]

    adj_points = points.copy()
    global p0
    p0 = adj_points[0]

    sorted_points = sorted(points[1:], key=polar_angle_and_distance)

    dprint(f"Sorted points: {sorted_points}")

    hull_stack = [p0,sorted_points[0]]

    for k in range(1,len(sorted_points)):
        pt = sorted_points[k]
        while direction(hull_stack[-2],hull_stack[-1],pt) <= 0:
            
            disc = hull_stack.pop()
            dprint(f"At point ({pt[0]},{pt[1]}) discarding ({disc[0]},{disc[1]})")
            if len(hull_stack) < 2:
                break
        hull_stack.append(pt)
        
        dprint(f"Adding {pt[0]},{pt[1]} to the stack")

    #for i in range(len(hull_stack)):
    #    hull_stack[i] = (hull_stack[i][0],hull_stack[i][1])
    
    n = len(hull_stack)

    return n, hull_stack
    
def plot_points(points):
    # Function to plot points without connecting lines
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    # Plot points as scatter
    plt.scatter(x, y, color='red')

    # Annotate points with their order in the list
    for i, p in enumerate(points):
        plt.annotate('p{}'.format(i), (p[0], p[1]), textcoords="offset points", xytext=(0,10), ha='center')

def plot_hull(points):
    
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    
    plt.scatter(x, y, color='red')

    # Plot lines between adjacent points
    for i in range(len(points) - 1):
        plt.plot([points[i][0], points[i+1][0]], [points[i][1], points[i+1][1]], color='blue')

    # Connect the last point to the first point
    plt.plot([points[-1][0], points[0][0]], [points[-1][1], points[0][1]], color='blue')

def reorder(hull):
    max_x = -float("inf")
    max_index = 0
    dprint(hull)
    hull.reverse()
    dprint(hull)
    
    for i in range(len(hull)):
        point = hull[i]
        if point[0] > max_x:
            max_x = point[0]
            max_index = i
    
    hull = hull[max_index:] + hull[:max_index]
    dprint(hull)
    return hull


def main():
    nbr_of_points, points, index_y_min, only_int = read_points()
    dprint(f"There are {nbr_of_points.strip()} number of points")
    if only_int :
        dprint("They are all integers")
    n,hull = graham_scan(int(nbr_of_points), index_y_min, points)
    
    print(n)
    
    r_hull = reorder(hull)
    
    if(DEBUG):
        plot_points(np.array(points))
        plot_hull(r_hull)
        plt.show()

    if only_int:
        for x,y in r_hull:
            print(f"{int(x)} {int(y)}")
    else:
        for x,y in r_hull:
            print(f"{x:.3f} {y:.3f}")


    
if __name__ == "__main__":
    main()
