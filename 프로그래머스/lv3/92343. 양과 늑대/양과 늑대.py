from collections import *

def solution(info, edges):
    answer = []
    tree = defaultdict(list)

    # init tree
    for edge in edges:
        tree[edge[0]].append(edge[1])

    visited = [0] * len(info)
    visited[0] = 1

    def dfs(sheep, wolf):
        if wolf >= sheep:
            return
        else:
            answer.append(sheep)
        for i in range(len(visited)):
            if visited[i]:
                for v in tree[i]:
                    if not visited[v]:
                        visited[v] = 1
                        is_wolf = info[v]
                        dfs(sheep, wolf+1) if is_wolf else dfs(sheep+1, wolf)
                        visited[v] = 0

    dfs(1, 0)
    return max(answer)