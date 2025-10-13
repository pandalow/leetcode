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