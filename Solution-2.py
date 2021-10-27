def minSwap(arr, n):
    ans = 0
    t = arr.copy()
    d = {}
    t.sort()
    for i in range(n):
        d[arr[i]] = i
    init = 0
    for i in range(n):
        if (arr[i] != t[i]):
            ans += 1
            init = arr[i]
            arr[i], arr[d[t[i]]] = arr[d[t[i]]], arr[i]
            d[init] = d[t[i]]
            d[t[i]] = i
    return ans

n = int(input().strip())
arr = []
for i in range(n):
    x = int(input().strip())
    arr.append(x)
print(minSwap(arr, n))