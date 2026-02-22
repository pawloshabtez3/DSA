from collections import deque

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        # Push to q2
        self.q2.append(x)
        
        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        Removes the element on top of the stack and returns it.
        :rtype: int
        """
        return self.q1.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q1) == 0