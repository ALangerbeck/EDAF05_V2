# is your solution recursive or iterative?
Solution is recursive, but the actual work, i.e the construction of the matix is iterative

# What is the time complexity, and more importantly why?
O(m*n) since that is the time for constructing the "alignment matrix"

# What would the time complexity of a recursive solution without cache be?
since we would need to make 3 choices for every lette perhaps O(N³) with n being the lenght of the longes word?

# Can you think of any applications of this type of string alignment?
Dna matching bioinformatics, spell checking (missing letter)

# What could the costs represent in the applications?
likelyhood of letters being misstyped, difficulty to align, 
