def ask_question(question, correct_ans):
    """
    Ask a question, check the user's answer, and return whether it's correct.

    :param question: str, The question to be asked
    :param correct_answer: str, The correct answer to the question
    :return: int, 1 if the answer is correct, otherwise 0
    """
    answer = input(question.strip().lower())
    if answer == correct_ans.lower():
        print("Correct!")
        return 1
    else:
        print(f"Incorrect! correct answer is : {correct_ans}")
        return 0


def play_quiz():
    """
    Play the quiz game by askinnog a series of questions and calculating the score.
    """
    print("Welcome to my computer quiz!")

    game_on = input("Do you want to play game? ").strip().lower()
    if game_on != "yes":
        print("Goodbye! Thanks for stopping by.")
        return

    print("Okay, let's play! ;) ")

    score = 0
    total_questions = 4

    questions = [
        {
            "question": "What is the full form of CPU? ",
            "answer": "central processing unit",
        },
        {
            "question": "What is the full form of RAM? ",
            "answer": "random access memory",
        },
        {
            "question": "What is the full form of GPU? ",
            "answer": "graphics processing unit",
        },
        {
            "question": "What is the full form of LCD? ",
            "answer": "liquid crystal display",
        },
    ]

    for q in questions:
        score += ask_question(q["question"], q["answer"])

    print(f"You got {score} out of {total_questions} correct.")
    print(
        f"Your score is {(score / total_questions) * 100:.2f}%."
    )  # formatted to 2 decimal places for cleaner output


if __name__ == "__main__":
    play_quiz()
