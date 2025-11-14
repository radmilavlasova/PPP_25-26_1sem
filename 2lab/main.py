def filter_letters(s: str) -> str:
    letters = [ch for ch in s if ch.isalpha() and 'a' <= ch.lower() <= 'z']
    lower_cnt = {}
    upper_cnt = {}

    for ch in letters:
        key = ch.lower()
        if ch.islower():
            lower_cnt[key] = lower_cnt.get(key, 0) + 1
        else:
            upper_cnt[key] = upper_cnt.get(key, 0) + 1

    to_remove = {
        key for key in set(lower_cnt) | set(upper_cnt)
        if lower_cnt.get(key, 0) > upper_cnt.get(key, 0)
    }

    result = ''.join(ch for ch in letters if ch.lower() not in to_remove)
    return result

user_input = input("Введите строку: ")
output = filter_letters(user_input)
print("Результат:", output)


