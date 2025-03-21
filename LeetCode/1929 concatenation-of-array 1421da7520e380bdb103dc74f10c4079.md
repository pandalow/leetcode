# 1929 concatenation-of-array

List. + List 可以串联数组

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2  # Repeat the list twice
```

也可以乘以2

也可以用extend

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums.extend(nums)
```