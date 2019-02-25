def isSameTree(p: 'TreeNode', q: 'TreeNode') -> 'bool':
    # 基于递归进行判断，其时间复杂度较高
    if p is None or q is None:
        if p is None and q is None:
            return True
        else:
            return False
    if p.val == q.val:
        if isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
            return True
        else:
            return False
    else:
        return False
