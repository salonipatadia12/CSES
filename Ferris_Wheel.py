n, x = map(int, input().split())
p = sorted(list(map(int, input().split())))

a = 0
b = n-1
ans = 0
while(a < b):
    if p[a] + p[b] <= x:
        ans += 1
        a += 1
        b -= 1
    else:
        if p[b] <= x:
            ans += 1
        b -= 1

if a == b and p[a] <x:
    ans += 1

print(ans)
