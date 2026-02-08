class MinStack:
    """

    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.



    Example 1:

    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2


    Constraints:

    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.


    MAIN INTUITION:

    Using any other data structure like hashmaps or a single list or trees, we cant achieve getMin in 0(1). 
    Instead, we use another stack where can just store the min. 

    For example, push -> -2, 0, -2, 3 

    If you use a global variable, u track the -3 but if it gets popped, you have no idea what the prev min was. 
    In a second stack, u can check if your current push is less than your current min and push, 

    -2, -3 

    After you pop -3, -2 is the current min now. 

    Time: 

    - append, pop last element and lookup based on index is 0(1)
    - all operations are constant time 

    Space:

    - 0(n): where self.s can grow to the number of elements pushed
    [Worst case: decreasing array where self.t also gets pushed n elements] 



    """

    def __init__(self):
        self.s = []
        self.t = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.t or val <= self.t[-1]:
            self.t.append(val)

    def pop(self) -> None:
        ele = self.s.pop()
        if self.t and self.t[-1] == ele:
            self.t.pop()

    def top(self) -> int:
        if self.s:
            return self.s[-1]

    def getMin(self) -> int:
        if self.t:
            return self.t[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
