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
    * 中序遍历: 模拟遍历的方式, 用left和right的指针去替换直接当前的遍历的节点
        * curr = curr.left -->> curr = curr.right


6. 层序遍历:
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result
```


[107](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
* 思路是先层序遍历, 然后反转数组

[199](https://leetcode.com/problems/binary-tree-right-side-view/submissions/1787640997/)
* 思路为提取每层的最后一个值

[429. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/)

[637. Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/description/)

[515. Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/submissions/1788370682/)

[116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/)
这道题的核心是用一个prev来暂存已经遍历过的的节点

[117. Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/submissions/1788525186/)

[104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

[111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
出现无左右节点时, 直接刹车就可以了.