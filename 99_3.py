def recoverTree(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    the algorithm is based on recursive in-order traversal
    """
    prev, first, second = None, None, None
    # use inorder traversal to detect incorrect node
    inorderTraversal(root, prev, first, second)
    first.val, second.val = second.val, first.val
    
    
def inorderTraversal(root, prev, first, second):
    # recursive
    if root is None:
        return 
    inorderTraversal(root.left, prev, first, second)
    # in-order traversal of BST, prev should always have small value than current value
    if prev is not None and prev.val >= root.val:
        # incorrect smaller node is always found as prev node
        if first is None:
            first = prev
        # incorrect larger node is always found as cur(root) node
        second = root
    inorderTraversal(root.right, prev, first, second)
