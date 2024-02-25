"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

EXCELLENT_SCORE = 90
PASS_SCORE = 50


def main():
    """Get score from the users and display their status."""
    score = get_score()
    determine_status(score)


def determine_status(score):
    """Determine the status."""
    if score >= EXCELLENT_SCORE:
        print("Excellent")
    elif score >= PASS_SCORE:
        print("Pass")
    else:
        print("Bad")


def get_score():
    """Get score from the users."""
    score = float(input("Enter score: "))
    return score


main()
