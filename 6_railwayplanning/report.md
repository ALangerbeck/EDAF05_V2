Report Lab 6: Railway planning
==============================
# Implementation
Ford-Fulkersson with Bfs -> Edmondkarp

# What is the time complexity, and more importantly why?
O(|V||E|^2)  (bfs O(E)) to find 1 augmentation o(EV) number of augmentations found, Edges, the maximum path lenght
Worst case, bfs takes O(e) and the algorithm goes through every node for a shortest path, and does this for all paths up
to the longest one V, Ie, O(VE^2)
# Which other (well-known) algorithmic problems can be solved using Network-Flow?
Ford-fulkersson, preflow-push
# If the capacities of the edges are very large, how can one get a different(better) time complexity?
Edmond Karp dose not care about the capacity of the edges, but if one had done a Ford-Fulkersson i would
sugest using edmond-karp, Since the bfs avoids the worst case scenario of only pushing flow incrementaly
