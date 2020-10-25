class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q=[]
        self.size=k
        self.cur_size=0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.cur_size<self.size:
            self.q.insert(len(self.q), value)
            self.cur_size+=1
            return True
        else:
            return False
        #self.q.insert(len(self.q), value)
        #self.cur_size+=1
        #if self.q[-1]==value:
        #    return True
        #else:
        #    return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.q :
            self.q.pop(0)
            self.cur_size-=1
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.q:
            return self.q[0]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.q:
            return self.q[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.q:
            return False
        else:
            return True

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.size==self.cur_size:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)

param_1 = obj.enQueue(1)
param_12 = obj.enQueue(2)
param_13 = obj.enQueue(3)
param_14 = obj.enQueue(4)

param_2 = obj.Rear()
param_3 = obj.isFull()
param_4 = obj.deQueue()
param_15 = obj.enQueue(4)
param_41 = obj.Rear()
#param_3 = obj.Front()
#param_5 = obj.isEmpty()
#obj,
print( param_1,param_12, param_13, param_14, param_2, param_3, param_4, param_15, param_41 )