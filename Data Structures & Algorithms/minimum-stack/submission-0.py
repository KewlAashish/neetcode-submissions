class MinStack:
    def __init__(self):
        self.st_1 = []
        self.st_2 = []

    def push(self, val: int) -> None:
        if not self.st_2 or val <= self.st_2[-1]:
            self.st_2.append(val)
        self.st_1.append(val)

    def pop(self) -> None:
        val = self.st_1[-1]
        if val == self.st_2[-1]:
            self.st_2.pop()
        
        self.st_1.pop()

    def top(self) -> int:
        return -1 if not self.st_1 else self.st_1[-1]

    def getMin(self) -> int:
        return -1 if not self.st_2 else self.st_2[-1]