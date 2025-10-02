[226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

1. 前序遍历互换, 先互换children, 再进去
2. 后续便利互换, 先到最后层, 逐步返回互换
3. 层序遍历互换: 每一层互换, 用一个tmp来记录


[101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
            
        def compare(left, right):
            if not left and right: return False
            elif left and not right: return False
            elif not left and not right: return True
            elif left.val != right.val: return False

            outside = compare(left.left, right.right)
            inside = compare(left.right, right.left)
            isSym = outside and inside

            return isSym
        return compare(root.left, root.right)
```
1. 理解限制条件, 前面的四项条件为判断左右的对称逻辑
2. 需要使用后序便利, 可以找到最底部, 而不是前序, 前序会在前面节点就提前结束了判断逻辑

相同的树的操作
[100. Same Tree](https://leetcode.com/problems/same-tree/submissions/1789190468/)

[572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
1.  这个需要用一个dfs先去遍历主树, 然后在每个节点去判断是不是相同的, 如果有任何一个相同的情况(or), 就返回结果True