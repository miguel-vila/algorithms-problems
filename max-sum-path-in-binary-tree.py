class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

t1 = TreeNode(2)
l1 = TreeNode(1)
l2 = TreeNode(3)
t1.left = l1
t1.right = l2

class Solution:
    def is_leaf(self,T):
        return T.left == None and T.right == None

    def maxPathSum(self, T):
        if self.is_leaf(T):
            return T.val
        else:
            candidates = [T.val]
            left_answer = None
            right_answer = None
            if T.left != None:
                left_answer = self.maxPathSum(T.left)
                candidates.append( left_answer )
                candidates.append( left_answer + T.val )
            if T.right != None:
                right_answer = self.maxPathSum(T.right)
                candidates.append( right_answer )
                candidates.append( right_answer + T.val )
            if left_answer != None and right_answer != None:
                candidates.append( left_answer + T.val + right_answer )
            return max(candidates)

s = Solution()

#[-100, -200, -1, -300, -400, -1, -1, -1, -1]

#         -100
#          / \
#       -200 null
#        / \
#     -300 -400

t = TreeNode(
    -100,
    TreeNode(
        -200,
        TreeNode(-300),
        TreeNode(-400)
    ),
    None
)

print( s.maxPathSum(t1) )
print( s.maxPathSum(t) )
