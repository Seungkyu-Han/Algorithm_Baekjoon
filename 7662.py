import sys
import heapq

cnt = int(sys.stdin.readline())
for i in range(cnt):
    maxheap = []
    minheap = []
    num = int(sys.stdin.readline())
    seq = [False] * num
    for t in range(num):
        ans = list(sys.stdin.readline().split())
        if ans[0] == 'I':
            heapq.heappush(maxheap, (int(ans[1]) * -1, t))
            heapq.heappush(minheap, (int(ans[1]), t))
            seq[t] = True
        else:
            if ans[1] == '-1':
                if not minheap:
                    continue
                tmp = heapq.heappop(minheap)
                while not seq[tmp[1]] and minheap:
                    tmp = heapq.heappop(minheap)
                if seq[tmp[1]]:
                    seq[tmp[1]] = False
            else:
                if not maxheap:
                    continue
                tmp = heapq.heappop(maxheap)
                while not seq[tmp[1]] and maxheap:
                    tmp = heapq.heappop(maxheap)
                if seq[tmp[1]]:
                    seq[tmp[1]] = False
    if len(maxheap) < 1 or len(minheap) < 1:
        print('EMPTY')
        continue
    maxtmp = heapq.heappop(maxheap)
    mintmp = heapq.heappop(minheap)
    while not seq[maxtmp[1]] and maxheap:
        maxtmp = heapq.heappop(maxheap)
    while not seq[mintmp[1]] and minheap:
        mintmp = heapq.heappop(minheap)
    if seq[maxtmp[1]] is not False and seq[mintmp[1]] is not False:
        print(f'{maxtmp[0] * -1} {mintmp[0]}')
    else:
        print('EMPTY')
