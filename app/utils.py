import random
import operator

def generate_operation(op_type, num_count, digit_count):
    operations = {
        'sum': operator.add,
        'subtraction': operator.sub,
        'multiplication': operator.mul,
        'division': operator.truediv,
    }

    numbers = [random.randint(10**(digit_count-1), 10**digit_count - 1) for _ in range(num_count)]
    operation_str = f" {op_type} ".join(map(str, numbers))
    correct_answer = numbers[0]
    for num in numbers[1:]:
        correct_answer = operations[op_type](correct_answer, num)

    return operation_str, round(correct_answer, 2) if op_type == 'division' else correct_answer