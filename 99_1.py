def recoverTree(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    stack = []
    swapnode = [] # 保存逆序对的结果
    res = TreeNode(float("-inf"))
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if res.val > root.val:
            swapnode.append(res)
            swapnode.append(root)
            if len(swapnode) == 4: # 若有二个逆序对
                tmp = swapnode[0].val
                swapnode[0].val = swapnode[-1].val
                swapnode[-1].val = tmp
                return
        res = root
        root = root.right
    if len(swapnode) == 2:# 若有一个逆序对
        tmp = swapnode[0].val
        swapnode[0].val = swapnode[-1].val
        swapnode[-1].val = tmp
        return
