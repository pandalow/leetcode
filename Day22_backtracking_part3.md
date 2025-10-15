[93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)

```python
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        res = []
        path = []

        def isValid(digits):
            if len(digits) > 1 and digits[0] == '0':
                return False
            digits = int(digits)
            if 0<=digits<=255:
                return True
            return False
        
        def backtracking(index):
            # 当前的分割为4段，满足ip地址的条件
            if len(path) == 4:
                # 当前index已经到达s的末尾，即该截取的起始位置所有组合已经遍历结束
                if index == len(s):
                    # 收集该起始位置的结果
                    res.append(".".join(path[:]))
                    return
            
            for i in range(index, len(s)):
                # 截取对应的sub s， sub s从startindex开始， 到当前遍历位置结束
                subdigits = s[index:i+1]
                if not isValid(subdigits):
                    continue
                path.append(subdigits)
                backtracking(i+1)
                path.pop()
        
        backtracking(0)
        return res
```

1. start index 确定切割部位， 每一个递归是进行切割
2. is valid进行验证
3. 返回条件两层， 一层是当前的path有四个结果， 且已经结束了切割所有的字符串
4. 分割线为i+1: python 中[a:b]表示取 从下标 a 开始（包含 a），到下标 b 结束（不包含 b） 的子串。


[78. Subsets](https://leetcode.com/problems/subsets/)
```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []


        def backtracking(start):
            # 每次进入遍历都加一下当前路径， 不需要判断
            res.append(path[:])
            # 可以忽略掉的长度， 因为下面是for循环，结束不需要return吗 循环结束会自然return对吗
            if start == len(nums): return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i+1)
                path.pop()

        backtracking(0)
        return res
```



```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # 数层重复， used 需要控制
        used = [False for _ in range(len(nums))]
        res = []
        path = []
        nums.sort()
        def backtracking(start):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(i+1)
                path.pop()
                used[i] = False
            
        backtracking(0)
        return res
```

1. 理解“树层去重”和“树枝去重”非常重要。
2. 用used控制是否当前是否重复和使用过， 见[21日的组合2](Day21_backtracking_part2.md)
3. 与子集1一样的直接添加当前path(遍历所有节点)