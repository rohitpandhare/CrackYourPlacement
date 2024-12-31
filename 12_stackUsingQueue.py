class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        while self.q1:
            self.q2.append(self.q1.popleft()) #popping the first entered element and adding it to q2
        self.q1.append(x) #appending new elements to q1

        while self.q2:
            self.q1.append(self.q2.popleft()) #to maintain LIFO append the q1 with q2
        

    def pop(self):
        #return the left most element( just like stack's top)
        return self.q1.popleft()
        

    def top(self):
        #return the first element( just like stack's top)
        return self.q1[0]
        

    def empty(self):
        return not self.q1 #will check the queue which is acting as stack is empty or not
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
