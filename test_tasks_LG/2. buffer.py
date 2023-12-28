# С использованием списка:

class RingBuffer1:
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.start = 0
        self.end = 0
        self.count = 0

    def isEmpty(self):
        return self.count == 0 and self.start == self.end

    def isFull(self):
        return self.count == self.size and self.start == self.end
        
    def push(self, item):
        if self.isFull():
            raise Exception('Ring buffer is full')
        self.buffer[self.end] = item
        self.end = (self.end + 1) % self.size
        self.count += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Buffer is empty")
        item = self.buffer[self.start]
        self.start = (self.start + 1) % self.size
        self.count -= 1
        return item
        
# С использованием очереди:
from collections import deque

class RingBuffer2:
    def __init__(self, size):
        self.size = size
        self.buffer = deque(maxlen=self.size)
    
    def isEmpty(self):
        return len(self.buffer) == 0
    
    def isFull(self):
        return len(self.buffer) == self.size
    
    def push(self, item):
        if self.isFull():
            raise Exception("Ring buffer is full")
        self.buffer.append(item)
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Ring buffer is empty")
        return self.buffer.popleft()