print("--Welcome To Kon Banega Crorepati--\n") # Heading

# Below it the function for playing KBC game
def play_quiz():
    # This below list containes the questions that will be asked from the used
    question_list = ["Q.1 What is the capital of India ?", "Q.2 How many colors are there in rainbow ?", "Q.3 In which state Jaipur lies ?", "Q.4 Who is the prime minister of india ?"]

    # We used the for loop to iterate every question and then asking the answer from the user
    for question in question_list:
        print(f"{question}")
        answer = input("Enter you answer here: ") # User enters the answer
        print("") # Adds the new line between every question

        # Here the file named answer.txt will be created where all the answers will be added
        with open("answers.txt", "a") as f:
            f.write(f"{answer}\n")
    # Here we reads the data of the answers.txt file
    with open("answers.txt") as f:
        data1 = f.read()

    # Here we read the data of file.txt this file helps us to check the answers that the used entered
    with open("file.txt") as f:
        data = f.read()

    # Here we are using if else in if, if the data and data1 both content are same means the answers are same then the user will won but if it doesn't match then the user lose
    if(data1 == data):
        print("Your all answers are correct You Won")
        with open("answers.txt", "w") as f:
            f.write("")
    else:
        print("Your some answers or all answers are wrong sorry but You Lose")

play_quiz() # Function call