english_alphabet_letters_num = 26
possible_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
letters = {'0': possible_letters.copy(), '1': possible_letters.copy(), '2': possible_letters.copy(),
           '3': possible_letters.copy(), '4': possible_letters.copy()}
colours = {'S': 0, 'N': 0, 'Z': 0}
pairs_num = int(input())
known_cells = 0
unknown_cells = 5
Nletters = {}


def get():
    global known_cells, unknown_cells
    word = input()
    snz = input()

    for i in '01234':
        letter = word[int(i)]
        appearance = snz[int(i)]
        if appearance == 'S':
            colours['S'] += 1
            for j in '01234':
                if type(letters[j]) == list and letter in letters[j]:
                    letters[j].pop(letters[j].index(letter))
        elif appearance == 'N':
            colours['N'] += 1
            list1to5 = list(range(5))
            list1to5.pop(int(i))
            Nletters[letter] = list1to5.copy()
            if letter in letters[i]:
                letters[i].pop(letters[i].index(letter))
        elif appearance == 'Z':
            colours['Z'] += 1
            if letter in Nletters.keys():
                Nletters.pop(letter)
            letters[i] = letter
            known_cells += 1
            unknown_cells -= 1


def evaluate_n_numbers():
    for i in Nletters.keys():
        for j in range(len(letters)):
            if type(letters[str(j)]) == str:
                if type(Nletters[i]) == int and j == Nletters[i]:
                    Nletters[i].pop(Nletters[i].index(j))
                elif j in Nletters[i]:
                    Nletters[i].pop(Nletters[i].index(j))

    for i in Nletters.keys():
        if (type(Nletters[i]) == list and len(Nletters[i]) == 1) or (type(Nletters[i]) == int):
            letters[str(Nletters[i][0])] = i


def evaluate():
    evaluate_n_numbers()
    list_keys = []
    for i in range(5):
        if type(letters[str(i)]) == list:
            list_keys.append(str(i))

    if len(list_keys) == 0:
        return 1
    if len(list_keys) == 1:
        return len(letters[list_keys[0]])
    if len(list_keys) > 1:
        result = 1
        for i in list_keys:
            result = result*len(letters[str(i)])
        return result


def main():
    for i in range(pairs_num):
        get()

    result = evaluate()
    print(result)


main()
