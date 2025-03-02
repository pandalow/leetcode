# 138. Copy List with Random Pointer

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return *the head of the copied linked list*.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will **only** be given the `head` of the original linked list.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/12/18/e1.png)

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/12/18/e2.png)

```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

```

**Example 3:**

![](https://assets.leetcode.com/uploads/2019/12/18/e3.png)

```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

```

**Constraints:**

- `0 <= n <= 1000`
- `104 <= Node.val <= 104`
- `Node.random` is `null` or is pointing to some node in the linked list.

- Recursive solution
    
    ```python
    """
    # Definition for a Node.
    class Node:
        def __init__(self, x, next=None, random=None):
            self.val = int(x)
            self.next = next
            self.random = random
    """
    
    class Solution(object):
        def __init__(self):
            self.visitedHash = {}
    
        def copyRandomList(self, head):
            """
            :type head: Node
            :rtype: Node
            """
            if head == None:
                return None
    
            if head in self.visitedHash:
                return self.visitedHash[head]
    
            new_node = Node(head.val,None,None)
    
            self.visitedHash[head] = new_node
    
            new_node.next = self.copyRandomList(head.next)
            new_node.random = self.copyRandomList(head.random)
    
            return new_node
    ```
    
- explain
    
    ### **Approach 1: Recursive**
    
    **Intuition**
    
    The basic idea behind the recursive solution is to consider the linked list like a graph. Every node of the Linked List has 2 pointers (edges in a graph). Since, random pointers add the randomness to the structure we might visit the same node again leading to cycles.
    
    ![](https://leetcode.com/problems/copy-list-with-random-pointer/solutions/169069/Figures/138/138_Copy_List_Random_2.png)
    
    In the diagram above we can see the random pointer points back to the previously seen node hence leading to a cycle. We need to take care of these cycles in the implementation.
    
    All we do in this approach is to just traverse the graph and clone it. Cloning essentially means creating a new node for every unseen node you encounter. The traversal part will happen recursively in a depth first manner. Note that we have to keep track of nodes already processed because, as pointed out earlier, we can have cycles because of the random pointers.
    
    **Algorithm**
    
    1. Start traversing the graph from`head`node.
        
        Lets see the linked structure as a graph. Below is the graph representation of the above linked list example.
        
        ![](https://leetcode.com/problems/copy-list-with-random-pointer/solutions/169069/Figures/138/138_Copy_List_Random_7.png)
        
        In the above example`head`is where we begin our graph traversal.
        
    2. If we already have a cloned copy of the current node in the visited dictionary, we use the cloned node reference.
    3. If we don't have a cloned copy in the visited dictionary, we create a new node and add it to the visited dictionary.
        
        `visited_dictionary[current_node] = cloned_node_for_current_node.`
        
    4. We then make two recursive calls, one using the`random`pointer and the other using`next`pointer. The diagram from step 1, shows`random`and`next`pointers in red and blue color respectively. Essentially we are making recursive calls for the children of the current node. In this implementation, the children are the nodes pointed by the`random`and the`next`pointers.