class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"{"🍪"*self.size}"

    def deposit(self, n):
        if n < 0:
            raise ValueError
        if self.size + n > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError
        if self.size - n < 0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if self.size + n > self.capacity or n < 0:
            raise ValueError
        self._size = n




def main():
    jar1 = Jar()
    print(jar1.size)
    print(jar1.capacity)
    jar1.deposit(5)
    print(jar1.size)
    current_size = jar1.size
    print(current_size)
    print(jar1)



if __name__ == "__main__":
    main()
