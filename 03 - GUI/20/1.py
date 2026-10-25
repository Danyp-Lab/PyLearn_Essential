# بررسی متقارن بودن آرایه
def is_symmetric(array):
    return array == array[::-1]


# تولید جفت‌های تصادفی برای ازدواج
import random


def random_marriage(boys, girls):
    random.shuffle(boys)
    random.shuffle(girls)
    return list(zip(boys, girls[: len(boys)]))


# پیاده‌سازی بازی "پاالم، پولوم، پيليش"
def play_game():
    options = ["✋", "✌️"]
    user_score, computer1_score, computer2_score = 0, 0, 0

    for _ in range(5):
        user_choice = input("انتخاب کنید ✋ یا ✌️: ")
        computer1_choice = random.choice(options)
        computer2_choice = random.choice(options)
        print(f"کامپیوتر ۱: {computer1_choice}, کامپیوتر ۲: {computer2_choice}")

        # اینجا باید منطق برنده شدن را بر اساس قوانین بازی پیاده‌سازی کنید

    # در انتها برنده کلی را مشخص کنید


# نمونه استفاده
print(is_symmetric([1, 4, 3, 4, 1]))  # خروجی: True
print(is_symmetric([1, 2, 3]))  # خروجی: False

boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]
print(random_marriage(boys, girls))

play_game()
