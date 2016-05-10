def preorder(tree):
    if isinstance(tree, tuple):
        lhs = tree[1]
        exp = tree[0]
        rhs = tree[2]
        return lhs + preorder(exp) + preorder(rhs)
    return tree

def postorder(tree):
    if isinstance(tree, tuple):
        lhs = tree[1]
        exp = tree[0]
        rhs = tree[2]
        return postorder(exp) + postorder(rhs) + lhs
    return tree

def inorder(tree):
    if isinstance(tree, tuple):
        lhs = tree[1]
        exp = tree[0]
        rhs = tree[2]
        return inorder(exp) + lhs + inorder(rhs)
    return tree

#print(preorder((('1', '*', '2'), '+', (('3', '+', '4'), '*', '5'))))
#print(postorder((('1', '*', '2'), '+', (('3', '+', '4'), '*', '5'))))
#print(inorder((('1', '*', '2'), '+', (('3', '+', '4'), '*', '5'))))
