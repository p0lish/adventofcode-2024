

def read_from_file(path):
    with open(path, 'r') as f:
        return f.read()

def run():
    cont = read_from_file('input.txt')
    sum = 0
    for char in cont.split("mul("):
        numbers = char.split(")")[0]
        numbers = numbers.split(",")

        if len(numbers) == 2:
            try:
                a = int(numbers[0])
                b = int(numbers[1])
                print(a * b)
                sum += a * b
            except ValueError:
                pass
        print(sum)

def run2():
    cont = read_from_file('input.txt')
    sum = 0
    chars = cont.split("don't()")
    ok_lines = chars.pop(0)
    for char in chars:
        ok_line = char.split("do()")
        del ok_line[0]
        ok_lines += "".join(ok_line)
    
    for char in ok_lines.split("mul("):
        numbers = char.split(")")[0]
        numbers = numbers.split(",")

        if len(numbers) == 2:
            try:
                a = int(numbers[0])
                b = int(numbers[1])
                print(a * b)
                sum += a * b
            except ValueError:
                pass
        print(sum)


if __name__ == '__main__':
    run2()
