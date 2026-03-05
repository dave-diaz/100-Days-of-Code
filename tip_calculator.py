# Tip Calculator
print('Welcome to the tip calculator!') 
total_bill = float(input('What was the total bill? $'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
number_of_people = int(input('How many people to split the bill? '))                  
bill_split = (total_bill + (total_bill * tip_percentage / 100)) / number_of_people
final_amount = "{:.2f}".format(bill_split)
print(f'Each person should pay: ${final_amount}')                                                                                      