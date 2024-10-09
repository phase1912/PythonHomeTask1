import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r'(?<!\S)(-?\d+(?:\.\d+)?)(?!\S)'
    matches = re.findall(pattern, text)

    for m in matches:
        yield float(m)

def sum_profit(text: str, func: Callable):
    sum = 0.0

    for result in func(text):
        sum += result

    return sum

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == "__main__":
    main()