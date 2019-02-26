# LeetCode
Record the process of solve LeetCode's programming questions  
## 99题: Recover Binary Search Tree
+ 基于中序遍历的结果中的逆序对进行判断，若只有一个逆序对，则将这两个node互换即可；若有两个逆序对，则将第一个逆序对的第一个节点与第二个逆序对的第二个节点进行互换即可；由于中序遍历有三种算法：递归、基于栈的迭代、Morris Traversal，但是满足O(1)的空间复杂度只有基于Morris Traversal的中序遍历算法  
## 100题：Same Tree
+ 基于递归的算法：判断两个树p、q的根结点是否相同，再判断p.left与q.left及p.right与q.right是否相同；时间复杂度较高
+ 基于遍历的算法：在基于栈的遍历过程中比较节点是否相同  
## 101题：Symmetric Tree  
+ 基于递归的算法：判断当前根节点的两个子节点是否对称；  
+ 基于迭代的算法：在每个iteration中，将当前高度的树节点存入一个列表中，并判断这个列表中的节点是否对称  
