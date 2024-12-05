

def read_input():
    with open('./input.txt', 'r') as f:
        list_a = []
        list_b = []
        pairs_arr = f.read().split('\n')
        for pair in pairs_arr:
            pairs = pair.split('  ')

            list_a.append(int(pairs[0].strip()))
            list_b.append(int(pairs[1].strip()))
        sorted_a = sorted(list_a)
        sorted_b = sorted(list_b)
        return sorted_a, sorted_b

def get_distance(a, b):
    distance = 0
    for i in range(len(a)):
        distance += abs(a[i] - b[i])
    return distance

def similarity_score(a, b):
    score = 0
    for i in range(len(a)):
        score += a[i] * b.count(a[i])
    return score


def run():
    lista, listb = read_input()
    print(get_distance(lista, listb))
    print(similarity_score(lista, listb))
   
if __name__ == '__main__':
    run()