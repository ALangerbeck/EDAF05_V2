from ctypes import sizeof
import sys
import numpy as np 
sys.setrecursionlimit(10**5)

DEBUG = False

PENTALY = -4

def dprint(text):
    if DEBUG:
        print(text)


def read_points():
    dprint("=== Started Reading Data ===")
    characters = sys.stdin.readline().strip().split(" ")
    letter_index = {}
    for i,key in enumerate(characters):
        letter_index[key] = i
    k = len(characters)

    dprint("== Included charateres == ")
    dprint(letter_index)
    dprint("== Number of characters ==")
    dprint(k)

    costs = np.zeros((k,k))
    
    for i in range(k):
        costs[i] = sys.stdin.readline().strip().split(" ")
        #dprint(sys.stdin.readline().strip().split(" "))

    dprint("== Costs array ==")
    dprint(costs) 
    dprint("=== Finnished reading data ===")

    nbr_of_queries = int(sys.stdin.readline().strip())

    dprint("== Number of queries ==")
    dprint(nbr_of_queries)
    
    queries = []

    for i in range(nbr_of_queries):
        queries.append(sys.stdin.readline().strip().split(" "))

    dprint("== Queries ==")
    dprint(queries)
    
    return letter_index,k,costs,nbr_of_queries,queries

def create_allignment_matrix(string_a,string_b,costs,letter_index):
    
    length_a = len(string_a)
    length_b = len(string_b)
    
    
    allignment_matrix = np.zeros((length_a + 1, length_b + 1) )
    
    for i in range(1,length_a+1):
        allignment_matrix[i][0] = allignment_matrix[i-1][0] + PENTALY
    
    for i in range(1,length_b+1):
        allignment_matrix[0][i] = allignment_matrix[0][i-1] + PENTALY


    for i in range(1,length_a + 1):
        for j in range(1,length_b + 1):
            
            index_a = letter_index[string_a[i-1]]
            index_b = letter_index[string_b[j-1]]
            
            #dprint(f"cost is {costs[index_a][index_b]}")

            allignment_matrix[i][j] = max(allignment_matrix[i-1][j-1] + costs[index_a][index_b],
                                          allignment_matrix[i][j-1] + PENTALY,
                                          allignment_matrix[i-1][j] + PENTALY)
            
    
    #dprint(allignment_matrix)
    return(allignment_matrix)




def solve(am,costs,letter_index,i,j,word_a,word_b,align_a="",align_b=""):

    if i == 0 and j == 0:
        return align_a,align_b

    #dprint(f"Currently at {i},{")
    #dprint(f"align: {align_a} {align_b}")

    index_a = letter_index[word_a[i-1]]
    index_b = letter_index[word_b[j-1]]
   
    
    #dprint(f"letters: {word_a[i-1]} and {word_b[j-1]}")

    if am[i-1][j-1] + costs[index_a][index_b] == am[i][j]:
        return solve(am,costs,letter_index,i-1,j-1,word_a,word_b,word_a[i-1] + align_a,
               word_b[j-1] + align_b)
    elif am[i][j-1] + PENTALY == am[i][j] :
        return solve(am,costs,letter_index,i,j-1,word_a,word_b,'*' + align_a,
               word_b[j-1] + align_b)
    elif am[i-1][j] + PENTALY == am[i][j] :
        return solve(am,costs,letter_index,i-1,j,word_a,word_b,word_a[i-1] + align_a,
               '*' + align_b)
    
def main():

    dprint("=== Begin Input Read ===")
    letter_index,k,costs,nbr_of_queries,queries = read_points()
    
    dprint("=== Starting Queries ===")
    
    for i,querie in enumerate(queries):
            dprint(f"Queriy {i} : {querie}")
            word_a = querie[0]
            word_b = querie[1]
            
            dprint(f"=== Calulating aligment matrrix for querie {i} ===")
            align_matrix = create_allignment_matrix(querie[0], querie[1],costs,letter_index)
            dprint(f"=== Start solvin querie {i} ===")
            output = solve(align_matrix,costs,letter_index,len(word_a),len(word_b),word_a,word_b)
            dprint(f"=== finished querie {i} ===")
            print(f"{output[0]} {output[1]}")

if __name__ == "__main__":
    main()
