def dfs(root, level, res):
    if not root: 
        return
    if len(res) < level+1:
       res.insert(0, [])
    dfs(root.left, level+1, res)
    dfs(root.right, level+1, res)
    res[len(res) - level-1].append(root.val)

def levelOrder(root):
    if not root:
        return []
    res = []
    dfs(root, 0, res)
    return res
