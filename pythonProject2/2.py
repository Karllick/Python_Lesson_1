arr = [i**3 for i in range(1, 1001, 2)]
result1 = 0
result2 = 0
for i, val in enumerate(arr):
    res = 0
    while val > 0:
        res += val % 10
        val //= 10
    if res % 7 == 0:
        result1 += arr[i]
print(result1)
arr = [i+17 for i in arr]
for i, val in enumerate(arr):
    res = 0
    while val > 0:
        res += val % 10
        val //= 10
    if res % 7 == 0:
        result2 += arr[i]
print(result2)

