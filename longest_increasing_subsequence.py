
def lis(A):
    max_lens = [1]
    for i in range(1,len(A)):
        candidates = filter(lambda j: A[j] < A[i], xrange(i))
        candidates_lens = [max_lens[j] for j in candidates]
        if len(candidates) > 0:
            max_lens.append( max(candidates_lens) + 1 )
        else:
            max_lens.append( 1 )
    return max(max_lens)

print( lis([0,2,-1,3,1000,4]) )
print( lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6 )

# https://www.interviewbit.com/problems/longest-increasing-subsequence/
