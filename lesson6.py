def is_very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isalnum() for char in password)


def password_score(password):
    score = 0
    checks = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    for check in checks:
        if check(password):
            score += 2
    return score


def main():
    password = input("Введите пароль: ")
    score = password_score(password)
    print("Рейтинг пароля:", score)


if __name__ == "__main__":
    main()
