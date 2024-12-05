

def read_from_file(path):
    with open(path, 'r') as f:
        return f.read()

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle-1)])

def check_order(page, raw_ruleset):
    ordered = True
    for rule in raw_ruleset:
            rule = rule.split('|')
            rule = [str(x) for x in rule]
            left = rule[0]
            right = rule[1]
            if left in page and right in page:
                leftindex = page.index(left)
                rightindex = page.index(right)
                if leftindex > rightindex:
                    ordered = False
                    break
    return ordered

def fix_order(page, raw_ruleset):
    ordered = True
    for rule in raw_ruleset:
            rule = rule.split('|')
            rule = [str(x) for x in rule]
            left = rule[0]
            right = rule[1]
            if left in page and right in page:
                leftindex = page.index(left)
                rightindex = page.index(right)
                if leftindex > rightindex:
                    ordered = False
                    page[rightindex], page[leftindex] = page[leftindex], page[rightindex]
    return ordered
        

def run():
    lines = read_from_file('./input.txt').split('\n')
    raw_ruleset = []
    pages = []
    split_happend = False
    for line in lines:
        if split_happend:
            pages.append(line)
        else:
            if line == "":
                split_happend = True
            else:
                raw_ruleset.append(line)
    
    ordered_sum = 0
    fixed_sum = 0
    circuit_breaker = 5000
    for i in pages:
        page = i.split(',')
        ordered = check_order(page, raw_ruleset)
        if ordered:
            ordered_sum += int(findMiddle(page))
        else:
            while True and circuit_breaker > 0:
                ordered = fix_order(page, raw_ruleset)
                circuit_breaker -= 1
                if ordered:
                    fixed_sum += int(findMiddle(page))
                    break     
    print(f"Solution 1: {ordered_sum}")
    print(f"Solution 2: {fixed_sum}")

if __name__ == '__main__':
    run()