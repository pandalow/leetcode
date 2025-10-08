
[654. Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/description/)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """


        def traverse(order):
            if not order: return None

            max_value = max(order)
            root = TreeNode(val = max_value)

            index = order.index(max_value)
            leftorder = order[:index]
            rightorder = order[index+1:]

            root.left = traverse(leftorder)
            root.right = traverse(rightorder)
            return root

        return traverse(nums)
```
1. 和106的方式差不多, 注意前序遍历, 先构造根节点, 然后左子树, 右子树

[617. Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/description/)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root1: return root2
        if not root2: return root1

        root1.val = root1.val + root2.val


        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

```

1.  递归定义：merge(root1, root2) 返回合并后的树根；
2. 递归结束条件：一方为空；
3. 递归调用：合并左右子树；
4. 递归返回：修改过的根节点

[700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/description/)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root: return None;

        if root.val == val: return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        
        if val > root.val:
            return self.searchBST(root.right, val)

        return None
```

1. 自带顺序, 不用关注顺序了