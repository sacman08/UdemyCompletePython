from Addition import Addition


class Calculator:
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)

    @classmethod
    def subtract(cls, num1, num2):
        return num1 - num2

    @classmethod
    def multiply(cls, num1, num2):
        # Num1 added Num2 times
        n = 0
        for m in range(1, num2 + 1):
            n = cls.add(n, num1)
        return n

    @classmethod
    def divide(cls, num1, num2):
        d = 0
        if num2 == 0:
            raise ValueError(num2)
        else:
            while num1 >= num2:
                num1 = cls.subtract(num1, num2)
                d = cls.add(d, 1)
            return f'{d} remainder {num1}'
