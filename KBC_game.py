# KBC game:
# *Note this code is under testing stage dont use it until this note disappears this note means it is not checked yet
print("|----You are playing KBC----|")
ques_list = ["Q.1What is the capital of India?", "Q.2In which state Jaipur is?", "Q.3How many colors are there in Rainbow?"] # This is the list containg questions
i = 0
 # We used while loops to showcase quesiton and in that we are showcasing questions 1 by 1 and then we are going to collect the entered answers in the file and then going to match the answers with the presented answers
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
# Here below we are checking answers 
if(answers == content):
    print("Your all answers are correct")
    with open("answers.txt", "w") as f:
        f.write("")
else:
    print("Your some or all answers are incorrect")
    with open("answers.txt", "w") as f:
        f.write("")