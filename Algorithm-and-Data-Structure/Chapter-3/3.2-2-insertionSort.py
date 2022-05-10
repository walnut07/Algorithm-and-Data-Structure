# May 20th 2022
# 8 minutes

N = int(input())
A = list( map(int, input().split()) )

for i in range(len(A) - 1):
    print(A[i], end=" ")
print(A[-1])

for i in range(1, N):
    v = A[i] # the first element of unsorted elements
    j = i - 1 # the index of the last element of sorted elements

    while v < A[j] and j >= 0:
        A[j + 1] = A[j]
        j -= 1

    A[j + 1] = v
    for k in range(len(A) - 1):
        print(A[k], end=" ")
    print(A[-1])

# python3 3.2-2-insertionSort.py