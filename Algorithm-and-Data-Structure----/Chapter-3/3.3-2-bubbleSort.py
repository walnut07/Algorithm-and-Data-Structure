# May 10th 2022
# 15 minutes

N = int(input())
A = list(map(int, input().split()))

# bubble sort 
sorted_tail = 0
count = 0
flag = True
while flag:
    flag = False
    for i in range(N-1, sorted_tail, -1):
        if A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
            flag = True
            count += 1
    sorted_tail += 1

for i in range(N - 1):
    print(A[i], end=" ")
print(A[-1])

print(count)

# python3 3.3-2-bubbleSort.py