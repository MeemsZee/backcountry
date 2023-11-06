class Jar:
    def __init__(self, capacity=12):
        #if capacity is a not a positive number, raise a valueerror
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        #returns a str with number of cookie emojis
        return "🍪" * self.size
    
    def deposit(self, n):
        #adds n cookies to jar, if there are more than capacity of cookies, raise valueerror
        if self.size + n > self.capacity:
            raise ValueError("Cookie jar won't close, add fewer cookies")
        self.size += n


    def withdraw(self, n):
        #removes n cookies from jar.  if there are that many cookies in the cookie jar, raise value error
        if self.size - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self.size -= n 

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if not isinstance(capacity,int) or capacity < 1:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if size > self.capacity or size < 0:
            raise ValueError
        self._size = size