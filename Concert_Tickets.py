n,m = map(int,input().split())
actual = list(sorted(map(int, input().split())))
custom = list(map(int, input().split()))
actual.reverse()
for i in range(len(custom)):
    for j in range(len(actual)):
        if actual[j] <= custom[i]:
            print(actual[j])
            actual.remove(actual[j])
            break


