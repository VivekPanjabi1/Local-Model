import datetime


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome."


def today_info() -> str:
    now = datetime.datetime.now()
    return f"Today is {now.strftime('%A, %B %d, %Y')}."


def days_until_new_year() -> int:
    today = datetime.date.today()
    next_year = datetime.date(today.year + 1, 1, 1)
    return (next_year - today).days


if __name__ == "__main__":
    print(greet("Vivek"))
    print(today_info())
    print(f"Days until New Year: {days_until_new_year()}")
