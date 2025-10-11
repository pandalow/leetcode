[669. Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)
```python
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        if root is None: return None
        if root.val < low:
            if root.right:
                return self.trimBST(root.right, low, high)
            else:
                return None
        if root.val > high:
            if root.left:
                return self.trimBST(root.left, low, high)
            else:
                return None
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root
```
1. 核心误区： BST的特征为
    * node的右子树比它大， 在小于val时， 右边也可能在区间内
    * node的左子树比它小， 在大于val时， 左边也可能在区间内
2. 因此返回的是， 
    * 在小于val时， 向右找到所有的在区间的节点
    * 在大于val时， 向左找到所有的在区间的节点
3. 遍历后， 用root的左右子树接住新的子树


```python
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(nums) < 1: return None
        size = len(nums)
        index = size // 2
        root = TreeNode(nums[index])
        
        root.left = self.sortedArrayToBST(nums[:index])
        root.right = self.sortedArrayToBST(nums[index+1:])

        return root
```
1. 用中间节点做为分割点， 取其进行为当前节点返回
2. 左边的树去接左边的区间， 右边的树去接右边的区间
3. 左闭右闭的方式渐进的进行递归。
4. 如果数组为偶数， 那么中间节点可以是+1/-1， 这决定了树的样子， 都可以接受， 但都是平衡的树， 因为高度相差不过1

