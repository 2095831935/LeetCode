def levelOrder(root):
    if not root:
        return []
    stack = [root]
    ans = []
    while stack:
        tmp = []
        level_val = []
        for node in stack[:]:
            level_val.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        stack = tmp
        ans.append(level_val)
    return ans
