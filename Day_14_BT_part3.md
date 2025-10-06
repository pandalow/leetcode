[110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)
1. -1 返回,提供信号表示不是平衡树;
2. 当切节点高度的 = 左右子树的最大值 + 1
3. 后续遍历返回高度, 前序遍历返回深度.
4. 平衡二叉树: 所有的左右子树的到叶子节点的高度差不超过1



[257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/description/)
1. 找到的是叶子节点, 就停止, 而不是找到空节点(否则处理起来非常麻烦);
2. 使用回溯+前序遍历
    * 前序遍历是因为处理逻辑需要先加入本节点, 后面加入叶子节点,与后续的pop的过程放在一起;
    * 回溯为核心: 当前回退一个路径就把已经加入的节点拿出来, 方便下一步去遍历别的路径;
3. 回溯要和递归永远在一起

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    ArrayList<String> results = new ArrayList<>();
    Stack<Integer> stack = new Stack<>();

    public List<String> binaryTreePaths(TreeNode root) {
        if (root == null){
            return results;
        }

        traversePath(root);
        return this.results;
    }
    public void traversePath(TreeNode node){
        
        this.stack.push(node.val);
        if(node.left == null && node.right == null){
            List<String> path = new ArrayList<>();
            for(Integer i:stack){
                path.add(String.valueOf(i));
            }
            String res = String.join("->", path);
            this.results.add(res);
            return;
        }

        if(node.left != null){
            traversePath(node.left);
            // back tracking, when return from the previous node, then pop() the node from the preivous;
            stack.pop();
        }
        if(node.right!=null){
            traversePath(node.right);
            stack.pop();
        }

    }
}
```


[404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/description/)

1. 核心判断条件: 节点A的左孩子不为空，且左孩子的左右孩子都为空（说明是叶子节点），那么A节点的左孩子为左叶子节点
2. 通过上一层来进行下一层的计算



[222. Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
            
        if root.left and root.right:
            leftnode = root.left
            rightnode = root.right
            left, right = 0, 0
            while leftnode:
                leftnode = leftnode.left
                left+=1
            while rightnode:
                rightnode = rightnode.right
                right+=1

            if right == left: return (1 << (left + 1)) - 1   # 2^(h+1) - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1
```

1. 用完全二叉树的特性去解决;
2. 如果是满二叉树, 则只需要去计算该二叉树的深度就可以了, 通过 2^n-1的公式可计算所有节点数量;
3. 如何判断 满二叉树:
    * 最左侧叶子节点的深度和最右侧叶子节点深度一致; 则就是一颗满二叉树(从左至右, 叶子姐点都填满了)

