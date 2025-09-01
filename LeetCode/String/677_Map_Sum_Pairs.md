Design a map that allows you to do the following:

Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.


#### Solution
1. 字典树构建prefix search的方法, 值存在leaf node
2. 找到有prefix时, 用dfs找到从当前节点下所有leafnode的value, 加和

```python
class Trie():

    def __init__(self):
        self.children = dict()
        self.isEnd = False
        self.val = 0

    def insert(self, word, value):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True
        cur.val = value
    
    def search(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                return 0
            
            cur = cur.children[ch]
        return self.dfs(cur)

    def dfs(self,node):
        if not node:
            return 0
        res = node.val
        for val in node.children.values():
           res += self.dfs(val)
        return res
                    
class MapSum(object):

    def __init__(self):
        self.node = Trie()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.node.insert(key, val)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.node.search(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```