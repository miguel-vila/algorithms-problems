# detect a loop on a linked list @TODO

class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next
        self.visited = False

C = Node('C',None)
E = Node('E',C)
D = Node('D',E)
B = Node('B',C)
A = Node('A',B)
Z = Node('Z',A)
C.next = D

def detect_loop(start):
    if start == None or start.next == None or start.next.next == None:
        return None
    current = start
    forward = start.next.next

    loop_elem = None
    while True:
        if current == None or forward == None or forward.next == None or forward.next.next == None:
            return None
        if forward.visited:
            print("found!")
            loop_elem = forward
            break
        current.visited = True

        current = current.next
        forward = forward.next.next
    return loop_elem
