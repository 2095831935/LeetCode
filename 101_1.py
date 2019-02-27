def _isSymmetric(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val) and _isSymmetric(p.left, q.right) and _isSymmetric(p.right, q.left)

def isSymmetric(root: TreeNode) -> bool:
    return _isSymmetric(root, root)
