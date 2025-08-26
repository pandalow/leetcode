Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Constraints:

0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.





#### Solution 1
```python
class MyHashMap(object):

    def __init__(self):

        
        self.capacity = 769
        self.data = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return key % self.capacity

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        idx = self._hash(key)
        bucket = self.data[idx]
        for i, (k,v) in enumerate(bucket):
            if key == k:
                bucket[i][1] = value
                return
        bucket.append([key,value])
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        idx = self._hash(key)
        bucket = self.data[idx]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                return bucket[i][1]
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = self._hash(key)
        bucket = self.data[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```

好问题 👌，这三个正是面试官喜欢追问的点。给你整理一个**答题思路**（可直接用在面试里）：

---

### 1️⃣ 为什么选 **分离链接**（Separate Chaining）而不是开放寻址（Open Addressing）？

**答题要点：**

* **时间复杂度**：分离链接在负载因子较高时表现更稳健。即使某个桶变长，查找是 O(桶长)，平均还是 O(1)。
* **删除操作更简单**：直接从桶里移除元素，不影响其他数据。开放寻址删除时需要「标记已删除」或进行再探测，否则会破坏探测序列。
* **扩容灵活**：分离链接只需要把所有元素重新分桶；开放寻址可能会导致长时间的探测和数据搬移。
* **空间利用**：开放寻址对负载因子更敏感（一般建议 ≤0.7），否则冲突严重性能急剧下降；分离链接可以容忍更高的负载因子。

> **一句话总结**：分离链接实现简单、删除友好、对高负载更鲁棒，因此在面试题里常选它。

---

### 2️⃣ 如果要扩容，你的触发条件与 rehash 步骤是？

**触发条件：**

* 典型选择：当 **元素数 ÷ 桶数 > 负载因子** 时触发扩容。
* 常见负载因子：0.75（Java 的 HashMap 默认值）。

**rehash 步骤：**

1. 新建一个更大的数组（容量一般翻倍，比如从 769 → 1538）。
2. 遍历旧表所有 (key, value)。
3. 对每个 key 重新计算 `idx = hash(key) % new_capacity`。
4. 把它放入新表对应的桶里。
5. 替换旧表引用。

> **一句话总结**：扩容就是「容量翻倍 → 所有元素重新哈希 → 放入新桶」。

---

### 3️⃣ 如何选择容量（素数 vs 2 的幂）以及哈希函数，来降低碰撞？

**容量选择：**

* **素数容量**：避免数据分布与哈希模式（如 key 分布有规律）产生“对齐效应”，更均匀。
* **2 的幂容量**：计算快（`key & (capacity-1)` 等价于 `% capacity`），适合性能要求高的系统。
* **实际工程**：Java 的 `HashMap` 就是选 **2 的幂**，因为配合好的哈希函数能减少碰撞。

**哈希函数选择：**

* 最简单：`key % capacity`。
* 更稳健：乘法哈希（`(key * A) % capacity`，A 取常数，如黄金比例相关数）。
* 对象键：要结合对象的 `hashCode()` 再做二次混合，避免模式化冲突。

> **一句话总结**：
>
> * 题目里常用素数，避免冲突；
> * 工程里常用 2 的幂，结合更复杂的哈希函数；
> * 关键点是 **哈希函数分布均匀**，而不是只靠容量。

---

✅ 这样回答，面试官会觉得你不光会写，还理解**设计权衡**。

要不要我帮你整理成一个「简洁版口述答案」，让你在面试里能 1 分钟答完这三个问题？
