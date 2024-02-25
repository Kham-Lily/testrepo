MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90
PASS_SCORE = 50
DEFAULT_SCORE = -1


def main():
    score = DEFAULT_SCORE
    """Get score from the users and display their status."""
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score == DEFAULT_SCORE:
                print(f"No score entered, please get the score first!")
                score = get_valid_score()
            determine_status(score)
        elif choice == "S":
            if score == DEFAULT_SCORE:
                print("No score entered, please get score first")
                score = get_valid_score()
            display_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("choice: ").upper()
    print("Farewell")


def determine_status(score):
    """Determine the status."""
    if score >= EXCELLENT_SCORE:
        print("Excellent")
    elif score >= PASS_SCORE:
        print("Pass")
    else:
        print("Bad")


def get_valid_score():
    """Get the valid score from the users."""
    score = get_score()
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score!")
        score = float(input("Enter score: "))
    return score


def get_score():
    """Get score from the users."""
    score = float(input("Enter score: "))
    return score


def display_stars(score):
    """Display stars according to number of user's score."""
    print("*" * int(score))


main()
