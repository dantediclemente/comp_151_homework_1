#Dante DiClemente, Homework 1, 2/22/17


#everything works

def average():
    number_of_scores = input("How many scores? ") #takes in a number 
    total_score = 0 #used for while loop and the number of times the user is prompted to enter a score
    score_count = 0 #takes numbers fromthe user input each time so the number value can be reset
    while (int(number_of_scores) > score_count): #while loop that decides how many times the user is prompted to enter a score
        number = input("Enter a score: ") #takes users score
        total_score += int(number) #adds score to total score
        score_count += 1 #adds 1 to the score count
    print(f"The total score is {total_score}") #prints total score
    average_score = total_score / int(number_of_scores) #finds average
    print(f"The average score is {average_score}") #prints average


#everything works 

def bar():
    number_of_bars = input("How many bars? ") #takes in number of bars
    bar_count = 0 #used for while loop
    while (int(number_of_bars) > bar_count): #amount of times user is asked to enter a size
        print('\n') #new line
        size_of_bar = input("Enter a size: ") #takes the size of the bar
        bar_size_count = 0
        while (int(size_of_bar) > bar_size_count):
           print("*", end='') #prints size of the bar
           bar_size_count += 1 #used for loop 
        bar_count += 1 #used for loop



#everything works

def tri():
    height = input("Height? ") #takes in height
    height_count = 0 #used for while loop and to print amount
    while (int(height) > height_count): 
        print("*" * height_count) #prints triangle
        height_count += 1 #adds count for while loop



#everything works

def base_tri():
    height = input("Height? ") #takes in height
    base = input("Base? ") #takes in the base
    height_count = 0 #keeps count for loop and multiplys number of stars that should be printed
    divided = int(base) / int(height) #finds starting length of stars printed
    while (int(height) >= height_count): 
        print("*" * int(divided) * height_count) #prints stars times the starting number and also multiplys it by the line you're on
        height_count += 1 #adds 1 the to height count



#everything works 

def total_tri():
    height = input("Height? ") #takes in height
    base = input("Base? ") #takes in the base
    height_count = 0 #keeps count for loop and multiplys number of stars that should be printed
    star_count = 0
    divided = int(base) / int(height) #finds starting length of stars printed
    while (int(height) >= height_count): 
        print("*" * int(divided) * height_count) #prints stars times the starting number and also multiplys it by the line you're on
        height_count += 1 #adds 1 the to height count
        stars = int(divided) * height_count #gets number of stars in row
        star_count += stars #adds number of stars in row to the total stars
    star_count = star_count - int(base) + 1 #fixes the unneeded stars from being added to the total
    print(f"There were {star_count} stars")
    area = 0.5 * int(base) * int(height) #finds area
    print(f"The triangle's area is 1/2 * base * height, which is {area}")
    


#everything works

def mortgage():
    initial_value = input("How much are you borrowing initially? ")
    yearly_interest = input("What is the yearly interest rate as a percent? ")
    monthly_payment = input("How much are you paying back each month? ")
    number_of_years = input("How many years are you paying? ")
    money_payed_each_year = int(monthly_payment) * 12 #finds amount paid each year
    year_count = 1
    year_value = (int(initial_value) - int(money_payed_each_year)) #finds how much is paid off before adding interest
    interest = year_value * (float(yearly_interest) / 100) #gets interest after subtracting payment
    year_value += interest #finds next years amount owed
    print(f"At the end of year 1 you still owe $ {year_value}")
    while (int(number_of_years) > year_count): #loops this until years are up, everything in this loop does the same as above
        year_count += 1
        year_value -= int(money_payed_each_year)
        interest = year_value * (float(yearly_interest) / 100)
        year_value += interest
        print(f"At the end of year {year_count} you still owe {year_value}")



















           
           
