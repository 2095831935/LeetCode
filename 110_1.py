def depth(root):
    if not root:
        return 0
    return 1 + max(depth(root.left), depth(root.right))

def isBalanced(root):
    if not root:
        return True
    if abs(depth(root.left) - depth(root.right)) > 1:
        return False
    else:
        if isBalanced(root.left) and isBalanced(root.right):
            return True
        else:
            return False
