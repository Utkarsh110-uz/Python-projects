# Harmonic Mean Calculator:
'''This is the harmonic mean code where we can calculate harmonic mean now lets talk about the code first user will enter the total values in total_numbers() then we used while loop and asked user to enter the number in numbers() on which we will perform harmonic mean and we have handled the 0 input problem that if someone enters 0 that iteration will be skipped and the you have to enter that value again then those values entered in numbers() then we will divide these numbers form 1 in reciproclas() then these values will be appended in reciprocals_list[] and then we will sum those values in reciprocal_sum() and then we will calculate harmonic_mean() by dividing the sumed values with the total_numbers()'''

def harmonic_mean():
    
    print("---Harmonic Mean---")
    reciprocals_list = [] # An empty list where values will be added form reciprocal
    i = 0
    total_numbers = int(input("Enter total numbers: ")) # Here user will enter the total numbers
    while(i<total_numbers):
        numbers = float(input("Enter number for harmonic mean: ")) # Here user will enter number for HM
        if(numbers == 0): # Here if someone enters 0 then that iteration  will be skipped
            input("You are entering 0 which is not valid please enter a valid number")
            continue
        reciprocal = 1/numbers # Here numbers will be divided by one
        reciprocals_list.append(reciprocal) # the divided values will be added to reciprocals_list
        i += 1

    reciprocal_sum = sum(reciprocals_list) # Here we will sum the values of reciprocals_list
    harmonic_mean = total_numbers/reciprocal_sum # Here the HM will be calculated by dividing total_numbers and reciprocal_sum
    print(f"The harmonic mean is: {round(harmonic_mean,2)}")
    print("---Thanks For Using Our Programm---")

harmonic_mean()