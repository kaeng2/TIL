N, M = map(int, input().split())
never_heard = [input() for _ in range(N)]
never_seen = [input() for _ in range(M)]
nv_h_s = list(set(never_heard) & set(never_seen))
print(len(nv_h_s), *sorted(nv_h_s), sep='\n')