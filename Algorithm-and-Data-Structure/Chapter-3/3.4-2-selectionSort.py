# May 10th 2022
# 12 minutes

N = int(input())
A = list(map(int, input().split()))

# selection sort 
count = 0
for i in range(N):
    min = i # the index of the minimum value
    for j in range(i, N):
        if A[min] > A[j]:
            min = j
    A[i], A[min] = A[min], A[i]
    if i != min:
        count += 1

for k in range(N - 1):
    print(A[k], end=" ")
print(A[-1])
print(count)

# python3 3.4-2-selectionSort.py