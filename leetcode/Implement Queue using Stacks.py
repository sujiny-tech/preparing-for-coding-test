class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.q.insert(len(self.q), x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.q.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.q:
            return 0
        else:
            return 1

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)

param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print( param_3, param_2, param_4)
