def find_all_green_time(N, T, A):
    for t in range(T):
        all_green = True
        for n in range(N):
            if A[n][t] == 0:
                all_green = False
                break
        if all_green:
            return t
    return -1

N = int(input())
T = int(input())

A = []
for i in range(N):
    row = list(map(int, input().replace(",", " ").split()))
    if len(row) != T:
        exit(1)
    A.append(row)

print(find_all_green_time(N, T, A)) 

