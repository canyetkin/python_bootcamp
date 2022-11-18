#find the longest contiguous subsequence in a rising sequence in Python.

A = [5,6,7,8,9,13,15,16,17,18,19,20,21,22,23]
diff = [j-i for i,j in zip(A, A[1:])]
splits = [[A[0]]]
for x,d in zip(A[1:], diff):
    if d == 1:
        splits[-1].append(x)
    else:
        splits.append([x])
out = max(splits, key=len)

print(out)


#code below is same with above

sayilar = [1,13,2,11,5,3,8,12,4,6,17,19,14,15,16,17,18]

def fy(A):
    A.sort()
    diff=[]
    splits=[[A[0]]]
    for i,j in zip(A,A[1:]):
        diff.append(j-i)
    for x,d in zip(A[1:],diff):
        if d == 1:
            splits[-1].append(x)
        else:
            splits.append([x])       
    out= max(splits,key=len)
    print(out)
fy(sayilar)