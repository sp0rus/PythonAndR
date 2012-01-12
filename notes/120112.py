# Notes
# January 12, 2012

#Clustering
#   - minimum spanning tree clustering algorithm
#   - k means clustering ("center seekers")
#   - kNN -> k Nearest Neighbors
#       - validation set with known classes
#       - test set with unknown classes

#Clustering Evaluations
#   - mass of cluster: number of elements in that cluster
#   - radius of a cluster: average distance from the center of the cluster
#       - essentially, standard deviation
#   - good: clearly defined clusters with no overlap


###############################################################################

# Dot product
import numpy as np

def dot(A, B):
    EAB = sum(A*B)
    EAA = sum(A*A)
    EBB = sum(B*B)
    return EAB / np.sqrt(EAA) * np.sqrt(EBB))
