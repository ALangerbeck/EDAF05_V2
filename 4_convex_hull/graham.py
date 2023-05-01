import sys

DEBUG = False

def dprint(text:str):
    if DEBUG:
        print(text)


def read_points():
    dimensions,nbr_of_points = sys.stdin.readline().split(" ")
    dprint("N = "+ nbr_of_points)
    for line in sys.stdin:
        inputs = line.split(" ")
       dprint("x: " + inputs[0] +  " y: " + inputs[1])  

def main():
    read_points()
    
if __name__ == "__main__":
    main()
