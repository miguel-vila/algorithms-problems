
def build_graph_adj(projects, deps):
    adj = {}
    for a,b in deps:
        if a not in adj:
            adj[a] = [b]
        else:
            adj[a].append(b)
    return adj, projects

def build_graph_mat(projects, deps):
    mat = {}
    for a,b in deps:
        if a not in mat:
            mat[a] = {}
        mat[a][b] = True
    return mat

def nodes_without_incoming_(projects, mat):
    result = []
    for p in projects:
        if p not in mat:
            result.append(p)
    return result

def nodes_without_incoming(projects, deps):
    s = set()
    for a, b in deps:
        s.add(b)
    return set(projects) - s

def has_incoming_edges(n, mat):
    for m,p in mat.iteritems():
        if n in p and p[n]:
            return True
    return False

def topological_sort(mat, projects, deps):
    s = nodes_without_incoming(projects, deps)
    sort = []
    while len(s) != 0:
        n = s.pop()
        sort.append(n)
        if n not in mat:
            continue
        for m in mat[n]:
            mat[n][m] = False
            if not has_incoming_edges(m,mat):
                s.add(m)
    print(sort)
    if len(sort) != len(projects):
        raise Exception("there was a cycle")
    return sort

def build_order(projects, deps):
    mat = build_graph_mat(projects, deps)
    return topological_sort(mat, projects, deps)

projects = ['a','b','c','d','e','f']
deps = [
    ('a','d'),
    ('f','b'),
    ('b','d'),
    ('f','a'),
    ('d','c')
]

print(build_order(projects, deps))
    
