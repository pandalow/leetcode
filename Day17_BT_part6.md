[]
```python
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        min_value = 999999
        results = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            results.append(node.val)
            traverse(node.right)

            return 
        traverse(root)

        for i in range(1,len(results)):
            min_value = min(min_value, results[i]-results[i-1])
        
        return min_value
```
1. 中序遍历, 转有序数组
2. 比对i, i+1的值(因为有序), 所以必然就有了最小的值
3. 最小值输出

```python
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0

        self.min_val = float('inf')
        self.prev = None

        def traverse(node):
            if not node: return
            traverse(node.left)
            if self.prev is not None:
                self.min_val = min(self.min_val, node.val-self.prev.val)
            self.prev = node
            traverse(node.right)
            return

        traverse(root)

        return self.min_val
```

1. 用prev来记录前一个值, 用curr(node)来返回现在的值, 正好是有序的, 所以现在的值-prev值就是当前最小值;
2. 用self. 来避免python2的闭包问题


[501. Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/description/)
```python
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.count = 0
        self.max_count = 0 
        self.prev = None
        self.results = []

        def traverse(node):
            if node is None: return 
            traverse(node.left)

            if self.prev and self.prev.val == node.val:
                self.count += 1
            else:
                self.count = 1
            
            if self.count > self.max_count:
                self.max_count = self.count
                self.results = [node.val]
            elif self.count == self.max_count:
                self.results.append(node.val)
     
            self.prev = node
            traverse(node.right)

        
        traverse(root)
        return self.results
```

1. 取得是众数队列, 所以结果要加++val
2. 一个max count记录最大值, 一个count记录现在值
2. 核心:
    * 如果count >  max Count: 则代表的最大值队列已经无效, maxCount更新, results队列更新
    * 如果count = max Count: 则代表这个数字也是频率最大的数字, 可以加入队列

```python
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        results = defaultdict(int)

        def traverse(node):
            if node is None: return
            traverse(node.left)
            results[node.val]+=1
            traverse(node.right)

        traverse(root)
        
        sorted_results = sorted(results.items(), key=lambda x:x[1], reverse=True)
        max_freq = sorted_results[0][1]

        return [k for k, v in sorted_results if v == max_freq]

```

1. sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True) 
    * 用了lambda函数: lambda x:x[1], 去这个tuple的index=1 的值为排序依据
    * results.items() 会返回一个[(),()]的tuple的list


