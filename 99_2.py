def recoverTree(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    The algorithm is based on in-order Morris traversal for satisfied the O(1) space complexity
    """
    pre, tmp, first, second = None, None, None, None
    # Morris Traversal
    while root:
        if root.left is None:
            if pre is not None and pre.val > root.val:
                if first is None:
                    first, second = pre, root
                else:
                    second = root
            pre = root
            root = root.right
        else:
            # connect threading for root
            tmp = root.left
            while tmp.right is not None and tmp.right is not root:
                tmp = tmp.right
            if tmp.right is None:
                # construct the threading
                tmp.right = root
                root = root.left
            else:
                # the threading already exists
                if pre is not None and pre.val > root.val:
                    if first is None:
                        first, second = pre, root
                    else:
                        second = root
                pre = root
                tmp.right = None
                root = root.right
    # swap two node values
    if first is not None and second is not None:
        first.val, second.val = second.val, first.val
