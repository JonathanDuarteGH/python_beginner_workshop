# # Python quiz game

# questions = ("How many elements are in the periodic table? ",
#              "Which animal lays the largest eggs?: ",
#              "What is the most abundant gas in Earth's atmosphere?: ",
#              "How many bones are in the human body?: ",
#              "Which planet in the solar system is the hottest?: ")

# options = (("A. 116", "B. 117", "C. 118", "D. 119"),
#            ("A. Ostrich", "B. Whale", "C. Crocodile", "D. Salmon"),
#            ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
#            ("A. 206", "B. 208", "C. 210", "D. 212"),
#            ("A. Venus", "B. Mercury", "C. Mars", "D. Jupiter"))

# answers = ("C", "D", "B", "A", "B")
# guesses = []
# question_num = 0

# for question in questions:
#     print("--------------------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess= input("Enter (A, B, C, or D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         print("CORRECT!")
#     else:
#         print("WRONG!")
#         print(f"{answers[question_num]} is the correct answer.")
#     question_num += 1

# print("-----------------------------------")
# print("            RESULTS                ")
# print("-----------------------------------")

# print("Answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("Guesses: ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# # count correct answers
# score = 0
# for i in range(len(answers)):
#     if guesses[i] == answers[i]:
#         score += 1

# # convert to percentage
# score = int(score / len(questions) * 100)
# print(f"Your score is: {score}%")

# fruits = ["apples", "bananas", "cherries", "dates"]
# print(dir(fruits))

import math

print(math.pi)