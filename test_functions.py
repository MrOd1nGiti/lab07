from functions import average, normalize_text, select_numbers, sum_digits

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12

assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9

assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

test_list = [-5, 0, 2, 5]
original_copy = test_list.copy()

assert select_numbers(test_list, 2) == [5]
assert select_numbers([], 2) == []
assert select_numbers([5, 5, 1], 2) == [5, 5]

assert test_list == original_copy

print("Все проверки успешно пройдены")
