from functions import average, normalize_text, select_numbers, sum_digits


def main():
    raw_digit_input = int(input("Целое число для суммы цифр: "))
    print(f"Сумма цифр - {sum_digits(raw_digit_input)}")

    raw_list_input = input("Список чисел через пробел: ").split()
    numbers = []
    for part in raw_list_input:
        numbers.append(int(part))

    avg_result = average(numbers)
    if avg_result is None:
        print("Среднее - Нет данных")
    else:
        print(f"Среднее - {avg_result:.2f}")

    raw_text = input("Произвольный текст для нормализации: ")
    print(f"Нормализованный текст - '{normalize_text(raw_text)}'")

    threshold = int(input("Порог для отбора чисел: "))
    filtered = select_numbers(numbers, threshold)
    print(f"Результат отбора (вариант 1) - {filtered}")


if __name__ == "__main__":
    main()
