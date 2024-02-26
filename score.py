"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

EXCELLENT_SCORE = 90
PASS_SCORE = 50

score = float(input("Enter score: "))
if score >= EXCELLENT_SCORE:
    print("Excellent")
elif score >= PASS_SCORE:
    print("Pass")
else:
    print("Bad")
