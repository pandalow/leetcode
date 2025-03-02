# 234. Palindrome Linked List

Given the `head` of a singly linked list, return `true` *if it is a*

*palindrome*

*or*

```
false
```

*otherwise*

.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

```
Input: head = [1,2,2,1]
Output: true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)

```
Input: head = [1,2]
Output: false

```

**Constraints:**

- The number of nodes in the list is in the range `[1, 105]`.
- `0 <= Node.val <= 9`

- solution
    
    ```python
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution(object):
        def isPalindrome(self, head):
            """
            :type head: Optional[ListNode]
            :rtype: bool
            """
            arr = []
            
            while head:
                arr.append(head.val)
                head = head.next
    
            left = 0
            right = len(arr) - 1
            while left < right:
                if arr[left] != arr[right]:
                    return False
                left+=1
                right-=1
            return True
    ```
    
- explain
    
    拷贝了一个完整的数组, 然后用回文解决
    

有一个递归的方法, 还没研究