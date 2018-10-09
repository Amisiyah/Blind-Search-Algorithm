import sys

# Breadth First Search
# Depth First Search
def get_breadth_first_nodes(root):
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node)
        for child in cur_node.get_children():
            stack.append(child)
    return nodes


def get_depth_first_nodes(root):
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node)
        for child in cur_node.get_rev_children():
            stack.insert(0, child)
    return nodes


class Node(object):
    def __init__(self, id_):
        self.id = id_
        self.children = []

    def __repr__(self):
        return "Node: [%s]" % self.id

    def add_child(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children

    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children


def println(text):
    sys.stdout.write(text + "\n")


def make_tree():
    a0 = Node("a0")
    b0 = Node("b0")
    b1 = Node("b1")
    b2 = Node("b2")
    c0 = Node("c0")
    c1 = Node("c1")
    d0 = Node("d0")

    a0.add_child(b0)
    a0.add_child(b1)
    a0.add_child(b2)

    b0.add_child(c0)
    b0.add_child(c1)

    c0.add_child(d0)

    return a0


def breadth_first_nodes():
    root = make_tree()
    node_list = get_breadth_first_nodes(root)
    for node in node_list:
        println(str(node))


def depth_first_nodes():
    root = make_tree()
    node_list = get_depth_first_nodes(root)
    for node in node_list:
        println(str(node))


if __name__ == "__main__":
    breadth_first_nodes()
    println("")
    depth_first_nodes()
    println("")




# Iterative Deepening Search
# Depth Limited Search
'''graph = {
    'a' : ['b', 'c', 'e'],
    'b' : ['d', 'f'],
    'c' : ['g'],
    'e' : ['f'],
    'f' : ['e'],
}'''

graph = {
    1: [2, 9],
    2: [3, 8],
    9: [10, 11],
    3: [4, 7],
    4: [5, 6]
}


def iterative_deepening_search(root, goal):
    depth = 0
    while True:
        print("Looping at depth %i " % depth)
        result = depth_limited_search(root, goal, depth)
        print("Result: %s, Goal: %s" % (result, goal))
        if result == goal:
            return result
        depth = depth + 1


def depth_limited_search(node, goal, depth):
    print("node: %s, goal %s, depth: %i" % (node, goal, depth))
    if depth == 0 and node == goal:
        print(" --- Found goal, returning --- ")
        return node
    elif depth > 0:
        print("Looping through children: %s" % (graph.get(node, [])))
        for child in graph.get(node, []):
            if goal == depth_limited_search(child, goal, depth-1):
                return goal


iterative_deepening_search(1, 2)

# iterative_deepening_search('a', 'g')
