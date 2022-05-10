# May 10th 2022 
# 30 minutes

n = int(input())


minv = int(input())
maxv = -float("inf")

for i in range(n - 1):
    r = int(input())
    maxv = max(maxv, r - minv)
    minv = min(minv, r)

print(maxv)

# python3 2.5-1-introduction.py