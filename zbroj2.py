import sys

broj_znamenaka = int(input())
zbroj_znamenaka = int(input())
if broj_znamenaka + 10 > 640:
    sys.set_int_max_str_digits(broj_znamenaka + 10)


def zbrojznamenaka(broj):
    return 0 if broj == 0 else int(broj % 10) + zbrojznamenaka(int(broj / 10))


def get_sum_elements(digit_sum):
    sum_elements = []
    while digit_sum > 0:
        difference = digit_sum - 9
        if difference >= 0:
            digit_sum = difference
            sum_elements.append(9)
        else:
            sum_elements.append(digit_sum)
            digit_sum = 0
    return sum_elements


def create_najveci(sum_elements):
    result_str = ''
    for i in sum_elements:
        result_str += str(i)
    for i in range(broj_znamenaka - len(result_str)):
        result_str += '0'
    return result_str


def create_najmanji(num_list):
    if len(num_list) != broj_znamenaka:
        mnum_list = list(reversed(num_list.copy()))
        mnum_list[0] = mnum_list[0] - 1
        result = '1'
        for i in range(broj_znamenaka - len(num_list) - 1):
            result += '0'
        for i in mnum_list:
            result += str(i)
        return result
    elif len(list(set(num_list))) == 1:
        return create_najveci(num_list)
    elif len(num_list) == broj_znamenaka:
        mnum_list = list(reversed(num_list.copy()))
        result = ''
        for i in mnum_list:
            result += str(i)
        return result
    else:
        result = str(num_list[0])
        for i in range(broj_znamenaka - len(num_list)):
            result += '0'
        return result



a = get_sum_elements(zbroj_znamenaka)
najveci = create_najveci(a)
najmanji = create_najmanji(a)
print(najmanji)
print(najveci)
