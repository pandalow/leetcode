[242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

1. 声明字典初始值为0
2. s出现字符+=1, t出现字符-=1
3. 如果出现values不为0情况即 返回 false


[349](https://leetcode.com/problems/intersection-of-two-arrays/)

这道题可以三种做法:
1. 用set()直接获得两个去重hash, 遍历两个set, 从而获得交集;
2. 自己使用hashmap模拟set的操作, 如果出现 value = 1, 这样就可以获得交叉部分.
3. 用双指针的方式进行:
    * nums1, nums2 分别进行快速排序;
    * 双指针a, b从头向尾进行
        * 如果出现相等 , 且不在最终结果数组中, 加入
        * 如果 nums1[a] < num2[b], 则代表a指针可以继续往前(因为是有序的)
        * 如果 nums1[a] > nums2[b], 则b指针往前

[208](https://leetcode.com/problems/happy-number/submissions/1779144177/)

1. 处理商和余数的方法: n, l =  `divmod(a, b)`, 返回的n为商, l为余数, 是一个很好的缩位的方法
2. endless loop代表 sums的数字会反复出现, 只要不是1, 同时在set里出现过,就代表进入了无限循环.


[1](https://leetcode.com/problems/two-sum/description/)
1. 用hash map的思路为: a, b 两个值, target - a == b 就成功了, 
2. 正好 a:index, b:index 两个值可以使用map的方式存下来, 这样 我就可以查询 target - a 这个值是否存在与 map 中, 如果存在就代表之前有个元素和当前的a 想加为目标值;
3. 所以用map来处理已经遍历过的对象, 更换存储结构.
4. 所以用map来处理value: index的格式, 因为最终返回的为索引位置.