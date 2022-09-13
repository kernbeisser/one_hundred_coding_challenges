from collections import Counter


def sum_fractions(lst):
    return round(sum(numerator / denominator for numerator, denominator in lst))


def get_list_of_digits(number):
    result = []
    while number != 0:
        result.append(number % 10)
        number //= 10
    return result


def harshad_number(number):
    digits = get_list_of_digits(number=number)
    return number % sum(digits) == 0


class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        # Complete the code!
        self.fullname = self.__compile_fullname__()
        self.email = self.__compile_email__()

    def __compile_fullname__(self):
        return f"{self.firstname} {self.lastname}"

    def __compile_email__(self):
        return f"{self.firstname}.{self.lastname}@company.com"


def invert(d):
    return {value: key for key, value in d.items()}


def format_date(date):
    return "".join(date.split("/")[::-1])


def is_adjacent(matrix, node1, node2):
    return matrix[node1][node2]


def num_of_sublists(lst):
    cnt = 0
    for item in lst:
        if type(item) == list:
            cnt += 1
    return cnt


def num_of_sublists2(lst):
    return sum(1 for i in lst if type(i) == list)


def histogram(lst, char):
    for item in lst:
        print(f"{item*char}\n", end="")


def histogram_return(lst, char):
    return "\n".join(i * char for i in lst)


def expensive_orders(d, p):
    return {key: value for key, value in d.items() if value > p}


def digit_occurrences(start, end, digit):
    digits = []
    for number in list(range(start, end + 1)):
        dl = list(str(number))
        digits.append(int(dl[0]))
        if len(dl) == 2:
            digits.append(int(dl[1]))
    return Counter(digits)[digit]


def digit_occurrences_ugly(start, end, digit):
    return int("".join(str(i) for i in range(start, end + 1)).count(str(digit)))


def square_patch(n):
    if n == 0:
        return []
    return [[n for x in range(n)] for y in range(n)]


def square_patch_ugly(n):
    # the solutions in this course are
    # sometimes anxthing but pythonic ...
    return [[n] * n] * n


def dna_to_rna(dna):
    tbl = str.maketrans("ATGC", "UACG")
    return dna.translate(tbl)


def valid(txt):
    return (len(txt) >= 4 and len(txt) <= 6) and all(
        [int(i) in range(0, 10) for i in txt]
    )


def valid2(txt):
    return txt.isnumeric() and len(txt) in [4, 6]


def return_unique(lst):
    return [i for i in lst if lst.count(i) == 1]


def completely_filled(lst):
    return all([False if " " in c else True for c in lst])


def longest_time(h, m, s):
    return max(h * 3600, m * 60, s)


def censor(s):
    # Eine Zensur findet nicht statt
    # Die Presse muß nicht geniert werden
    return " ".join([word if len(word) <= 4 else len(word) * "*" for word in s.split()])


def match_last_item(lst):
    return "".join(map(str, lst[:-1])) == lst[-1]


def circular_shift(lst1, lst2, n):
    return lst1[n:] + lst1[:n] == lst2


def duplicates(txt):
    c = Counter(txt)
    return sum([l - 1 for l in c.values() if l > 1])


def duplicates2(txt):
	return len(txt) - len(set(txt))


def fifth(*args):
     if len(args) >= 5:
         return type(args[4])
     else:
         return type("Not enough arguments")


def fifth2(*args):
    return type([args[4] if len(args) >= 5 else "Not enough arguments"][0])


def consecutive_combo(lst1, lst2):
    lst1.extend(lst2)
    lst1.sort()
    return lst1 == [i for i in range(min(lst1), max(lst1)+1)]


def pentagonal(num):
	if num==1: return 1
	return pentagonal(num-1) + 5*(num-1)


# das (score-dict) hätte ich ich jetzt nicht gefunden...
# der muß echt die Aufgabe besser formulieren!
# und warum is dieses dict ein 'score'?
score = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
def check_score(s):
    return max(0, sum(score[val] for row in s for val in row))


def encode_morse(txt):
	d = {'A':'.-', 'B':'-...',
		 'C':'-.-.', 'D':'-..', 'E':'.',
		 'F':'..-.', 'G':'--.', 'H':'....',
		 'I':'..', 'J':'.---', 'K':'-.-',
		 'L':'.-..', 'M':'--', 'N':'-.',
		 'O':'---', 'P':'.--.', 'Q':'--.-',
		 'R':'.-.', 'S':'...', 'T':'-',
		 'U':'..-', 'V':'...-', 'W':'.--',
		 'X':'-..-', 'Y':'-.--', 'Z':'--..',
		 '1':'.----', '2':'..---', '3':'...--',
		 '4':'....-', '5':'.....', '6':'-....',
		 '7':'--...', '8':'---..', '9':'----.',
		 '0':'-----', ',':'--..--', '.':'.-.-.-',
		 '?':'..--..', '/':'-..-.', '-':'-....-',
		 '(':'-.--.', ')':'-.--.-', '!': '-.-.--', 
		 ' ': ' ', "'": '.----.', ':': '---...'}
		 
	return ' '.join(d[i] for i in txt.upper())


def main():
    result = sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]])
    print(result)

    print(invert({"a": 1, "b": 2, "c": 3}))
    print(format_date("01/15/2019"))

    matrix = [
        [0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0],
    ]

    node1, node2 = (0, 3)
    print(is_adjacent(matrix, node1, node2))

    node1, node2 = (1, 4)
    print(is_adjacent(matrix, node1, node2))

    histogram([6, 2, 15, 3], "=")
    print(histogram_return([1, 3, 4], "#"))
    histogram([1, 3, 4], "#")

    order_rejected = expensive_orders(
        {
            "Gucci Fur": 24600,
            "Teak Dining Table": 3200,
            "Louis Vutton Bag": 5550,
            "Dolce Gabana Heels": 4000,
        },
        20000,
    )
    print(order_rejected)

    print(digit_occurrences(1, 36, 9))
    print(digit_occurrences_ugly(1, 36, 9))

    print(longest_time(15, 955, 59400))


if __name__ == "__main__":
    main()
