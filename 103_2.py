def zigzagLevelOrder(root):
    if not root:
        return []
    stack = [root]
    ans = []
    direction = 0
    while stack:
        tmp = []
        level_val = []
        for node in stack[:]:
            if (-1)**direction == 1:
                level_val.append(node.val)
            else:
                level_val.insert(0, node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        stack = tmp
        ans.append(level_val)
        direction += 1
    return ans
