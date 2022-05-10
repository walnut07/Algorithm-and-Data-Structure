# May 10th 2022
# 35 minutes
N = int(input())
A = list( map(int, input().split()) )

# selection sort 
count = 0

for i in range(N): 
    min = i # is going to be the index of the smallest element in the unsorted ones
    for j in range(i, N):
        if A[j] < A[min]:
            min = j # the index of minimum element
    A[i], A[min] = A[min], A[i]
    if i != min:
        count += 1

for i in range(N - 1):
    print(A[i], end=" ")
print(A[-1])

print(count)
# python3 3.4-1-selectionSort.py