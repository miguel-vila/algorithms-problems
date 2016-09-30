#Write a function that takes a list of numbers, and returns the longest consecutive sublist of strictly increasing or decreasing numbers.

#straight([1, 3, 3, 5, 6, 4, 2, 1, 7])
#-> [6, 4, 2, 1]
#([1, 3, 3, 5, 6] is not strictly increasing, because of the repeated 3s)
#If there are multiple increasing/decreasing sublists of the same length, return whichever one you like.

def find_max_index(A):
    max_index = 0
    for i in range(1,len(A)):
        if A[i] > A[max_index]:
            max_index = i
    return max_index

# O(n)
def straight(A):
    max_inc_subl_len   = [1]
    max_inc_subl_start = [0]
    max_dec_subl_len   = [1]
    max_dec_subl_start = [0]
    for i in range(1,len(A)):
        if A[i-1] != A[i]:
            if A[i-1] < A[i]:
                max_inc_subl_len.append( max_inc_subl_len[i-1] + 1 )
                max_inc_subl_start.append( max_inc_subl_start[i-1] )

                max_dec_subl_len.append( 1 )
                max_dec_subl_start.append( i )
            else:
                max_dec_subl_len.append( max_dec_subl_len[i-1] + 1 )
                max_dec_subl_start.append( max_dec_subl_start[i-1] )

                max_inc_subl_len.append( 1 )
                max_inc_subl_start.append( i )
        else:
            max_inc_subl_len.append( 1 )
            max_inc_subl_start.append( i )
            max_dec_subl_len.append( 1 )
            max_dec_subl_start.append( i )
    max_inc = find_max_index(max_inc_subl_len)
    max_dec = find_max_index(max_dec_subl_len)
    (max_end, max_inc_subl_start) = (max_inc, max_inc_subl_start) if max_inc_subl_len[ max_inc ] > max_dec_subl_len[ max_dec ] else (max_dec, max_dec_subl_start)
    max_start = max_inc_subl_start[ max_end ]
    return A[max_start : max_end+1]

print(straight([1, 3, 3, 5, 6, 4, 2, 1, 7]) == [6,4,2,1])
print(straight([1, 3, 7, 6, 4, 2, 1, 7]) == [7,6,4,2,1])
