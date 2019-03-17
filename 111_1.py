def minDepth(root):
    if not root:
        return 0
    depth_l = minDepth(root.left)
    depth_r = minDepth(root.right)
    return 1+min(depth_l+depth_r) if (depth_l and depth_r) else (1+depth_l+depth_r)
