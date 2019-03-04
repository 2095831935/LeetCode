def construct_recursion(preorder, l_pre, r_pre, inorder, l_in, r_in, index):
    if l_pre == r_pre:
        # single node & end recursion
        return TreeNode(preorder[l_pre])
    elif l_pre > r_pre:
        # prevent outing of range
        return None
    val = preorder[l_pre]
    root = TreeNode(val)
    i = index[val]
    d_pre_in = i - l_in
    root.left = construct_recursion(preorder, l_pre+1, l_pre+ d_pre_in, inorder, l_in, i-1, index)
    root.right = construct_recursion(preorder, l_pre+ d_pre_in+1, r_pre, inorder, i+1, r_in, index)
    return root
def buildTree(preorder, inorder):
    """
    ps: 没有重复的元素
    """
    if preorder:
        index = {value:index for index, value in enumerate(inorder)}
        root = construct_recursion(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, index)
        return root
    else:
        return None
