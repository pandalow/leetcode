1. 完全二叉树
    * 叶子节点是连续的,从左之右
    * 堆是完全二叉树
2. BST, 二叉搜索树
    * 左子树小于父节点, 右子树大于父节点

3. BST,平衡二叉搜索树
    * 左子树和右子树的高度差不能超过1
    * map, set, multimap, multiset -> 平衡二叉搜索树

4. 存储方式:
    1. 链式存储:指针left, right
    2. 线性存储: 2n+1 left, 2n+2 right


三道遍历的题:
[PreOrder](https://leetcode.com/problems/binary-tree-preorder-traversal/)
[Post Order](https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/1786700398/)
[InOrder](https://leetcode.com/problems/binary-tree-inorder-traversal/)


5. 迭代方案:
    * 前序遍历:是中左右，每次先处理的是中间节点，那么先将根节点放入栈中，然后将右孩子加入栈，再加入左孩子。
        *  循环为栈有节点
    * 后序便利: 左右中, 颠倒前序遍历顺序, 再翻转最后数组
    