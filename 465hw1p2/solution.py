
#Author: Rohit Gohel, Shravan Suresh and Trisha Mandal

# Merging Algorithm given in class
def merge_sorted_arrays(A,B):
    C = []
    i = 0
    j = 0
    m = len(A)
    n = len(B)
    A.append(2147483648)
    B.append(2147483648)
    for k in range(m+n):
        if A[i] < B[j]:
            C.append(A[i])
            i = i + 1
        else:
            C.append(B[j])
            j = j+1
    return C

# From algorithm done in class
def merge_sort(A,n):
    if n<=1:
        return A
    p1 = merge_sort(A[:n//2], len(A[:n//2]))
    p2 = merge_sort(A[n//2:], len(A[n//2:]))
    return merge_sorted_arrays(p1,p2)

n = int(input())
A = input().split()

A = [int(a) for a in A]

A = merge_sort(A,n)

for a in A:
    print(a, end = " ")
