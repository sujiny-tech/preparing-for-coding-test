import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        #self.stack.append(x)
        self.stack.insert(len(self.stack),x)
        print("출력 시작")
        self.print()
        print("출력 끝")


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.stack :
            return 0
        else:
            return 1
    def print(self) -> None:
        for st in self.stack:
            print(st)

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print("obj 생성")
obj.push(1)
obj.push(2)
obj.push(3)
#obj.print()
param_3 = obj.top()
print(param_3)
param_2 = obj.pop()
print(param_2)
param_4 = obj.empty()
print(param_4)