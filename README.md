# LeetCode
Record the process of solve LeetCode's programming questions  

## 99题: Recover Binary Search Tree
+ 基于中序遍历的结果中的逆序对进行判断，若只有一个逆序对，则将这两个node互换即可；若有两个逆序对，则将第一个逆序对的第一个节点与第二个逆序对的第二个节点进行互换即可；由于中序遍历有三种算法：递归、基于栈的迭代、Morris Traversal，但是满足O(1)的空间复杂度只有基于Morris Traversal的中序遍历算法  

## 100题：Same Tree
+ 基于递归的算法：判断两个树p、q的根结点是否相同，再判断p.left与q.left及p.right与q.right是否相同；时间复杂度较高
+ 基于遍历的算法：在基于栈的遍历过程中比较节点是否相同 

## 101题：Symmetric Tree  
+ 基于递归的算法(101_1.py)：输入两棵相同的树p,q，判断根结点是否相同q.val==p.val；再判断p.left与q.right及p.right与q.left是否对称； 
  + Time complexity : O(n)O(n). Because we traverse the entire input tree once, the total run time is O(n)O(n), where nn is the total number of nodes in the tree.  
  + Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the tree is linear and the height is in O(n)O(n). Therefore, space complexity due to recursive calls on the stack is O(n)O(n) in the worst case.  
+ 基于迭代的算法(101_2.py)：在每个iteration中，将当前高度的树节点存入一个列表中，并判断这个列表中的节点是否对称；100_2的解法中空间复杂度随着树高度指数增加；  
+ 基于迭代的算法(101_3.py 源自Leetcode其他人): 在每个迭代的过程中只比较两个应该对称的节点  
  + Time complexity : O(n)O(n). Because we traverse the entire input tree once, the total run time is O(n)O(n), where nn is the total number of nodes in the tree.  
  + Space complexity : There is additional space required for the search queue. In the worst case, we have to insert O(n)O(n) nodes in the queue. Therefore, space complexity is O(n)O(n).  

## 102题：Binary Level order Traversal  
+ `102_1.py` 基于迭代的方法: 类似于`101_2.py`中的想法，`stack`中存储的是当前层的节点，然后遍历`stack`中的节点，将该层的值保存到`ans`中，同时将这些节点的左右子节点刷新`stack`，一层一层的往下遍历  
+ `102_2.py` 基于递归的方法：构建一个辅助函数`dfs(root, level, res)`，其中`level`表示的是递归的层数，即当前root所在的层数

## 107题：Binary Level order Traversal II  
+ 将102题的输出结果做倒序输出（答案略过）
+ `107_1.py` 在102题的递归解法`102_2.py`中，改变输出结果的顺序以及每次均在`res`开始处增加空列表  

## 103题：Binary Tree Zigzag Level Order Traversal  
+ `103_1.py` 在`102_1.py`的基础上进行修改，初始化变量`direction=0`，在每个迭代过程中将`direction += 1`，这样可用`(-1)**direction==1`表示当前层从左到右遍历，`(-1)**direction==-1`表示当前层从右向左遍历，修改`ans.append(level_val)`为`ans.append(level_val[::(-1)**direction])`即可  
+ `103_2.py` 在`102_1.py`的基础上的另一种修改方式，将`level_val.append(node.val)`修改为`if (-1)**direction == 1:level_val.append(node.val); else:level_val.insert(0, node.val);`
+ `103_3.py` 在`102_2.py`的基础上做的修改，若当前层为奇数，表明应该从右向左遍历，这时将`res[level].append(root.val)`修改为从开始处插入，即`res[level].insert(0, root.val)`即可

## 104题：Maximum Depth of Binary Tree
+ `104_1.py` 基于递归的算法：树root深度的递归表达式 `depth(root) = max(depth(root.left)+depth(root.right))+1`；即树的深度为左子树的深度+1与右子树深度+1中的最大值  
  + 时间复杂度：我们每个结点只访问一次，因此时间复杂度为O(N), 其中N是结点的数量。
  + 空间复杂度：在最糟糕的情况下，树是完全不平衡的，例如每个结点只剩下左子结点，递归将会被调用N次（树的高度），因此保持调用栈的存储将是O(N)。但在最好的情况下（树是完全平衡的），树的高度将是log(N)。因此，在这种情况下的空间复杂度将是O(log(N))
+ `104_2.py` 基于迭代的算法，在`102_1.py`的基础上进行修改所得，对树的每一层做遍历，在每次迭代中，将高度+1，直到最底的叶结点为止
  + 时间复杂度：O(N).
  + 空间复杂度：O(N).

## 105题：Construct Binary Tree from Preorder and Inorder Traversal
+ `105_1.py` 基于递归的方法：preorder第一个元素为root，在inorder里面找到root，在它之前的为左子树（长L1），之后为右子树（长L2）。preorder[1]到preorder[L1]为左子树,之后为右子树，分别递归。(ps: 假设树中没有重复的元素)；  `105_2.py` 为了避免用循环搜索的方法在inorder里找到root，开始时便用inorder构建一个字典{key(节点):val(位置)}  
+ `105_3.py` 基于迭代的方法：中序遍历的结果：左子树的节点在根节点之前，右子树的节点在根节点之后；1. 遍历前序遍历的结果：将节点存入栈stack中，2. 将当前节点在中序遍历结果中的位置与stack[-1]在中序遍历结果中的位置比较；3. 若小于，则表明当前节点是stack[-1]的左节点；4. 反之，循环：u=stack.pop()，直到stack[-1]在中序遍历结果中的位置大于当前节点在中序遍历结果中的位置，则当前节点即为u的右节点。5. 将当前节点存入stack中  
