# *Note this chatbot is under development and not yet finished wait until it is finished.*
# A. Calculator.
# B. Games:
# a. snake water gun game.
# b. guess the number game.
# c. roll the dice game.
# d. stone paper scissors game.
# e. KBC game.
# f. Nuke the system game. (Play at your own risk)
# C. Image/gif downloader which gane download any image and gif. 
# D. News.
# E. Generate passwords.
# F. Generate tables.
# G. A basic to do function.
# H. Age Calculator.
# I. Digital clock
# J. Harmonice mean Calculator.
# K. PDF merger.
class ManualChatbot:
    def functions(self):
        print("The Opertion this chatbot can perform is:\nPress 1 for Calculator\nPress 2 for games\nPress 3 for Downloading Image/GIF\nPress 4 for News\nPress 5 for Generating passwords\nPress 6 for Generating tables\nPress 7 for Todo list\nPress 8 Digital clock\nPress 9 for PDF merger")

    def calculator(self, number1, number2, operation):
        print('Entre +, -, *, / in " " ')
        try:
            if("+" in operation):
                print(f"The  of two numbers are: {number1+number2}")
            elif("-" in operation):
                print(f"The subtraction of two numbers are: {number1-number2}")
            elif("*" in operation):
                print(f"The multiplication of two numbers are: {number1*number2}")
            elif("/" in operation):
                print(f"The division  of two numbers are: {number1/number2}")
        except ZeroDivisionError:
            print("Please entre number other than 0")

a = ManualChatbot()
a.calculator(10,10,"+")