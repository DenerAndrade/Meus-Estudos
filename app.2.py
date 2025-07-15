class Vetor:
    def __init__(self, n1):
        self.n1 = n1

    def __sub__(self, n):
        if not isinstance(n, int):
            n = int(n)
        return self.n1 - n

    def __eq__(self, n):
        return True if self.n1 == n else False


x = Vetor(4)

print(x == 2)
