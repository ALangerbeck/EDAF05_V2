from array import array
import sys
import numpy as np
import matplotlib.pyplot as plt

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

    points[0],points[i] = points[i],points[0]

    p0 = points[0]
    for i in range(len(points)):
        new_x,new_y = points[i][0]-p0[0],points[i][1]-p0[1]
        points[i] = (new_x,new_y)
    
    #sorted_points = sorted(points, key=lambda p: (atan2(p[1] - p0[1], p[0] - p0[0]), p[0], p[1]))
    print(points)
    plot_points(points)
    
def plot_points(points):
    points = np.array(points)
    N = points.shape[0]
    fig, ax = plt.subplots()
    ax.scatter(points[:, 0], points[:, 1], s=1)
    if len(points) < 20:
        for i in range(N):
            ax.annotate(f"p{i}", points[i, :])
    #return fig, ax
    plt.show()
def main():
    nbr_of_points, points, index_y_min, only_int = read_points()
    dprint(f"There are {nbr_of_points.strip()} number of points")
    if only_int :
        dprint("They are all integers")
    graham_scan(nbr_of_points, index_y_min, points)

    
if __name__ == "__main__":
    main()
