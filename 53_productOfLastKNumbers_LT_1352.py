class ProductOfNumbers(object):
    def __init__(self):
        self.stream = [1]          # Initialize array with 1 for prefix products
        self.n = 1                 # Track length of stream
        self.last_zero_index = -1  # Track last zero position
    
    def add(self, num):
        # If num is 0, update last_zero_index
        if num == 0:
            self.last_zero_index = self.n
        
        # If previous number was 0, just append num
        # Else multiply with previous product and append
        if self.stream[-1] == 0:
            self.stream.append(num)
        else:
            self.stream.append(self.stream[-1]*num)
        self.n += 1
        
    def getProduct(self, k):
        # If zero exists in last k numbers, return 0
        if self.last_zero_index >= self.n - k:
            return 0
            
        # If number before window is 0, return current product
        # Else divide current product by product before window starts
        if self.stream[self.n - k - 1] == 0:
            return self.stream[self.n - 1]
        else:
            return self.stream[self.n - 1] // self.stream[self.n - k - 1]
