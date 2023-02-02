enter_age = int(input("Please enter your age: "))

if enter_age >= 18:
    print('You are able to participate in voting')
else:
    remain_year = 18 - enter_age
    print('Sorry! You cannot participate in voting, you will be able to participate after '+str(remain_year))