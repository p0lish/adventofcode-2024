from itertools import product

def read_from_file(path):
    with open(path, 'r') as f:
        return f.read()

def generate_values(numbers):
    def eval_expression(numbers, operations):
        """Evaluate an expression using the given numbers and operations."""
        result = numbers[0]
        for i, op in enumerate(operations):
            if op == '+':
                result += numbers[i + 1]
            elif op == '*':
                result *= numbers[i + 1]
            elif op == '|':
                result = int(str(result) + str(numbers[i + 1]))
        return result

    results = set()

    n = len(numbers)
    if n == 0:
        return results

    # Generate all possible subsets of numbers (including the full list)
            # Generate all permutations of the current subset
                # Generate all possible operations (length = len(perm) - 1)
    p1_ops = ['+', '*']
    p2_ops = ['+', '*', '|']
    for ops in product(p1_ops, repeat=len(numbers) - 1):
        result = eval_expression(numbers, ops)
        results.add(result)
    return results

def draw_output():
    lines = read_from_file('input.txt').split('\n')
    summ = 0
    for line in lines:
        line = line.split(':')
        test = int(line[0])
        numbers =  [ int(x) for x in line[1].strip().split(' ')]
        results = generate_values(numbers)
        if test in results:
            print("Found", test, "in", results)
            summ += test
    print("Founded sums: ", summ)
if __name__ == "__main__":
    draw_output()