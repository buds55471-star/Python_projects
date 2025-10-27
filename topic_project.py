''' Choose one:

💡 Simple Calculator (takes two numbers + operation)

💡 Number Guessing Game (random number between 1–10)

💡 Basic Quiz App (ask 3-5 questions and score user)

💡 Age in Days Calculator (user enters birth year)'''

print("----- Basic Quiz App -----")

score = 0  # To keep track of correct answers

# Q1
print("\nQ1: Who is the Prime Minister of India?")
print("(A): Indira Gandhi")
print("(B): Rahul Gandhi")
print("(C): Narendra Modi")
print("(D): Arvind Kejriwal")
answer1 = input("Your answer: ").strip().upper()
if answer1 == "C":
    score += 1

# Q2
print("\nQ2: Which city is the capital of India?")
print("(A): Punjab")
print("(B): Odisha")
print("(C): New Delhi")
print("(D): Bihar")
answer2 = input("Your answer: ").strip().upper()
if answer2 == "C":
    score += 1

# Q3
print("\nQ3: Who is the CEO of Google?")
print("(A): Sundar Pichai")
print("(B): Elon Musk")
print("(C): Satya Nadella")
print("(D): Jeff Bezos")
answer3 = input("Your answer: ").strip().upper()
if answer3 == "A":
    score += 1

# Q4
print("\nQ4: Who is the CEO of Amazon?")
print("(A): Sundar Pichai")
print("(B): Elon Musk")
print("(C): Steve Jobs")
print("(D): Jeff Bezos")
answer4 = input("Your answer: ").strip().upper()
if answer4 == "D":
    score += 1

# Final Score
print(f"\nYour final score is {score}/4")
