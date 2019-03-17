def buildTree(inorder, postorder) -> TreeNode:
    """
    ps: 没有重复的元素
    """
    idx = {}
    for i, val in enumerate(inorder):
        idx[val] = i
        
    stack = []
    head = None
    for val in postorder[::-1]:
        if not head:
            node = TreeNode(val)
            head = node
            stack.append(head)
        else:
            node = TreeNode(val)
            if idx[val] > idx[stack[-1].val]:
                stack[-1].right = node
            else:
                while stack and idx[val] < idx[stack[-1].val]:
                    u = stack.pop()
                u.left = node
        stack.append(node)
    return head
