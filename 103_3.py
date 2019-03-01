def zigzag(root, res, level):
    if root == None:
        return
    if len(res) == level:
        res.append([])
    if level%2 == 0:
        res[level].append(root.val)
    else:
        res[level].insert(0, root.val)
    zigzag(root.left, res, level+1)
    zigzag(root.right, res, level+1)
    
def zigzagLevelOrder(root):
    if root == None:
        return []
    res = []
    zigzag(root, res, 0)
    return res
