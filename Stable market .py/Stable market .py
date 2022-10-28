def no_of_stable_blocks(A,k):

    b=[1]

    count=1

    for i in range(1,len(A[1:])+1):

        if A[i]==A[i-1]:

            count=count+1

            b.append(count)

        else:

            count=1

            b.append(count)

    return b.count(k)     

if __name__ == '__main__':

    t=int(input())

    for _ in range(t):

        N,Q=map(int,input().split())

        A=list(map(int,input().split()))

        for i in range(Q):

            l,r,k=map(int,input().split())

            print(no_of_stable_blocks(A[l-1:r],k))

        
