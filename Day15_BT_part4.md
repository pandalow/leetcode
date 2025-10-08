[513. Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value/description/)

```java
class Solution {
    int result = 0;
    int depth = 0;
    int maxDepth = 0;
    public int findBottomLeftValue(TreeNode root) {
        if(root.left == null && root.right == null){
            return root.val;
        }
        getDepth(root);
        return result;
    }

    public void getDepth(TreeNode node){
        if(node.left == null && node.right == null){
            if(depth > maxDepth){
                maxDepth = depth;
                result = node.val;
            }
            return;
        }
        if(node.left != null){
            depth++;
            getDepth(node.left);
            depth--;
        }
        if(node.right != null){
            depth++;
            getDepth(node.right);
            depth--;
        }
        return;
    }
}
```
* 递归法:
1. depth 控制当前深度, 用回溯来模拟当前的迭代深度
    * Notes: 深度++, 深度-- 要与递归函数放在一起;
2. 判断条件: 判断当前为叶子节点且:
    * 深度比当前的最大深度大(满足题目条件, 最深处)
3. 因为是三种遍历方式都会在处理叶子节点时, 先处理左侧节点.
    * 所以只要将大于最大深度的的第一个值存起来就是当前最大层最左侧的数据


```java
class Solution {
    public int findBottomLeftValue(TreeNode root) {
        
        Queue<TreeNode> queue = new LinkedList<>();
        if(root==null){
            return 0;
        }
        queue.add(root);
        int maxDepth = 0;
        int res = 0;
        int depth = 0;
        while(!queue.isEmpty()){
            int size = queue.size();
            depth++;
            for(int i = 0; i < size; i++){
                TreeNode node = queue.remove();

                if(depth>maxDepth){
                    maxDepth = depth;
                    res = node.val;
                }

                if(node.left != null){
                    queue.add(node.left);
                }
                if(node.right != null){
                    queue.add(node.right);
                }
            }
            
        }
        return res;
    }
}
```
* 迭代法:
    * 也是用depth和maxdepth比较, 出现了第一次depth > maxdepth. 就是深度加一且为最左侧数据了


[112. Path Sum](https://leetcode.com/problems/path-sum/)
```java
class Solution {

    int value = 0;
    boolean isPath = false;
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null){
            return false;
        }
        value = root.val;
        findPath(root, targetSum);
        return isPath;
    }

    public void findPath(TreeNode root, int targetSum){
        if(root.left==null && root.right == null){
            if(value == targetSum){
                isPath = true;
            }
            return;
        }
        if(root.left != null){
            value += root.left.val;
            findPath(root.left, targetSum);
            value -= root.left.val;
        }
        if(root.right!= null){
            value+=root.right.val;
            findPath(root.right, targetSum);
            value -= root.right.val;
        }
        return;
    }
}
```
* 个人的递归做法:
1. 先加上最初始的节点, 后面就是使用回溯法来进行
2. 每次递归的步骤, 先加上子节点, 然后出来后就减去子节点;
3. 最终叶子节点(题目要求)判断是否路径和等于该目标值, 如果等于就修改判断值为true
```java
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null) return false;
        return traverse(root, targetSum-root.val);
    }

    public boolean traverse(TreeNode node, int count){
        if(node.left == null && node.right == null){
            if(count == 0){
                return true;
            }
            return false;
        }
        
        if(node.left != null){
            count-=node.left.val;
            if(traverse(node.left, count)) return true;
            count+=node.left.val;
        }
        if(node.right!= null){
            count-=node.right.val;
            if(traverse(node.right, count)) return true;
            count+=node.right.val;
        }
        return false;
    }
}
```
* 优化做法, 是用递减的方式:
    1. 直接返回结果, 同时用if() 来做递归判断, 这样即进行了递归, 又确保了返回值可以继续往上返回;
    2. 如果递归调用 traverse(node.left, count) 返回了 true，那就立刻在当前函数中也返回 true，不再继续执行下面的代码（包括右子树部分）。
1. 判断是否需要返回值:
    * 如果需要搜索整棵二叉树且不用处理递归返回值，递归函数就不要返回值。（这种情况就是本文下半部分介绍的113.路径总和ii）
    * 如果需要搜索整棵二叉树且需要处理递归返回值，递归函数就需要返回值。 （这种情况我们在236. 二叉树的最近公共祖先 (opens new window)中介绍）
    * 如果要搜索其中一条符合条件的路径，那么递归一定需要返回值，因为遇到符合条件的路径了就要及时返回。（本题的情况）

[113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)

```java
class Solution {
    List<List<Integer>> results = new ArrayList<>();
    Stack<Integer> stack = new Stack<>();
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if(root != null){
            stack.push(root.val);
            traverse(root, targetSum-root.val);
        }
        return results;
    }
    public void traverse(TreeNode node, int count){
        if(node.left == null && node.right == null){
            if(count == 0){
                results.add(new ArrayList<>(stack));
            }
        }
        if (node.left != null){
            stack.push(node.left.val);
            count-=node.left.val;
            traverse(node.left, count);
            stack.pop();
            count+=node.left.val;
        }
        if (node.right != null){
            stack.push(node.right.val);
            count-=node.right.val;
            traverse(node.right,count);
            stack.pop();
            count+=node.right.val;
        }
    }
}s
```
* 用一个stack来管理回溯的过程;
* 只需要替换下叶子节点返回值变为组成一个stack, 并向最终集合中添加就可以了.
* 需要便遍历所有可能性, 不要立即返回, 所以不加任何return


[106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
    
        def traverse(inorder, postorder):
            if len(postorder) == 0: return None
            root_value = postorder[-1]
            root = TreeNode(val = root_value)

            if len(postorder) == 1: return root

            index = 0
            for i in range(len(inorder)):
                if inorder[i] == root_value:
                    index = i
                    break
            
            left_inorder = inorder[:index]
            right_inorder = inorder[index+1:]

            postorder = postorder[:-1]
            left_postorder = postorder[:len(left_inorder)]
            right_postorder = postorder[len(left_inorder):]
            root.left = traverse(left_inorder, left_postorder)
            root.right = traverse(right_inorder, right_postorder)

            return root

        return traverse(inorder, postorder)
```

第一步：如果数组大小为零的话，说明是空节点了。
第二步：如果不为空，那么取后序数组最后一个元素作为节点元素。
第三步：找到后序数组最后一个元素在中序数组的位置，作为切割点
第四步：切割中序数组，切成中序左数组和中序右数组 （顺序别搞反了，一定是先切中序数组）
第五步：切割后序数组，切成后序左数组和后序右数组
第六步：递归处理左区间和右区间