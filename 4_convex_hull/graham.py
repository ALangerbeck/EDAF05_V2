from array import array
import sys
import numpy as np

DEBUG = True

def dprint(text:str):
    if DEBUG:
        print(text)


def read_points():
    dprint("Started Reading Data")
    dimensions,nbr_of_points = sys.stdin.readline().split(" ")
    dprint("N = "+ nbr_of_points)
    points = []
    only_int = True
    y_min = float("inf")
    index_y_min = 0
    for line in sys.stdin:
        inputs = line.split(" ")
        x = float.fromhex(inputs[0])
        y = float.fromhex(inputs[1])
        points.append((x,y))
        only_int = only_int and  x.is_integer() and y.is_integer
        dprint(f"x: {x}  y: {y}")

    return nbr_of_points,points,index_y_min,only_int

def get_angle(tuple):
    return -tuple[0]


def graham_scan(nbr_of_points, index_y_min,points):
    n = nbr_of_points
    i = index_y_min
    p0 = points.pop(i)
    adjusted_points = np.array(points) - p0
    adjusted_points = sorted(adjusted_points, key=get_angle)
    print(adjusted_points)
    

def main():
    nbr_of_points, points, index_y_min, only_int = read_points()
    dprint(f"There are {nbr_of_points.strip()} number of points")
    if only_int :
        dprint("They are all integers")
    graham_scan(nbr_of_points, index_y_min, points)

    
if __name__ == "__main__":
    main()
