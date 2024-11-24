###################game quiz
print("Welcome to my Computer Quize")
number_of_question = 4
score = 0
playing = input("Do you want to play? ").lower()
print(playing)
if playing != "yes":
    quit()

print("Okey Lets play ;) ")

answer = input("What is the full form of CPU? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrcet! Correct answer is : 'central processing unit' ")

answer = input("What is the full form of GPU? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrcet! Correct answer is : 'graphics processing unit' ")

answer = input("What is the full form of RAM? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrcet! Correct answer is : 'random access memory' ")

answer = input("What is the full form of PSU? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrcet! Correct answer is : 'power supply unit' ")

print(f"you got {score} correct answers")
print(f"youre percentage is: {((score / number_of_question) * 100)}%")
