def isSymmetric(root: TreeNode) -> bool:
    """
    基于迭代的算法，空间复杂度随着树的高度指数增加，速度一般
    """
    node_list = [root]
    while any(node_list):
        tmp = []
        vals = []
        for node in node_list:
            if node.left:
                vals.append(node.left.val)
            else:
                vals.append(None)
            if node.right:
                vals.append(node.right.val)
            else:
                vals.append(None)
            tmp.append(node.left)
            tmp.append(node.right)
        if vals[:] != vals[::-1]:
            return False
        node_list = tmp
    return True    
    
