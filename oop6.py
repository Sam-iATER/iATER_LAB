class SimpleCalculator:

    @staticmethod
    def add(first_num, second_num):
        return first_num + second_num

    @staticmethod
    def subtrack(first_num, second_num):
        return first_num - second_num

    @staticmethod
    def mutiply(first_num, second_num):
        return first_num * second_num

    @staticmethod
    def divide(first_num, second_num):
        return first_num / second_num


calculator = SimpleCalculator()

print(calculator.add(4, 5))
print(calculator.subtrack(4, 5))
print(calculator.mutiply(4, 5))
print(calculator.divide(4, 5))
