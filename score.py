import random

EXCELLENT_SCORE = 90
PASS_SCORE = 50
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    score = get_valid_score()
    result = determine_grade(score)
    print(result)
    random_score = random.uniform(MINIMUM_SCORE, MAXIMUM_SCORE)
    random_score_result = determine_grade(random_score)
    print(f"Random score: {random_score}")
    print(random_score_result)


def get_valid_score():
    score = get_score()
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid Score!")
        score = get_score()
    return score


def determine_grade(score):
    if score >= EXCELLENT_SCORE:
        print("Excellent")
    elif score >= PASS_SCORE:
        print("Pass")
    else:
        print("Bad")


def get_score():
    score = float(input("Enter score: "))
    return score


main()
