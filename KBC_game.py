# KBC game:

print("|----You are playing KBC----|")
ques_list = ["Q.1What is the capital of India?", "Q.2In which state Jaipur is?", "Q.3How many colors are there in Rainbow?"]
i = 0
while(i<len(ques_list)):
    print(ques_list[i])
    a = input("Enter number: ")
    with open(f"answers.txt", "a") as f:
        f.write(f"{a}\n")
        print("")
    with open(f"answers.txt") as f:
        answers = f.read()
    with open("answers_check.txt") as f:
        content = f.read()
    i += 1
print("You have attempted all the question")
if(answers == content):
    print("Your all answers are correct")
    with open("answers.txt", "w") as f:
        f.write("")
else:
    print("Your some or all answers are incorrect")
    with open("answers.txt", "w") as f:
        f.write("")