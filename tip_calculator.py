print('Welcome to the tip calculator!\n')
total = int(input('What was the total bill? '))
desired_tip = int(input('How much tip would you like to give? '))
split = int(input('How many people to split the bill? '))
shares = round(float((total * (1 + desired_tip/100 ))/split),2)
shares = "{:.2f}".format(shares)
print(f" Each person should pay: ${shares}")
