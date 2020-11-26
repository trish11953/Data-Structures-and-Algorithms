
#Author: Rohit Gohel, Shravan Suresh and Trisha Mandal

# Merging Algorithm given in class
def sort_count(A,B):
    C = []
    curr = 0
    prev = 0
    tot = 0
    i = 0
    j = 0
    m = len(A)
    n = len(B)
    A.append(2147483648)
    B.append(2147483648)
    for k in range(m+n):
        if A[i] < B[j]:
            C.append(A[i])
            tot = tot + prev + curr
            prev += curr
            curr = 0
            i = i + 1
        else:
            C.append(B[j])
            curr += 1
            j = j+1
    return C, tot

# From algorithm done in class
def count(A,n):
    if n<=1:
        return A, 0
    p1, p1count = count(A[:n//2], len(A[:n//2]))
    p2, p2count = count(A[n//2:], len(A[n//2:]))
    p, pcount = sort_count(p1,p2)
    total = pcount + p1count + p2count
    return p,total

n = int(input())
A = input().split()

A = [int(a) for a in A]

A,count = count(A,n)

print(count)
