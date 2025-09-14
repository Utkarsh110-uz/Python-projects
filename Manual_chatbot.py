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
class MannualChabot:
    def functions(self):
        print("The Opertion this chatbot can perform is:\nPress 1 for Calculator\nPress 2 for games\nPress 3 for Downloading Image/GIF\nPress 4 for News\nPress 5 for Generating passwords\nPress 6 for Generating tables\nPress 7 for Todo list\nPress 8 Digital clock\nPress 9 for PDF merger")

    def calculator(self):
        try:
            number1  = int(input("Enter number 1: "))
            number2  = int(input("Enter number 2: "))
            operation = input("Entre operation: ")
            if("+" in operation):
                return number1 + number2
            elif("-" in operation):
                return number1 - number2
            elif("*" in operation):
                return number1 * number2
            elif("/" in operation):
                return number1 / number2
        except ZeroDivisionError:
            print("Please entre number other than 0")