class MyQueue(object):

    def __init__(self):
        self.s1 = [] # primary stack
        self.s2 = [] #help for reversing operation

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop()) #copy the s1 to s2
        self.s1.append(x) #append new elements

        while self.s2:
            self.s1.append(self.s2.pop()) # again copy s2 to s1 for mainting order

    def pop(self):
        return self.s1.pop() #return the top element
        

    def peek(self):
        return self.s1[-1] #return the top of stack
        

    def empty(self):
        return not self.s1 #return self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
