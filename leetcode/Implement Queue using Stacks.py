class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #선입선출, ->
        self.q=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.q.insert(len(self.q), x)
        #self.q.append(x)
        #큐는 앞에서부터 차곡차곡 쌓고
        #먼저들어온애가 나가고

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