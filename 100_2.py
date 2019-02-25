def isSameTree(p, q):
    stack_p, stack_q = [], []
    while stack_p or p or stack_q or q:
        while p or q:
            try:
                if p.val == q.val:
                    stack_p.append(p)
                    stack_q.append(q)
                    p = p.left
                    q = q.left
                else:
                    return False
            except:
                return False
        p = stack_p.pop()
        q = stack_q.pop()
        p = p.right
        q = q.right
    return True
