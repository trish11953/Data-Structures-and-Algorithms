#Done by Trisha Mandal, Rohit Ghoel,Sharvan Suresh

from bisect import insort

nv, ne = input().split(" ")
nv = int(nv)
ne = int(ne)


adjList = [[] for i in range(nv + 1)]
reverseadjList = [[] for i in range(nv + 1)]

for i in range(0, ne):
    tempa, tempb = input().split(" ")
    # print(tempa, tempb)
    tempa = int(tempa)
    tempb = int(tempb)
    insort(adjList[tempa], tempb)
    insort(reverseadjList[tempb], tempa)

print(adjList)
print(reverseadjList)


def explore(v, visited):
    visited[v] = 1
    for j in adjList[v]:
        if visited[j] == 0:
            explore(j, visited)


def explorewithTiming(v, clock, visited, pre, post, postlist):
    # print("in")
    visited[v] = 1
    pre[v] = clock
    clock[0] += 1
    # print("in explore", visited)
    for j in reverseadjList[v]:
        if visited[j] == 0:
            explorewithTiming(j, clock, visited, pre, post, postlist)
    post[v] = clock
    clock[0] += 1
    postlist.append(v)


def DFSwithTiming():
    postlist = []
    clock = [1]
    visited = [0 for i in range(nv + 1)]
    pre = [0 for i in range(nv + 1)]
    post = [0 for i in range(nv + 1)]
    for i in range(1, nv + 1):
        if visited[i] == 0:
            explorewithTiming(i, clock, visited, pre, post, postlist)
    return postlist


def specificOrder():
    postlist = DFSwithTiming()
    postlist.reverse()
    return postlist


def DFS():
    num_cc = 0
    visited = [0 for i in range(nv + 1)]
    #print(visited)
    for b in specificOrder():
        if visited[b] == 0:
            num_cc += 1
            explore(b, visited)
    return num_cc


print(DFS())
