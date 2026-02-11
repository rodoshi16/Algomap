***What is Monotonic stack?***

Just a stack that is kept in a specific order. 

- monotonically increasing 
- monotonically decreasing 


***When to use this?***

- Next greater element
- Next smaller element
- Previous greater/smaller 
- Histogram/rectangle problems
- Daily temperate
- Stock span 

Each element is pushed and poppped at most once. 
Main idea is: if your current element breaks monotonic order, pop from the stack untill the order is restored. 

**Example**

For each number, find the next greater element to the right. 

[5, 3, 8, 2, 7]

Brute force: for each element, traverse through rest of array and keep updating global variable. 0(n^2)

Monotonic Stack: use the a stack to store elements that haven't found a greater pair. 

Push(5)
3 < 5 (so can't pop)
Push(3)
8 > 5 (8 is the next greater for both)
Pop(5), Pop(3)
Push(8)
Push(2)
7 > 2
Pop(2)
Push(7)

Stack: 5, 3
       8, 2

Elements in stack is always decreasing because if a greater element is next we pop the smaller ones. Hence a monotonic decreasing stack. 

**Shortcut** -> next greater (decreasing), next smaller(increasing)

[5, 3, 8, 2, 7]

Push(5)
Push(3)
Pop(5)
Push(8)
Push(2)
Pop(8)
Push(7)

***Rectangle problems***

(the bane of monotonic stacks)

[2, 1, 5, 6, 2, 3]

At each point, 

- how far right can i go while bar height is greater than mine?
- store the indices that are still waiting for a smaller bar 

[1, 2, 3]
[1, 4, 5]

- for each bar, we want the left boundary and right boundary to see how far it can stretch
- width = right - left 
- area = height * width 

[1,4,5,0]

pop(5) = right - left -1 = 6-4-1 = 1 
area = bar[5] = 3 * 1

pop(4) = 6-1-1 = 4
area = bar[4] = 2 * 4 

pop(1) = 6-0-1 = 5
area = bar[1] = 2 *5 








