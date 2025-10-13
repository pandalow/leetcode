* 解决的问题：
    * 组合问题：N个数里面按一定规则找出k个数的集合
    * 切割问题：一个字符串按一定规则有几种切割方式
    * 子集问题：一个N个数的集合里有多少符合条件的子集
    * 排列问题：N个数按一定规则全排列，有几种排列方式
    * 棋盘问题：N皇后，解数独等等


* 都可以抽象为一个树形结构-> N叉树
    * 宽度-> for
    * 深度-> 递归 recursion

模板： 
```
void backtracking(params){
    if(stop condition){
        collect results;
        return
    }

    for loop in (collection element){
        handle nodes
        rucurrsion(params)
        handle backtracking
    }
    return
}
```

[77. Combinations](https://leetcode.com/problems/combinations/description/)

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def backtracking(n, k, start_index): # start_index搜索的起始位置, 避免重复搜索
            if len(path) == k: # 如果path长度为k， 则证明当前结果已经收集到了
                res.append(path[:]) # 注意需要深拷贝对象
                return
            
            # 每一个节点都是一个for循环
            for i in range(start_index, n+1):
                path.append(i)
                backtracking(n, k, i+1)
                path.pop() # 最重要的一步， 把结果取出来
            
            return
        
        backtracking(n, k, 1)
        return res
```

1. 回溯法解决的问题都可以抽象为树形结构（N叉树），用树形结构来理解回溯就容易多了。
2. 三步解法：
    * 递归函数的返回值以及参数
    * 回溯函数终止条件(到达叶子节点的终止条件)

* 剪枝操作：
    * 如果for循环选择的起始位置之后的元素个数 已经不足 我们需要的元素个数了，那么就没有必要搜索了。
`n-(k-len(path))+2`

* 已经选择的元素个数：path.size();
* 所需需要的元素个数为: k - path.size();
* 列表中剩余元素（n-i） >= 所需需要的元素个数（k - path.size()）
* 在集合n中至多要从该起始位置 : i <= n - (k - path.size()) + 1，开始遍历


```python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def backtracking(k, n, start):
            if sum(path) == n and len(path) == k:
                res.append(path[:])
                return
            for i in range(start, 10):
                path.append(i)
                backtracking(k, n, i+1)
                path.pop()
            
        backtracking(k,n,1)
        return res
```
加了剪枝
```python
class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        path = []

        def backtracking(k, n, start, curr_sum):
            # 剪枝1：如果当前和已超过目标
            if curr_sum > n:
                return
            # 成功条件
            if curr_sum == n and len(path) == k:
                res.append(path[:])
                return
            # 遍历选择
            for i in range(start, 10):
                # 剪枝2：剩余数字不足以组成长度k
                if len(path) + (9 - i + 1) < k:
                    return
                path.append(i)
                backtracking(k, n, i + 1, curr_sum + i)
                path.pop()

        backtracking(k, n, 1, 0)
        return res
```

[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)
```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == "": return []
        tele = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }  
        res = []
        path = []

        def backtracking(digits, index): 
            # index为确认当前遍历到哪一个digits, 
            if index == len(digits):
                res.append("".join(path[:]))
                return
            s = tele[digits[index]]
            # 因为s每次取出的都不一样, 为2个集合, 与前一层的集合不同, 不需要用start做区分
            # 所以每次直接遍历当前字符串, 加入路径即可
            for ch in s: 
                path.append(ch)
                backtracking(digits,index+1)
                path.pop()
            
        backtracking(digits, 0)
        return res
```
1. index是记录遍历第几个数字了，就是用来遍历digits的（题目中给出数字字符串），同时index也表示树的深度。