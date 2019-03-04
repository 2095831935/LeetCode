def buildTree(preorder, inorder):
    """
    ps: 没有重复的元素
    """
    idx = {} 
    # 字典：key:节点；val:在中序遍历结果中的位置
    for i, val in enumerate(inorder):
        idx[val] = i 
			
	# Iterate over preorder and construct the tree 
    stack = []
    head = None
    for val in preorder:
        if not head:
            head = TreeNode(val)
            stack.append(head)
        else:
            node = TreeNode(val)
            if idx[val] < idx[stack[-1].val]:
                # 若node在inorder中的位置在stack[-1]之前
                # 则node是stack[-1]的左节点
                stack[-1].left = node
            else:
                while stack and idx[stack[-1].val] < idx[val]:
                # 反之，则是stack中某个节点stack[i]的右节点
                # 此时idx[val]应比stack[i]左子树所有节点在inorder中的位置更大
                    u = stack.pop()
                u.right = node
            stack.append(node)
    return head
