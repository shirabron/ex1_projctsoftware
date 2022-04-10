import math
from operator import le
import sys

from matplotlib import lines


def main(K,max_iter,input,output):
    K = int(input())
    numOfArgs = len(sys.argv)
    if numOfArgs == 3:
        max_iter = 200
    elif numOfArgs == 4:
        max_iter = input
    else:
        print("Invalid Input!")
    input = input()
    output = input()
    vectors = readInput(input)
    if validityOfK(K,len(vectors))==False:
        print("Invalid Input!")
    centroids = intializeCentroids(vectors,K)

    for i in range(max_iter):
        clusters = []
        num_of_unchanged_centorids = 0
        for i in range(len(vectors)):
            assignVectorToCluster(vectors,centroids,clusters,i)
        for i in range(K):
            old_centroid = centroids[i]
            updateCentroid(vectors,centroids,clusters,i)
            new_centroid = centroids[i]
            if euclideanDistance(old_centroid,new_centroid)<0.001:
                num_of_unchanged_centorids+=1
        if num_of_unchanged_centorids==K:
            break
    return (writeToOutput(output,centroids))

    
            
# checking in the size of k is valid
def validityOfK(k,n):
    if 1<k and k<n:
        return True
    return False

# func to read data from file, return a list of lstsc(vectors = [],vectorCooirdinates = [])
def readInput(fileName):
    file = open(fileName,'r')
    lines = file.read().splitlines()
    file.close
    vectors = []
    for i in range(1,len(lines)):
        line = lines[i].split(',')
        v = []
        for j in range(len(line)-1):
            coordinate = float(line[j])
        vectors.append(v)

    return vectors  


# creates lst in length k, initialize with first k vectors
def intializeCentroids(vectors,k):
    centroids = []
    for i in range(k):
        centroids.append(vectors[i])
    return centroids

# calculates euclideanDistance between 2 vectors, returns dis
def euclideanDistance(x,y):
    sumOfSquaredDiffrence = 0
    for i in range(len(x)):
        sumOfSquaredDiffrence += math.pow(x[i]-y[i],2)
    return math.sqrt(sumOfSquaredDiffrence)

# updates and returns centroid
def updateCentroid(vectors,centroids,clusters,i):
    centroid=centroids[i]
    cluster=clusters[i]
    size = len(cluster)
    for j in range(len(centroid)):
        sum = 0
        for index in cluster:
            sum+=vectors[index][j]
        centroid[j]=sum/size
    return


# assigns vector to closest cluster
def assignVectorToCluster(vectors,centroids,clusters,vectorIndex):
    min = sys.float_info.max
    index = 0
    for i in range (len(centroids)):
        distance = euclideanDistance(vectors[vectorIndex],clusters[i])
        if distance<min:
            min = distance
            index = i
    clusters[index].append(vectorIndex)
    return

def writeToOutput(fileName,centroids):
    file = open(fileName,'r')
    str_centroids = ",".join(centroids)
    file.write(str_centroids)

if __name__ == "__kmeans__":
    main()