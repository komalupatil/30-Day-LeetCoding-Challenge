#Problem10

#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#getMin() -- Retrieve the minimum element in the stack.
#Example:
#MinStack minStack = new MinStack();
#minStack.push(-2);
#minStack.push(0);
#minStack.push(-3);
#minStack.getMin();   --> Returns -3.
#minStack.pop();
#minStack.top();      --> Returns 0.
#minStack.getMin();   --> Returns -2.

#Solution - using two stacks 

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack)==0 or x <= self.minStack[-1]:
            self.minStack.append(x)
                
    def pop(self) -> None:
        last = self.stack.pop()
        if last == self.minStack[-1]:
            self.minStack.pop()
               
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()