class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if a == 0 or b == 0:
                return 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        # Add before the loop
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        # Add before the loop
        if b == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed.")
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))