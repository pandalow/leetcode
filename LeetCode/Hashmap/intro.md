
### Concept Explain
1. Key: a input in the hash function that determines the location for the storage
2. Hash Function: input Key, output hash index
3. Hash Table: map key, value pairs using hash function.

- Hash stores the data in an associative manner in an array where each data value has its own unique index.

4. Collision: two key possibility that two keys could produce same value
5. Load Factor: determined by how many elements are there in relation to how big the table is. 当元素越来越多，超过一定负载因子（load factor，比如 0.75），哈希表就会自动 扩容（resize），重新分配更大的数组（比如从 16 扩到 32），再把已有的元素重新哈希一遍（rehash）。
6. bucket: bucket（桶） 就是数组的一个槽位（slot），用来存放哈希到同一个位置的 一个或多个键值对 (key, value)。

### Hash Function ([url](https://www.geeksforgeeks.org/dsa/what-are-hash-functions-and-how-to-choose-a-good-hash-function/))
A function that translates keys to array indices is known as a hash function.

- Integer universe assumption
- Division / Multiplication(bitwise operation)

- Good hash function: Efficiently Computable, Uniform Distribution of Keys(Simplicity, Minimize Collisions, Uniform Distribution, Consider All bits)

![alt text](image.png)

### Collision

Key1 != Key2 BUT Hash(Key1) == Hash(Key2)

1. Open Addressing: 

 ** H(i) = (Hash(key)+F(i)) mod m, i  = 1, 2, 3, ...... , n(n <= m-1)
    ** Linear Probing - i = + 1
    ** Quadratic probing - i = i * i
    ** Fake random sequeece

2. Chaining



# Appendix:

## 📌 普通数组的样子

比如：

```text
arr = [1212, 23123, 4124]
```

* 索引(index)： `0, 1, 2`
* 值(value)： `1212, 23123, 4124`

👉 在普通数组里，索引 = 下标，值 = 直接存的内容。

---

## 📌 哈希表里的数组

哈希表底层也是用数组，不过 **数组里放的不是直接的 value，而是 bucket（桶）**。

比如：

```text
table = [bucket0, bucket1, bucket2, ..., bucket(m-1)]
```

* **索引 (index)**： `0, 1, 2, ... m-1`
  （就是哈希函数算出来的值 h(k)）
* **数组里的值 (bucket)**： 代表这个位置的“桶”，桶里才真正存 key/value。

---

## 🧩 两种情况

### 1. 开放定址法

bucket 只存 **一个键值对 (key, value)**：

```text
table = [ (17, "a"),  (23, "b"),  empty,  (42, "c") ]
index     0              1         2        3
```

### 2. 链地址法

bucket 是一个 **链表 / 动态数组**，能存多个键值对：

```text
table = [ [(8,"x"), (12,"y")],   [(5,"z")],   [],   [(7,"w")] ]
index     0                     1             2     3
```

👉 这里每个方括号就是一个 bucket。

* `table[0]` 里存着一个链表：`[(8,"x"), (12,"y")]`
* `table[2]` 是空 bucket。

---

## 🎯 总结

* **数组的索引** = 哈希函数的结果 h(k)，决定元素应该放在哪个 bucket。
* **数组的值** = bucket，本质是一个存放数据的“容器”。
* **bucket 的内容** = 存放一个或多个 (key, value)。

---

也就是说，你举的 `[1212, 23123, 4124]` 在哈希表语境下，应该理解成：

* `0, 1, 2` 是数组索引
* `1212, 23123, 4124` 分别是 **bucket**，只是这里 bucket 里恰好直接存的是整数而已。

---

## 📌 关键原因：避免“误认”

哈希函数只是一个 **压缩函数**，它把一个超大范围的 key 映射到有限范围 `[0, m-1]`。
这意味着：**不同的 key 可能会哈希到同一个位置**，也就是所谓的 **哈希冲突**。

如果 bucket 里只存 **value**，就会有两个问题：

1. 你拿 key 去查找时，没法确认 bucket 里的 value 对应的 key 是不是你要找的。
2. 冲突发生时（两个不同的 key 哈希到同一个 bucket），数据就混乱了。

所以必须在 bucket 里存 **(key, value) 对**。

---

## 🧩 查找流程举例

假设哈希表大小 $m = 4$，哈希函数是 `h(k) = k mod 4`。

插入数据：

* 插入 (8, "Alice") → $h(8) = 0$，放到 bucket\[0]
* 插入 (12, "Bob") → $h(12) = 0$，也放到 bucket\[0]

哈希表（链地址法）：

```
index   bucket
0   ->  [(8, "Alice"), (12, "Bob")]
1   ->  []
2   ->  []
3   ->  []
```

### 查找 key=12 时：

1. 用哈希函数算：`h(12) = 0` → 找到 bucket\[0]。
2. 遍历 bucket\[0] 里的元素：

   * 先看到 (8, "Alice") → key 不匹配，继续。
   * 再看到 (12, "Bob") → key 匹配，返回 value = "Bob"。

👉 如果 bucket 里只存 value，比如 `[ "Alice", "Bob" ]`，那你完全分不清哪个值对应哪个 key。

---

## 🎯 总结

* **bucket 里存 key 是为了确认身份**，避免冲突时出错。
* 查找时：输入的 key → 通过哈希函数定位 bucket → 在 bucket 里比对 key → 找到对应 value。
* 没有 key 的话，查找就会模糊，无法保证正确性。


---

## 📌 1. 哈希函数一定是压缩的吗？

是的，哈希函数 **必然是压缩函数**。
原因：

* key 的取值空间很大（可能是整数、字符串、甚至对象），几乎是无限的。
* 但哈希表的数组大小是有限的，比如 $m = 2^{10} = 1024$。
* 所以哈希函数必须把“大空间”压缩到 `[0, m-1]` 这个“小空间”里。

数学上：

$$
h: U \rightarrow [0, m-1]
$$

其中 $U$ 是所有可能的 key（巨大），而 `[0, m-1]` 就是有限索引范围。

---

## 📌 2. 哈希函数一定会输出整数索引吗？

对，哈希表里使用的哈希函数 **最后的结果必然是整数索引**，因为：

* 底层存储是数组（array）。
* 数组只能通过 **整数下标** 访问。

所以无论中间怎么算（乘法法、除法法、字符串哈希、MD5/sha256 等），最终都要转成一个整数，然后再对 `m` 取模：

$$
h(k) = f(k) \bmod m
$$

得到的结果必然在 `0..m-1` 之间。

---

## 📌 3. 压缩后的必然现象：冲突

因为哈希函数是压缩的（把大空间挤到小空间），所以**必然会发生冲突**：

* 两个不同的 key 得到相同的索引。
* 比如 $h("cat") = 5$，$h("dog") = 5$。

这就是为什么哈希表需要 **冲突解决机制**（链地址法 / 开放定址法）。

---

## 📌 4. 类比理解

你可以把哈希函数想成 **把全国的人按身份证号映射到 100 个柜子里**：

* 身份证号空间 = 巨大
* 柜子数量 = 有限
* 最终必须压缩到 `0~99` 这 100 个索引
* 不同人可能进同一个柜子（冲突）
* 所以柜子里必须标注“身份证号”（= key），否则搞混。

---

✅ **总结：**

* 哈希函数一定是 **压缩函数**。
* 最终输出必然是一个 **整数索引**（用来访问数组）。
* 压缩意味着 **冲突不可避免**，所以才需要 bucket 和 key 存储。
