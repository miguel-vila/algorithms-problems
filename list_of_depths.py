
class TreeNode:

    def __init__(self,data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def right_to_left_children(self):
        children = []
        if self.right != None:
            children.append(self.right)
        if self.left != None:
            children.append(self.left)
        return children

    def __repr__(self):
        return str(self.data)

class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data) + " -> " + str(self.next)

    
def depths(T):
    frontier = T.right_to_left_children()
    depths = [ Node(T,None) ]
    while len(frontier) != 0:
        next_frontier = []
        current_node = None
        for f in frontier:
            current_node = Node(f, current_node)
            for c in f.right_to_left_children():
                next_frontier.append(c)
        depths.append(current_node)
        frontier = next_frontier
    return depths

def Leaf(data):
    return TreeNode(data,None,None)
        
T = TreeNode(
    1,
    TreeNode(
        2,
        Leaf(4),
        TreeNode(
            5,
            None,
            Leaf(7)
        )
    ),
    TreeNode(
        3,
        TreeNode(
            6,
            None,
            Leaf(8)
        ),
        None
    )
)

print(depths(T))
