import random
import time
from utils import mistake, speed_time, calculate_accuracy

def get_random_passage():
    try:
        with open("tests/sample_texts.txt", "r") as file:
            texts = file.readlines()
        return random.choice(texts).strip()
    except FileNotFoundError:
        return "The quick brown fox jumps over the lazy dog."

if __name__ == "__main__":
    print("👋 Welcome to TypeTester!")
    attempts = 0
    total_accuracy = 0

    while True:
        ready = input("\nReady to test your typing? (yes/no): ").lower()
        if ready != 'yes':
            break

        passage = get_random_passage()
        print(f"\n📝 Type this:\n{passage}")
        input("Press Enter to start...")

        start = time.time()
        typed_input = input("\nStart typing here:\n")
        end = time.time()

        wpm = speed_time(start, end, typed_input)
        errors = mistake(passage, typed_input)
        accuracy = calculate_accuracy(passage, typed_input)

        print(f"\n📊 Results:")
        print(f"Speed: {wpm} WPM")
        print(f"Mistakes: {errors}")
        print(f"Accuracy: {accuracy}%")

        attempts += 1
        total_accuracy += accuracy

    if attempts > 0:
        avg_accuracy = round(total_accuracy / attempts, 2)
        print(f"\n✅ You attempted {attempts} time(s). Average Accuracy: {avg_accuracy}%")
    print("\nThanks for using Typetester. Goodbye! 👋")
