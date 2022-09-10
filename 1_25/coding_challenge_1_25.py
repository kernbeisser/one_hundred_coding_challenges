import re
import math
from functools import reduce


def string_int(txt):
    try:
        return int(txt)
    except ValueError:
        print(f"'{txt}' could not be converted to an integer!")

def bool_to_string(flag : bool) -> str:
    return str(flag)

def get_first_value(number_list):
	return number_list[0]

def football_points(wins, draws, losses):
    return 3 * wins + 1 * draws + 0 * losses

def give_me_something(a):
    return f"something {a}"

def is_same_num(num1, num2):
    return num1 == num2

def concat(lst1, lst2):
	return lst1 + lst2

def less_than_or_equal_to_zero(num):
  return num <= 0

def findLargestNum(nums):
    return max(nums)

def find_smallest_num(lst):
    return min(lst)

def difference_max_min(lst):
    return max(lst) - min(lst)

def name_shuffle(txt):
    last, fist = txt.split()
    return fist + " " + last

def replace_vowels2(txt, ch):
    s2 = ""
    for v in txt:
        if v in "aeiou":
            s2 += ch
        else:
            s2 += v
    return s2

def replace_vowels(txt, ch):
	return re.sub(r'[aeiouAEIOU]', ch, txt)

def evenly_divisible(a, b, c):
	return sum(i for i in range(a, b+1) if not i%c)

def evenly_divisible2(a, b, c):
    result = 0
    for n in range(a, b+1):
        if n % c == 0:
            result += n
    return result

def factorial(num):
    return math.factorial(num)

def factorial_rec(num):
	return 1 if num < 2 else num * factorial(num - 1)

def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/' and num2 != 0:
        return num1 / num2
    else:
        return "Can't divide by 0!"

def calculator_eval(n1, operator, n2):
	try: 
		return eval(str(n1) + operator + str(n2))
	except ZeroDivisionError:
		return "Can't divide by 0!"

def correct_stream(user, correct):
    result = list()
    for a, b in zip(user, correct):
        result.append(1) if a == b else result.append(-1)
    return result

def correct_stream_solution(user, correct):
	return [1 if user[i] == correct[i] else -1 for i in range(len(user))]

def get_list_of_digits(number):
    result = []
    while number != 0:
        result.append(number % 10)
        number //= 10
    return result

def mean(num):
    lst = get_list_of_digits(num)
    return sum(lst) / len(lst)


def total_volume(*boxes):
    # meine ist eleganter!
    # need: from functools import reduce

   result = 0
   for box in boxes:
       result += reduce(lambda x, y: x*y, box)
   return result

def total_volume_solution(*boxes):
	return sum([x*y*z for x,y,z in boxes])

def get_student_names(students):
    lst = list(students.values())
    return sorted(lst)

def return_only_integer(lst):
    return [item for item in lst if type(item) == int]

def next_in_line(lst, num):
    if not lst:
        return "No list has been selected"
    lst.append(num)
    lst.pop(0)
    return lst

def next_in_line_solution(lst, num):
	return lst[1:] + [num] if lst else "No list has been selected"

def missing_num(lst):
    # using the arithmetic progression formula
    # it gives a float result --> int()
    # the solution: sum(list(range(1, 11))) - sum(lst)
    # only works for constant diff of 1 !
    return int(lst[-1] * (lst[-1] + lst[0]) / 2 - sum(lst))

def main():
    print(string_int("125"))
    print(string_int("xyz"))
    print(bool_to_string(True))
    print(bool_to_string(False))
    print(get_first_value([9, 8, 7]))
    print(football_points(5, 0, 2))
    print(give_me_something(", huh?"))


if __name__ == '__main__':
    main()