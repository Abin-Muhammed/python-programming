def display_question(question, options):
    print("\n----------------------------------------")
    print(question)
    for option in options:
        print(option)

def get_user_guess():
    while True:
        guess = input("Enter option (A, B, C, D): ").upper()
        if guess in ['A', 'B', 'C', 'D']:
            return guess
        else:
            print("Invalid input. Please enter A, B, C, or D.")

def display_feedback(guess, answer):
    if guess == answer:
        print("Correct Answer!")
        return True
    else:
        print("Incorrect")
        print(f"The correct answer is {answer}")
        return False

def quiz(questions, options, answers):
    score = 0
    for question_num, question in enumerate(questions):
        display_question(question, options[question_num])
        guess = get_user_guess()
        if display_feedback(guess, answers[question_num]):
            score += 1

    print("\n*****************************************")
    print("                RESULTS                  ")
    print("*****************************************")
    print(f"You answered {score} out of {len(questions)} questions correctly.")
    percentage_score = int(score / len(questions) * 100)
    print(f"Your score is: {percentage_score}%")

if __name__ == "__main__":
    questions = (
        "Who is the first prime minister of India?",
        "How many members are there in Lok Sabha?",
        "Who is the first president of India?",
        "How many members are there in Rajya Sabha?",
        "Who is the current prime minister of India?"
    )

    options = (
        ("A. Subhash Chandra Bose", "B. Jawaharlal Nehru", "C. B.R. Ambedkar", "D. Mahatma Gandhi"),
        ("A. 245", "B. 563", "C. 543", "D. 272"),
        ("A. Dr. Rajendra Prasad", "B. APJ Abdul Kalam", "C. S. Radhakrishnan", "D. B.R. Ambedkar"),
        ("A. 272", "B. 543", "C. 563", "D. 245"),
        ("A. Narendra Modi", "B. Rahul Gandhi", "C. Amit Shah", "D. Sonia Gandhi")
    )

    answers = ("B", "C", "A", "D", "A")

    quiz(questions, options, answers)
