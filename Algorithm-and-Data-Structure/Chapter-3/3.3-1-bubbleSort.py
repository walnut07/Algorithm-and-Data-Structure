# May 10th 2022
# 30 minutes

N = int(input())
A = list( map(int, input().split()) )

# bubble sort
count_swap = 0
flag = True
sort_tail = 0

while flag == True:
    flag = False
    for i in range(N-1, sort_tail, -1):
        if A[i] < A[i-1]: 
            A[i], A[i - 1] = A[i - 1], A[i]
            flag = True
            count_swap += 1
    sort_tail += 1

for i in range(N - 1):
    print(A[i], end=" ")
print(A[-1])
print(count_swap)

# python3 3.3-1-bubbleSort.py