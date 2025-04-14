import time

def mistake(original, user_input):
    return sum(1 for o, u in zip(original, user_input) if o != u) + abs(len(original) - len(user_input))

def speed_time(start_time, end_time, user_input):
    time_taken = end_time - start_time
    words = user_input.split()
    return round(len(words) / (time_taken / 60), 2)

def calculate_accuracy(original, user_input):
    correct = sum(1 for o, u in zip(original, user_input) if o == u)
    total = max(len(original), len(user_input))
    return round((correct / total) * 100, 2) if total else 0
