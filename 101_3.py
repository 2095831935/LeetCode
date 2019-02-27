def isSymmetric(root: TreeNode) -> bool:
    if root == None:
        return True
    stack = [root.left, root.right]
    while stack:
        tmp2 = stack.pop()
        tmp1 = stack.pop()
        if not tmp1 and not tmp2:
            continue
        if not tmp1 or not tmp2:
            return False
        if tmp1.val != tmp2.val:
            return False
        stack.append(tmp1.left)
        stack.append(tmp2.right)
        stack.append(tmp1.right)
        stack.append(tmp2.left)
    return True
