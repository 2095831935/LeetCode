# LeetCode
Record the process of solve LeetCode's programming questions  
## 99题
基于中序遍历的结果中的逆序对进行判断，若只有一个逆序对，则将这两个node互换即可；若有两个逆序对，则将第一个逆序对的第一个节点与第二个逆序对的第二个节点进行互换即可；由于中序遍历有三种算法：递归、基于栈的迭代、Morris Traversal，但是满足O(1)的空间复杂度只有基于Morris Traversal的中序遍历算法
