def dfs(root, level, res):
    if not root: 
        return
    if len(res) < level+1:
        res.append([])
    res[level].append(root.val)
    dfs(root.left, level+1, res)
    dfs(root.right, level+1, res)
    

def levelOrder(root):
    if not root:
        return []
    dfs(root, 0, res=[])
    return res
