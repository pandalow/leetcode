[491. Non-decreasing Subsequences](https://leetcode.com/problems/non-decreasing-subsequences/description/)
```python
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 不可以排序， 会干扰元素顺序， 影响递增子序列的结果

        res = []
        path = []

        def backtracking(start):
            # 这里当满足条件时，直接就加入即可，是个遍历的节点的过程
            if len(path)>1:
                res.append(path[:])
            # 树层去重， 需要用一个set记录当前的数字在本层使用过了
            uset = set()
            for i in range(start, len(nums)):
                if len(path) > 0 and nums[i] < path[-1] or nums[i] in uset:
                   continue
                path.append(nums[i])
                uset.add(nums[i])
                backtracking(i+1)
                path.pop()
        
        backtracking(0)

        return res
```
1. 用子集的思路解决问题： 不要排序
2. 这里当满足条件时，直接就加入即可，是个遍历的节点的过程
3. 树层去重， 需要用一个set记录当前的数字在本层使用过了


[46. Permutations](https://leetcode.com/problems/permutations/)
```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        # 用一个used来控制不要来使用同一个元素
        used = [False for _ in range(len(nums))]

        # 全排列问题中， 不需要使用start来控制， 因为排列问题中的数字相同， 组合方式不同是允许的。
        # 所以每次都会从开始进行取值
        def backtracking():
            # 终止条件为当前path长度与需要长度一致， 就可以返回
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking()
                used[i] = False
                path.pop()

        backtracking()
        return res
```


[47. Permutations II](https://leetcode.com/problems/permutations-ii/description/)
```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # [1, 1, 3]
        nums.sort()
        res = []
        path = []
        used = [False for _ in range(len(nums))]
        def backtracking():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                # 限定条件为： 当前树从使用过， 
                # 或者 当前数字与前一数字一致，且前一数字未使用过（证明为这个数字和前一数字是在层级中重复）
                # 从而限定了了重复情况
                if used[i] or (i>0 and nums[i]== nums[i-1] and not used[i-1]):
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking()
                used[i] = False
                path.pop()
        
        backtracking()
        return res
```
树层上对前一位去重非常彻底，效率很高，树枝上对前一位去重虽然最后可以得到答案，但是做了很多无用搜索。