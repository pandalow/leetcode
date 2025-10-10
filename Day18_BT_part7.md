[235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)
```python

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        def traverse(node, p, q):
            if node is None: return None
            if node.val> p.val and node.val > q.val:
                left = traverse(node.left, p, q)
                if left: return left

            if node.val < q.val and node.val < p.val:
                right = traverse(node.right,p, q)
                if right: return right
        
            
            return node
        
        return traverse(root, p, q)
```
1.  这是一个搜索过程, 
    * 如果比p, q都大, 就在左子树, 如果比p, q都小, 就在右子树
    * 如果既不比p, q 都大, 或者右不比p,q都小,就是在这中间, 依然是他们的公共祖先(且只有这一个公共祖先) 往上返回
    * 就会依据搜索路径逐步返回(左,或者右)


[701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/description/)
```python
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        
        if not root: return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        return root
```

核心思想：
* 若当前节点为空 → 新建节点；
    * 若值更小 → 插入左子树；
    * 若值更大 → 插入右子树；
    * 最终返回整个 root。
* 实际上可能只空一边时就能插入；

若无返回值: 需要记录上一个节点（parent），遇到空节点了，就让parent左孩子或者右孩子指向新插入的节点。然后结束递归。
```python
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        if root is None:
            return TreeNode(val)
            
        self.prev = TreeNode(0)

        def insert(node, val):
            if node is None:
                new = TreeNode(val)
                if self.prev.val > val:
                    self.prev.left = new
                else:
                    self.prev.right = new
                return
            self.prev = node
            if node.val > val:
                insert(node.left, val)
            else:
                insert(node.right, val)
            
            return

        insert(root, val)
        return root    
```