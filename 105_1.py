def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    ps: 没有重复的元素
    """
    for i in range(len(inorder)):
        if inorder[i] == preorder[0]:
            left_root  = buildTree(preorder[1:i+1], inorder[:i])
            right_root = buildTree(preorder[i+1:], inorder[i+1:])
            root = TreeNode(preorder[0])
            root.left  = left_root
            root.right = right_root
            return root
