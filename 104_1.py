def maxDepth(root: TreeNode) -> int:
    """
    递归算法
    """
    return 0 if root is None else max(maxDepth(root.left), maxDepth(root.right))+1
