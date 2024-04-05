class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for num in args[1:]:
            result /= num
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result


# Example usage:
print(Calculator.add(5, 10, 15))  # Output: 30
print(Calculator.multiply(2, 3, 4))  # Output: 24
print(Calculator.divide(100, 2, 5))  # Output: 10.0
print(Calculator.subtract(20, 5, 3))  # Output: 12
