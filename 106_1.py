def buildTree(inorder, postorder) -> TreeNode:
    """
    ps: 没有重复的元素
    """
    for i in range(len(inorder)):
        if inorder[i] == postorder[-1]:
            left_root  = buildTree(inorder[:i], postorder[0:i])
            right_root = buildTree(inorder[i+1:], postorder[i:-1])
            root = TreeNode(postorder[-1])
            root.left  = left_root
            root.right = right_root
            return root
