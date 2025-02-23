import app
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def subtract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise ZeroDivisionError("Division by zero is not possible")
        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def check_types(self, *args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Parameters must be numbers")

    def sqrt(self, x):
        self.check_types(x)
        if x < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return x ** 0.5

    def log10(self, x):
        self.check_types(x)
        if x <= 0:
            raise ValueError("El logaritmo en base 10 solo está definido para números positivos.")
        return math.log10(x)

#Ejemplo de uso
if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
