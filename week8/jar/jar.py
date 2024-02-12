class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"{'🍪' * self.size}"

    def deposit(self, n):
        if not n > 0:
            raise ValueError("Invalid deposit")
        current_size = self.size + n
        if current_size > self.capacity:
            raise ValueError("Capacity exceeded")
        self.size += n

    def withdraw(self, n):
        if n < 1:
            raise ValueError("Invalid withdraw")
        if n > self.size:
            raise ValueError("Not enough cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity >= 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n


def main():
    new_jar = Jar(15)
    new_jar.deposit(6)
    new_jar.deposit(5)
    new_jar.withdraw(5)
    print(new_jar.size)

if __name__ == "__main__":
    main()

