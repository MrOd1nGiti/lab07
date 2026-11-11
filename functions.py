def sum_digits(number):
    total = 0
    current = abs(number)
    while current > 0:
        total += current % 10
        current //= 10
    return total


def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    selected = []
    for number in numbers:
        if number > threshold:
            selected.append(number)
    return selected
