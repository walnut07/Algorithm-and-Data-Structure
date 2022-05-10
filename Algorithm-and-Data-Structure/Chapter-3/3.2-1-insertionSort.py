# May 10 2022
# 24 minutes
N = int(input())
A = list( map(int, input().split()) )

# print the original array
for k in range(len(A) - 1):
    print(A[k], end=" ")
print(A[-1])

# insertionSort
for i in range(1, N): # start with index-1 because index-0 is sorted 
    v = A[i] # unsorted value
    j = i - 1 # index of the last value in the sorted part

    while v < A[j] and j >= 0:
        A[j + 1] = A[j]
        j -= 1
    
    A[j + 1] = v
    for k in range(len(A) - 1):
        print(A[k], end=" ")
    print(A[-1])


# python3 3.2-1-insertionSort.py